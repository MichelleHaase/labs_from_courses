
def main():
    while True:
        fuel_input = input("Current state: ").strip()
        try:
            x,y = fuel_input.split("/")
            if x <= y and int(x) > 0 and int(y) > 0:
                x = int(x)
                y = int(y)
            else: 
                continue
            
        except (ValueError, UnboundLocalError):
            print("please provide a fraction of whole positive numbers, divided by a '/' ")
        else:
            break
        
    print(convert(x,y))

def convert(numerator,denominator):
    try:
        result = round((numerator/denominator) *100) 
    except ZeroDivisionError:
        main()
    
    if result <= 1:
        result = "E"
    elif result >= 99:
        result = "F"
    else:
        result = str(result) + "%"
    return result



if __name__ == "__main__":
    main()