from pydantic import BaseModel

class RuleInput(BaseModel):
    nilai_paket: int
    papua: bool = False
    spesialis: bool = False
    risiko_tinggi: bool = False
