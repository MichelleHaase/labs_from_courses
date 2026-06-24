from queue import Empty


input1 = input("Hi, Whats your name? ").strip()

if input1 != "" :
    print("hello, " + input1)
else :
    print("I asked your name... kinda rude")