def main():
    time = input("What's the time? ").strip()
    convertedTime = convert(time)
    if 7 <= convertedTime <= 8:
        print("breakfast time")
    elif 12 <= convertedTime <= 13:
        print("lunch time")
    elif 18 <= convertedTime <= 19:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    convertedTime = float((int(hour) + (float(minutes) / 60)))
    return convertedTime


if __name__ == "__main__":
    main()
