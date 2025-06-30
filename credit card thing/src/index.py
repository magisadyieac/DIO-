def discover_brand_from_number(card_number):
    """Returns the credit card brand based on the card number prefix."""
    card_number = str(card_number)
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number.startswith('5'):
        return 'Mastercard'
    elif card_number.startswith('3'):
        if card_number.startswith('34') or card_number.startswith('37'):
            return 'American Express'
        elif card_number.startswith('36') or card_number.startswith('38') or card_number.startswith('39') or card_number.startswith('30'):
            return "Diner's Club"
        elif card_number.startswith('35'):
            return 'JCB'
        elif card_number.startswith('300') or card_number.startswith('301') or card_number.startswith('302') or card_number.startswith('303') or card_number.startswith('304') or card_number.startswith('305'):
            return "Diner's Club"
        elif card_number.startswith('3095'):
            return 'JCB'
    elif card_number.startswith('6'):
        if card_number.startswith('6011') or card_number.startswith('65') or card_number.startswith('644') or card_number.startswith('645') or card_number.startswith('646') or card_number.startswith('647') or card_number.startswith('648') or card_number.startswith('649'):
            return 'Discover'
        elif card_number.startswith('636368') or card_number.startswith('636297'):
            return 'Elo'
        elif card_number.startswith('60'):
            return 'Hipercard'
    elif card_number.startswith('8699'):
        return 'Voyager'
    elif card_number.startswith('38') or card_number.startswith('39'):
        return 'Hipercard'
    elif card_number.startswith('50') or card_number.startswith('56') or card_number.startswith('57') or card_number.startswith('58'):
        return 'Maestro'
    # JCB extended prefixes
    jcb_prefixes = ['2100', '1800', '3088', '3096', '3112', '3158', '3337', '3528']
    if any(card_number.startswith(prefix) for prefix in jcb_prefixes):
        return 'JCB'
    return 'Unknown'

# Example usage:
# print(discover_brand_from_number('4111111111111111'))  # Visa
# print(discover_brand_from_number('6011111111111117'))  # Discover
# print(discover_brand_from_number('3528000000000000'))  # JCB
credit_card_number = input("Enter a credit card number: ")
print(discover_brand_from_number(credit_card_number))
