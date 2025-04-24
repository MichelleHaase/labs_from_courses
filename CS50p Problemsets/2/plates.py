alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
list_alpha = alphabet.split()
numbers = "1 2 3 4 5 6 7 8 9 0"
list_nums = numbers.split()


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        string_Len_Fisrt_scnd_Letter(s)
        and special_Chars(s)
        and first_nums_stuff(s)
        and only_nums_after_nums(s)
    ):
        return True


# and first_numb_stuff(s) and numb_stuff(s)


def string_Len_Fisrt_scnd_Letter(s):
    if 2 <= len(s) <= 6:
        if s[0] in list_alpha and s[1] in list_alpha:
            return True
        else:
            return False
    else:
        return False


def special_Chars(s):
    check = 0
    for i in s:
        if i not in list_alpha and i not in list_nums:
            check = 1
    if check == 0:
        return True
    else:
        return False


def first_nums_stuff(s):
    first_num = None
    for i in s:
        if i.isdigit():
            first_num = i
            break
    if first_num == "0":
        return False
    else:
        return True


def only_nums_after_nums(s):
    first_num = None
    check = 0
    for i in s:
        if i.isdigit():
            first_num = i
            break
    if first_num != None:
        index_first_num = s.find(first_num)
        location_num_in_s = len(s) - index_first_num
        for i in s[-location_num_in_s:]:
            if not i.isdigit():
                check = 1
    if check == 1:
        return False
    else:
        return True


main()
