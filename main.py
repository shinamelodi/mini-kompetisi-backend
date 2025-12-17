from fastapi import FastAPI
from schemas import RuleInput
from rules import evaluate_rules

app = FastAPI(
    title="Mini Kompetisi API",
    description="API evaluasi mini kompetisi PBJ",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "Backend Mini Kompetisi Aktif"}

@app.post("/rules/evaluate")
def evaluate(data: RuleInput):
    return evaluate_rules(data)
