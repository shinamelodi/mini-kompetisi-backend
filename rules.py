def evaluate_rules(data):
    metode = "Tender Cepat"

    if data.nilai_paket > 200_000_000_000:
        metode = "Tender"

    if data.papua or data.spesialis or data.risiko_tinggi:
        metode = "Seleksi"

    return {
        "metode_pengadaan": metode
    }
