def mask_phone_number(phone):
    masked_part = "*" * 6
    last_four_digits = phone[-4:]
    return masked_part + last_four_digits

print(mask_phone_number("9876543210"))