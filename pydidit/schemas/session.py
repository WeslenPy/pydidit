from enum import Enum
from pydantic import BaseModel, EmailStr,HttpUrl,Base64Str
from pydidit.schemas.common import (CallbackMethodEnum, ContactDetails,
                                  ExpectedDetails, LanguageEnum, 
                                  SandboxScenarioEnum, StatusEnum)

    
class CreateSessionRequest(BaseModel):
    workflow_id: str #id of the workflow to be executed (required)
    callback:str | None = None #callback url for the session (optional)
    
    vendor_data:str | None = None #identificator for the vendor (optional)
    callback_method:CallbackMethodEnum | None = None #callback method for the session (optional)

    metadata:dict | None = None #Arbitrary JSON object stored with the session and echoed back in webhooks. (optional)
    
    language:LanguageEnum | None = None # Browser language is auto-detected when omitted. (optional)
    
    contact_details:ContactDetails | None = None #Email address or phone number of the user. (optional)
    
    expected_details:ExpectedDetails | None = None #Expected details of the user. (optional)
    
    portrait_image: Base64Str | None = None #Base64-encoded face image (max 2MB; JPEG, PNG, WebP, or TIFF). Reference face for Biometric Authentication / Face-Match-first workflows. Optional when the vendor_data user already has a stored face (approved liveness face, ePassport photo, ID document portrait, or enrolled profile face): Didit reuses it automatically; 400 if neither is available. (optional)
    
    sandbox_scenario:SandboxScenarioEnum | None = None #Sandbox-only scenario slug (e.g. approve, decline_aml_hit) that auto-populates the session with magic inputs. (optional)
    
    
class CreateSessionResponse(BaseModel):
    session_id: str #Unique UUID for this session. Use it for GET /v3/session/{sessionId}/decision/ and webhooks.
    session_number: str| int #Human-readable sequence number shown in the Didit console.
    session_token: str #12-character URL-safe token that authorizes the end user to open the hosted flow, and initialises the native SDKs (the web SDK takes url instead). Treat it as a secret.
    url: str #Hosted verification URL to redirect the user to, or embed in an iframe. (Field name is url, not verification_url.) When the request includes language, the URL contains a language path segment — e.g. https://verify.didit.me/en/session/3FaJ9wLqX2Mz.
   
   
    vendor_data:str | None = None #identificator for the vendor (optional)
    callback:str | None = None #callback url for the session (optional)
    metadata:dict | None = None #Arbitrary JSON object stored with the session and echoed back in webhooks. (optional)
    status:StatusEnum #Current status — "Not Started" for a newly created session.
   
    workflow_id: str  #Stable workflow identifier the session runs on.
    workflow_version: str | int #Published workflow version the session was pinned to at creation.
    
    
    # {'session_id': 'eaba6ece-de0b-45b3-8438-b67e28df1dcb', 'session_number': 4, 'session_token': 'BJ_jHJ_Mvu64', 'url': 'https://verify.didit.me/session/BJ_jHJ_Mvu64', 'vendor_data': None, 'metadata': None, 'status': 'Not Started', 'callback': 'https://example.com/callback', 'workflow_id': 'eb1b299a-8457-4e97-aae7-f11f972f8bbc', 'workflow_version': 1}