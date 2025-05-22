list_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        input1 = input("Date: ").strip()
        try:
            if split_slash(input1) == False and split_str(input1):
                month, day, year = split_str(input1)
            elif split_str(input1) == False and split_slash(input1):
                month, day, year = split_slash(input1)
            try:
                if int(day) <= 31 and int(month) <= 12:
                    if int(month) < 10:
                        month = "0" + str(month)
                    if int(day) < 10:
                        day = "0" + day
                    print(year, "-", month, "-", day, sep="")
                    break
            except UnboundLocalError:
                continue
        except ValueError:
            continue


def split_slash(input1):
    if "/" in input1:
        month, day, year = input1.split("/")
        return month, day, year
    else:
        return False


def split_str(input1):
    if "/" not in input1:
        month1, day1, year = input1.split(" ")
        if day1.endswith(","):
            day = day1.removesuffix(",")
            if month1 in list_months:
                month = (list_months.index(month1)) + 1
                return month, day, year

            else:
                return False
        else:
            return False

    else:
        return False


main()
