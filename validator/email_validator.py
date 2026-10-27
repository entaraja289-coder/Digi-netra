import re

DISPOSABLE = ["tempmail","10minutemail","guerrilla","mailinator","yopmail","fakeemail"]
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    email=email.strip().lower()
    if not re.match(EMAIL_REGEX, email):
        return False,"Format email salah"
    if len(email)>254:
        return False,"Email kepanjangan"
    local, domain = email.split("@",1)
    for d in DISPOSABLE:
        if d in domain:
            return False,f"Disposable terdeteksi ({d})"
    return True,"Format Valid"

def parse_email(email):
    email=email.strip().lower()
    local, domain=email.split("@",1)
    name_guess=local.replace("."," ").replace("_"," ").title()
    provider="Custom Domain"
    if "gmail" in domain: provider="Google (Gmail)"
    elif "yahoo" in domain: provider="Yahoo"
    elif "outlook" in domain or "hotmail" in domain: provider="Microsoft"
    elif "proton" in domain: provider="ProtonMail"
    elif "icloud" in domain: provider="Apple iCloud"
    return {"email":email,"username":local,"domain":domain,"provider":provider,"name_guess":name_guess}
