from langchain_core.pydantic_v1 import BaseModel, Field

class Math_Output(BaseModel):
    """Output format for each input math word problem"""
    answer: str = Field(..., description="The step by step description of how to solve the question")
    result: str = Field(..., description="Single number only result")
    
