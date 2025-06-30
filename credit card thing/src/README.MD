# Credit Card Brand Discovery

This project provides a Python function to discover the brand of a credit card based on its number prefix.

## Supported Brands
- Visa
- Mastercard
- American Express
- Diner's Club
- Discover
- Elo
- Hipercard
- Voyager
- Maestro
- JCB

## Usage

1. Run the script and enter a credit card number when prompted:

```bash
python index.py
```

2. The script will print the detected brand, for example:

```
Enter a credit card number: 4111111111111111
Visa
```

## Function Reference

### `discover_brand_from_number(card_number)`

Returns the credit card brand based on the card number prefix.

**Parameters:**
- `card_number` (str or int): The credit card number to check.

**Returns:**
- `str`: The brand name (e.g., 'Visa', 'Mastercard', etc.) or 'Unknown' if not recognized.

## Example

```python
print(discover_brand_from_number('4111111111111111'))  # Visa
print(discover_brand_from_number('6011111111111117'))  # Discover
print(discover_brand_from_number('3528000000000000'))  # JCB
```

---

Feel free to extend the function with more brands or custom logic as needed.
