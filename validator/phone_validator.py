import phonenumbers

def normalize_and_validate(raw_number):
    raw = raw_number.strip().replace(" ","").replace("-","")
    if raw.startswith("0"): 
        raw = "+62"+raw[1:]
    elif raw.startswith("62") and not raw.startswith("+"): 
        raw = "+"+raw
    elif not raw.startswith("+"): 
        raw = "+"+raw
    try:
        parsed = phonenumbers.parse(raw, None)
        is_valid = phonenumbers.is_valid_number(parsed)
        return is_valid, raw, parsed
    except: 
        return False, raw, None

def get_phone_info(parsed):
    try:
        from phonenumbers import geocoder, carrier
        region = geocoder.description_for_number(parsed,"id")
        provider = carrier.name_for_number(parsed,"id")
        return region, provider
    except: 
        return "-","-"
