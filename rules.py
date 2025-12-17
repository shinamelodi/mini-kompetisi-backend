def evaluate_rules(paket):
    nilai = paket.nilai_paket

    # Kualifikasi usaha
    if nilai <= 15_000_000_000:
        kualifikasi = "Usaha Kecil"
    elif nilai <= 50_000_000_000:
        kualifikasi = "Usaha Menengah"
    else:
        kualifikasi = "Usaha Besar"

    # Jaminan penawaran
    jaminan_penawaran = nilai >= 10_000_000_000

    # Papua (OAP)
    subkontrak_oap = paket.papua

    return {
        "kualifikasi": kualifikasi,
        "jaminan_penawaran": jaminan_penawaran,
        "subkontrak_oap": subkontrak_oap,
        "max_pekerjaan_utama": 4
    }
