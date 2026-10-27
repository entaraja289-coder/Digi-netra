from validator.nik_validator import validate_nik, parse_nik, estimate_birth_year
from datetime import datetime

def check_nik():
    nik = input("\nMasukkan NIK 16 digit: ").strip()
    valid, msg = validate_nik(nik)
    if not valid:
        print(f"[GAGAL] {msg}")
        return
    data = parse_nik(nik)
    tahun = estimate_birth_year(data['tahun'])
    print(f"\nWilayah: {data['kode_wilayah']}")
    print(f"Tgl: {data['tgl']}-{data['bulan']}-{tahun}")
    print(f"Gender: {data['gender']}")
