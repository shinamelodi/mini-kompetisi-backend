from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import PaketInput, AturanOutput
from rules import evaluate_rules

app = FastAPI(
    title="Mini Kompetisi Rule Engine",
    version="1.0.0"
)

# CORS supaya React bisa akses
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # nanti bisa dipersempit
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend Mini Kompetisi Aktif"}

@app.post("/rules/evaluate", response_model=AturanOutput)
def evaluate(paket: PaketInput):
    return evaluate_rules(paket)
