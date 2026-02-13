from openai import OpenAI
from app.core.schemas import SecurityFinding


def analyze_smart_contract(contract_code: str) -> list[SecurityFinding]:
    client = OpenAI()

    prompt = f"""
    You are a senior smart contract security auditor well versed in finding vulnerabilities in solidity code
    Analyze the following Solidity smart contract.
    Identify potential vulnerabilities if present.
    For each vulnerabilty found, provide the following details:
    - Title: A brief title of the vulnerability.
    - Description: A detailed description of the vulnerability.
    - Severity: The severity level of the vulnerability (e.g., High, Medium, Low).
    - Impact: The potential impact of the vulnerability.
    - Mitigation: Recommended steps to mitigate the vulnerability.
    - Confidence: Provide a confidence score between 0 and 1.

    If unsure, state that the issue requires human review.
    Here's the Smart Contract Code:
{contract_code}
"""

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
        # output_schema=SecurityFinding
    )

    return {
        "analysis": response.output_text
    }