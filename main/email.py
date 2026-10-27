from validator.email_validator import validate_email, parse_email
import hashlib

def check_email():
    email = input("\nMasukkan Email: ").strip()
    valid, msg = validate_email(email)
    if not valid:
        print(f"[GAGAL] {msg}")
        return
    
    data = parse_email(email)
    username = data['username']
    
    # Hash untuk Gravatar
    gravatar_hash = hashlib.md5(email.lower().encode()).hexdigest()
    
    print("\n========== HASIL OSINT EMAIL ==========")
    print(f"Email        : {data['email']}")
    print(f"Username     : {username}")
    print(f"Domain       : {data['domain']}")
    print(f"Provider     : {data['provider']}")
    print(f"Tebakan Nama : {data['name_guess']}")
    print(f"Status       : {msg}")
    print("---------------------------------------")
    print("🔍 JEJAK DIGITAL DARI EMAIL INI:")
    print(f"1. Gravatar (Foto Profil):")
    print(f"   https://www.gravatar.com/avatar/{gravatar_hash}")
    print(f"   https://www.gravatar.com/{gravatar_hash}?d=404 (cek ada foto atau tidak)")
    print(f"")
    print(f"2. Cari di Google (apakah email ini pernah bocor di forum):")
    print(f"   https://www.google.com/search?q=\"{data['email']}\"")
    print(f"   https://www.google.com/search?q=\"{username}\"")
    print(f"")
    print(f"3. Cek Username di Sosmed (apakah pakai username sama):")
    print(f"   【entity-GitHub¦canonical_name=GitHub】: https://github.com/{username}")
    print(f"   【entity-Instagram¦canonical_name=Instagram】: https://instagram.com/{username}")
    print(f"   Twitter/X: https://twitter.com/{username}")
    print(f"   LinkedIn: https://www.linkedin.com/in/{username}")
    print(f"")
    print(f"4. Cek Data Breach (apakah email pernah dibobol):")
    print(f"   https://haveibeenpwned.com/account/{data['email']}")
    print(f"   https://intelx.io/?s={data['email']}")
    print(f"")
    print(f"5. Info Domain Perusahaan:")
    print(f"   https://who.is/whois/{data['domain']}")
    print(f"   https://{data['domain']}")
    print("======================================\n")
