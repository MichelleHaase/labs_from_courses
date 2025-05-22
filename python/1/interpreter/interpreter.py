input = input("Let's do some Maths! ").strip()
x, y, z = input.split(" ")
x = int(x)
z = int(z)
if (
    isinstance(x, int)
    and isinstance(z, int)
    and (y == "+" or y == "-" or y == "*" or y == "/")
):
    match y:
        case "+":
            print(f"{(x+z):.1f}")
        case "-":
            print(f"{(x-z):.1f}")
        case "*":
            print(f"{(x*z):.1f}")
        case "/":
            print(f"{(x/z):.1f}")
