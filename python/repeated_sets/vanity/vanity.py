def main():
        plate = input().strip()
        if valid(plate) is True:
            print("All right")
        else:
            print("Nope")


def valid(input_plate):
      
    if first_letters_valid (input_plate) and length_valid (input_plate) and numbers_valid (input_plate): 
      return True
    
    return False


def first_letters_valid(plate):
    # first two chars need to be letters no special chars at all
   
    if plate.isalnum() is False:
        return False
    
    if plate[:2].isalpha() is False:
        return False
    return True
    

def length_valid(plate):
    # length 2-6 chars
    if  len(plate) < 2 or len(plate) > 6:
        return False
    return True

def numbers_valid(plate):
    # numbers only at the end first num not 0
    first_num = None
    for digit in plate:
        if digit.isnumeric():
            first_num = digit
            break

    if first_num == None:
        return True
    
    if first_num == "0":
        return False
    
    part1,part2 = plate.split(first_num,maxsplit=1)
    if part2.isnumeric():
        return True

    return False



if __name__ == "__main__":
    main()