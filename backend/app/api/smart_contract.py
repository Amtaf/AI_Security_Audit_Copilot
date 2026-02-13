from fastapi import APIRouter
from app.core.llm import analyze_smart_contract
from app.core.schemas import SmartContractRequest

router = APIRouter(prefix="/smart_contract", tags=["smart_contract"])
@router.post("/analyze")

# def analyze(contract_code: str):
#     return analyze_smart_contract(contract_code)
def analyze(request: SmartContractRequest):
    return analyze_smart_contract(request.contract_code)