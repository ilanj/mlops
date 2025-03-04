from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class NumberInput(BaseModel):
    number: int

@app.post("/square")
def square_number(input: NumberInput):
    return {"square": input.number ** 2}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
