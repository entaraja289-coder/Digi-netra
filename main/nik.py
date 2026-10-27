import getpass
from validator.nik_validator import validate_nik, parse_nik, estimate_birth_year
from datetime import datetime

def check_nik():
    try:
        nik = getpass.getpass("\nMasukkan NIK 16 digit (hidden): ").strip()
    except:
        nik = input("\nMasukkan NIK 16 digit: ").strip()
    
    print("[*] NIK disembunyikan untuk privasi")
    valid, msg = validate_nik(nik)
    if not valid:
        print(f"[GAGAL] {msg}")
        return
    
    data = parse_nik(nik)
    tahun = estimate_birth_year(data['tahun'])
    umur = datetime.now().year - tahun
    
    print("\n========== HASIL CEK NIK ==========")
    print(f"Kode Wilayah : {data['kode_wilayah']}")
    print(f"Tgl Lahir    : {data['tgl']}-{data['bulan']}-{tahun}")
    print(f"Gender       : {data['gender']}")
    print(f"Umur         : {umur} tahun")
    print(f"Status       : {msg}")
    print("===================================\n")

