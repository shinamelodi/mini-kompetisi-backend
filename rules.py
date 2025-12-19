def evaluate_rules(data):
    """
    Evaluasi metode pengadaan mini kompetisi
    Output dirancang untuk:
    - justifikasi regulasi
    - checklist PPK/Pokja
    - pembuatan dokumen
    """

    catatan = []
    status = "VALID"

    # =========================
    # 1. VALIDASI DASAR
    # =========================
    if data.nilai_paket <= 0:
        return {
            "metode_pengadaan": None,
            "status": "TIDAK VALID",
            "catatan": ["Nilai paket tidak boleh nol atau negatif"]
        }

    # =========================
    # 2. PENENTUAN METODE AWAL
    # =========================
    metode = "Tender Cepat"

    if data.nilai_paket > 200_000_000_000:
        metode = "Tender"
        catatan.append("Nilai paket melebihi batas maksimal Tender Cepat")

    # =========================
    # 3. KONDISI KHUSUS
    # =========================
    if data.papua:
        metode = "Seleksi"
        catatan.append("Paket pekerjaan di wilayah Papua")

    if data.spesialis:
        metode = "Seleksi"
        catatan.append("Pekerjaan bersifat spesialis")

    if data.risiko_tinggi:
        metode = "Seleksi"
        catatan.append("Pekerjaan berisiko tinggi")

    # =========================
    # 4. VALIDASI REGULASI LANJUTAN
    # =========================
    if metode == "Tender Cepat":
        if data.spesialis:
            status = "PERLU PERHATIAN"
            catatan.append("Tender Cepat tidak sesuai untuk pekerjaan spesialis")

        if data.risiko_tinggi:
            status = "PERLU PERHATIAN"
            catatan.append("Tender Cepat tidak disarankan untuk pekerjaan berisiko tinggi")

    if metode == "Tender" and data.nilai_paket <= 200_000_000_000:
        status = "PERLU PERHATIAN"
        catatan.append("Nilai paket masih memungkinkan Tender Cepat")

    # =========================
    # 5. JUSTIFIKASI ADMINISTRATIF
    # =========================
    justifikasi = f"Metode pengadaan ditetapkan sebagai {metode} berdasarkan hasil evaluasi nilai paket dan karakteristik pekerjaan."

    return {
        "metode_pengadaan": metode,
        "status": status,
        "catatan": catatan,
        "justifikasi": justifikasi
    }

def generate_document_data(data):
    lokasi = "Papua" if data.papua else "Non Papua"

    persyaratan = [
        "Memiliki Nomor Induk Berusaha (NIB)",
        "Memiliki Sertifikat Badan Usaha (SBU) sesuai klasifikasi"
    ]

    if data.risiko_tinggi:
        persyaratan.append("Memiliki pengalaman pekerjaan sejenis")

    if data.spesialis:
        persyaratan.append("Memiliki tenaga ahli bersertifikat")

    return {
        "judul": "Dokumen Mini Kompetisi Pekerjaan Konstruksi",
        "informasi_umum": {
            "nilai_paket": data.nilai_paket,
            "metode": "Mini Kompetisi",
            "jenis_kontrak": "Harga Satuan",
            "lokasi": lokasi
        },
        "persyaratan": persyaratan,
        "metode_evaluasi": {
            "administrasi": True,
            "teknis": True,
            "harga": True
        },
        "jadwal": {
            "pengumuman": "T+0",
            "pemasukan_penawaran": "T+3",
            "evaluasi": "T+4"
        }
    }
