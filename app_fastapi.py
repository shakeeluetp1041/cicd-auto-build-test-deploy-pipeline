from fastapi import FastAPI
from pydantic import BaseModel # For data-valiadation

app = FastAPI() #Instance

class FibonacciInput(BaseModel):
    count: int

def generate_fibonacci(n: int):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
@app.get("/")
def title():
    return {"message": "Febanacci Series App"}
@app.post("/fibonacci")
def get_fibonacci(data: FibonacciInput):
    count = data.count
    if count < 0:
        return {"error": "Count must be non-negative"}
    return {"fibonacci": generate_fibonacci(count)}