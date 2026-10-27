def validate_nik(nik):
    nik=nik.strip()
    if not nik.isdigit(): return False,"NIK harus angka"
    if len(nik)!=16: return False,f"Harus 16 digit, kamu {len(nik)}"
    day=int(nik[6:8]); month=int(nik[8:10])
    real=day-40 if day>40 else day
    if not 1<=real<=31: return False,f"Tgl {day} salah"
    if not 1<=month<=12: return False,f"Bln {month} salah"
    return True,"Format Valid"

def parse_nik(nik):
    day=int(nik[6:8])
    return {"kode_wilayah":nik[0:6],"kode_provinsi":nik[0:2],"tgl":day-40 if day>40 else day,"bulan":nik[8:10],"tahun":nik[10:12],"gender":"Perempuan" if day>40 else "Laki-laki"}

def estimate_birth_year(two_digit):
    y=int(two_digit)
    return 1900+y if y>30 else 2000+y
