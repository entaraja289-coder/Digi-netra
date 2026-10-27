from validator.phone_validator import normalize_and_validate, get_phone_info

def check_phone():
    raw = input("\nMasukkan nomor HP: ").strip()
    print("[+] Validating...")
    is_valid, fixed, parsed = normalize_and_validate(raw)
    if not is_valid:
        print("[!] Invalid")
        return
    region, provider = get_phone_info(parsed)
    print(f"[OK] Valid! {region} | {provider}")
