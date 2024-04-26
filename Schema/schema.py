from langchain_core.pydantic_v1 import BaseModel, Field

class Math_Output(BaseModel):
    """Output format for each input math word problem"""
    answer: str = Field(..., description="The step by step description of how to solve the question")
    result: str = Field(..., description="Single number only result")

class Compare_Output(BaseModel):
    """Output format for comparing two potential solution for a question"""
    reasoning: str = Field(..., description="Reason for making the choice")
    choice: str = Field(..., description="1 if the first solution is correct and 2 if the second solution is correct")

    
