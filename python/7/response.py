from validator_collection import is_email

if is_email(input("E-Mail: ").strip()):
    print("Valid")
else:
    print("Invalid")
