## from day of birth calculate how many days that person has lived, in minutes round(0)
# output in words without and "Five hundred twenty-five thousand, six hundred minutes"
# assume they where born on midnght on that date
# datetime.date.today for current day

import inflect
from datetime import date
import sys


def main():
    print(days(input("What's your Birthday? ").strip()))


def days(Birthday):
    try:
        days = date.today() - date.fromisoformat(Birthday)
    except ValueError:
        sys.exit("Invalid Date format")
    return minutes(days)


def minutes(days):
    engine = inflect.engine()
    minutes = int(round(float(str(days).split("day")[0]), 0)) * 24 * 60
    minutes_text = engine.number_to_words(minutes).replace(" and", "").capitalize()
    return f"{minutes_text} minutes"


if __name__ == "__main__":
    main()
