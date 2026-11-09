def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


print(
    validate_pin("1234"), 
    validate_pin("0000"), 
    validate_pin("1111"), 
    validate_pin("123456"),
    validate_pin("098765"),
    validate_pin("000000"),
    validate_pin("123456"),
    validate_pin("090909"),

)