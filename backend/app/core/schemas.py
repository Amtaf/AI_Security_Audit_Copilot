from pydantic import BaseModel
from typing import List

class SmartContractRequest(BaseModel):
    contract_code: str
class SecurityFinding(BaseModel):
    title: str
    description: str
    severity: str
    impact: str
    mitigation: str
    confidence: str