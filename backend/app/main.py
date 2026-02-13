from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.smart_contract import router as smart_contract_router

load_dotenv()
app = FastAPI(title="AI Security Audit Copilot")
app.include_router(smart_contract_router)
