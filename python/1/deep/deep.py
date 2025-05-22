input = (
    input(
        "What's the answer to the Great Question of Life, the Universe and Everything? "
    )
    .strip()
    .lower()
)
if input == "42" or input == "forty-two" or input == "forty two":
    print("Yes")
else:
    print("No")
