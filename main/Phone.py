import getpass
from validator.phone_validator import normalize_and_validate, get_phone_info

def check_phone():
    try:
        raw = getpass.getpass("\nMasukkan nomor HP (hidden): ")
    except:
        raw = input("\nMasukkan nomor HP: ")
    print("[*] Nomor disembunyikan untuk privasi")
    is_valid, fixed, parsed = normalize_and_validate(raw)
    if not is_valid:
        print("[!] Invalid phone number")
        return
    region, provider = get_phone_info(parsed)
    print(f"[OK] Valid! {region} | {provider}")
    print(f"[+] WA: https://wa.me/xxx{fixed[-4:]}")
