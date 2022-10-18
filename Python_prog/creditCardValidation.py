from datetime import*
def validateCard(expDate):
    if expDate>datetime.now().date():
        return "valid"
    else:
        return 'expired'
