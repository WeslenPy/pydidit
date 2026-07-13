from datetime import date
from enum import Enum
from pydantic import BaseModel, EmailStr,HttpUrl,Base64Str



class CallbackMethodEnum(str,Enum):
    INITIADOR = "initiator"
    COMPLETER = "completer"
    BOTH = "both"


class LanguageEnum(str,Enum):
    EN = "en"
    ES = "es"
    PT = "pt"
    FR = "fr"
    DE = "de"
    IT = "it"
    JA = "ja"
    KO = "ko"


class SandboxScenarioEnum(str,Enum):
    APPROVE = "approve"
    DECLINE_AML_HIT = "decline_aml_hit"
    
class DocumentTypeEnum(str,Enum):
    PASSPORT = "P"
    NATIONAL_ID = "ID"
    DRIVING_LICENSE = "DL"
    RESIDENCE_PERMIT = "RP"
    HEALTH_INSURANCE_CARD = "HC"
    TAX_CARD = "TC"
    SOCIAL_SECURITY_CARD = "SS"
    
    
    
class StatusEnum(str,Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    RESUBMITTED = "Resubmitted"
    AWAITING_USER = "Awaiting User"
    APPROVED = "Approved"
    DECLINED = "Declined"
    ABANDONED = "Abandoned"
    EXPIRED = "Expired"
    KYC_EXPIRED = "Kyc Expired"
    IN_REVIEW = "In Review"
    
class ContactDetails(BaseModel):
    email: EmailStr | None = None #Email address (optional)
    phone: str | None = None #Phone number (optional)
    email_lang: LanguageEnum | None = None #Email language (optional)
    send_notification_emails:bool | None = None #Whether to send notification emails to the user. (optional)
    
    
class ExpectedDetails(BaseModel):
    first_name: str | None = None #First name (optional)
    last_name: str | None = None #Last name (optional)
    date_of_birth: date | None = None #Date of birth (optional)
    expected_document_types: list[DocumentTypeEnum] | None = None #Expected document types (optional)