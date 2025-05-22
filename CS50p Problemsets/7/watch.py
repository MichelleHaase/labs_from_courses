import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if Url := re.search(
        r"(iframe)?.*src=\"http[s]?://(www\.)?youtube\.com/embed/(?P<URL>\w+)", s
    ):
        # print(f"https://youtu.be/{Url.group("URL")}")
        return f"https://youtu.be/{Url.group("URL")}"
    else:
        return None


if __name__ == "__main__":
    main()
