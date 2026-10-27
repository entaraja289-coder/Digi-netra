from validator.email_validator import validate_email, parse_email

def check_email():
    email = input("\nMasukkan Email: ").strip()
    valid, msg = validate_email(email)
    if not valid:
        print(f"[GAGAL] {msg}")
        return
    data = parse_email(email)
    print(f"\nEmail: {data['email']}")
    print(f"Provider: {data['provider']}")
    print(f"Status: {msg}")
