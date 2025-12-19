from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RuleInput
from rules import evaluate_rules
from rules import evaluate_rules, generate_document_data

app = FastAPI(
    title="Mini Kompetisi API",
    description="API evaluasi mini kompetisi PBJ",
    version="1.0.0"
)

# 🔴 INI YANG PENTING
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # nanti bisa dipersempit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend Mini Kompetisi Aktif"}

@app.post("/rules/evaluate")
def evaluate(data: RuleInput):
    return evaluate_rules(data)

@app.post("/documents/generate")
def generate_document(data: RuleInput):
    return generate_document_data(data)
