from pydantic import BaseModel

class PaketInput(BaseModel):
    nilai_paket: int
    papua: bool
    spesialis: bool
    risiko_tinggi: bool

class AturanOutput(BaseModel):
    kualifikasi: str
    jaminan_penawaran: bool
    subkontrak_oap: bool
    max_pekerjaan_utama: int
