import re
import sys


def main():
    print(convert(input("Hours: ").strip()))

# [0-5][0-9]
def convert(s):
    if time := re.search(r"^(1[0-2]|0?[1-9])(\:[0-5][0-9])? (AM|PM).*to (1[0-2]|0?[1-9])(\:[0-5][0-9])? (AM|PM)$", s.strip()):
        if time.group(1) != "":
            first_time = int(time.group(1))
            first_time_sec = time.group(2)
            frist_time_spec = time.group(3)
            second_time = int(time.group(4))
            second_time_sec = time.group(5)
            second_time_spec = time.group(6)
            if frist_time_spec == "PM" and first_time != 12:
                first_time = first_time + 12
            if second_time_spec == "PM" and second_time != 12:
                second_time = second_time + 12
            if first_time == 12:
                if frist_time_spec == "AM":
                    first_time = 0
            if second_time == 12:
                if second_time_spec == "AM":
                    second_time = 0


            if first_time_sec == None:
                first_time_sec = ":00"
            if second_time_sec == None:
                second_time_sec = ":00"
            return f"{first_time:02}{first_time_sec} to {second_time:02}{second_time_sec}"
    else:
        raise ValueError





if __name__ == "__main__":
    main()
