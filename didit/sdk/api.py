from pydantic import BaseModel, ValidationError
from didit.schemas.error import AuthenticationError
from didit.schemas.session import CreateSessionRequest, CreateSessionResponse
from httpx import AsyncClient, Response
from urllib.parse import urljoin

class DiditAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://verification.didit.me/v3/"
        
        self._headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
    async def _post(self, url:str, *args:tuple, **kwargs:dict):
        print(url)
        async with AsyncClient(base_url=self.base_url, headers=self._headers) as client:
            return await client.post(url, *args, **kwargs)
        
    async def _get(self, url:str, *args:tuple, **kwargs:dict):
        async with AsyncClient(base_url=self.base_url, headers=self._headers) as client:
            return await client.get(url, *args, **kwargs)
        
    def _prepare_request(self, data:BaseModel):
        return data.model_dump(exclude_none=True)
    
    def _prepare_url(self, path:str):
        return urljoin(self.base_url, path)
    
    def _prepare_response(self, response: Response, schema: BaseModel):
        response_json = response.json()
        try:
            return schema.model_validate(response_json, strict=False)
        except ValidationError as e:
            error = response_json.get("detail", e.errors())
            raise AuthenticationError(detail=error, status_code=response.status_code)
        
    async def create_session(self, request: CreateSessionRequest)->CreateSessionResponse|AuthenticationError:
        
        url = self._prepare_url("session")
        response = await self._post(url, json=self._prepare_request(request))
        return self._prepare_response(response, CreateSessionResponse)
    
    
    async def decision_session(self, session_id: str):
        url = self._prepare_url(f"session/{session_id}/decision")
        return await self._get(url)