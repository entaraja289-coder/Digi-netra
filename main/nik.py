def validate_nik(nik):
    nik=nik.strip()
    if not nik.isdigit(): return False,"Harus angka"
    if len(nik)!=16: return False,f"Harus 16 digit"
    day=int(nik[6:8]); month=int(nik[8:10])
    real=day-40 if day>40 else day
    if not 1<=real<=31: return False,"Tgl salah"
    if not 1<=month<=12: return False,"Bln salah"
    return True,"Valid"
def parse_nik(nik):
    day=int(nik[6:8])
    return {"kode_wilayah":nik[0:6],"tgl":day-40 if day>40 else day,"bulan":nik[8:10],"tahun":nik[10:12],"gender":"Perempuan" if day>40 else "Laki-laki"}
def estimate_birth_year(two):
    y=int(two); return 1900+y if y>30 else 2000+y
