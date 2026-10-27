import re
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def validate_email(email):
    email=email.strip().lower()
    if not re.match(EMAIL_REGEX, email): return False,"Format salah"
    return True,"Valid"
def parse_email(email):
    local,domain=email.strip().lower().split("@",1)
    return {"email":email,"username":local,"domain":domain,"provider":"Gmail" if "gmail" in domain else "Custom"}
