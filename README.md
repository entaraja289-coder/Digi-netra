import getpass
from validator.phone_validator import normalize_and_validate, get_phone_info

def check_phone():
    # Input nomor jadi hidden kayak password
    try:
        raw = getpass.getpass("\nMasukkan nomor HP (input hidden): ").strip()
    except:
        # Kalau di HP gak support getpass, pakai input biasa
        raw = input("\nMasukkan nomor HP: ").strip()
    
    print("\n[+] Validating phone number...")
    print("[*] Nomor disembunyikan untuk privasi")
    
    is_valid, fixed, parsed = normalize_and_validate(raw)
    
    if not is_valid:
        print(f"[!] Invalid phone number.")
        print("[!] Coba lagi dengan format 0857... atau +62...")
        return

    region, provider = get_phone_info(parsed)
    print(f"[OK] Valid! Region: {region} | Provider: {provider}")
    # Gak tampilin nomor full lagi, cuma 4 digit akhir
    print(f"[+] WA: https://wa.me/xxxx{fixed[-4:]}")
    print("[*] Nomor lengkap tidak ditampilkan di layar")
