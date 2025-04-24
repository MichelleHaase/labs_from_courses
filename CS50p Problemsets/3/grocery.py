Dict1 = {}
while True:
    try:
        input1 = input().strip().upper()
        if input1 in Dict1:
            Dict1[input1] = Dict1[input1] + 1
        else:
            Dict1[input1] = 1
    except EOFError:
        break
for i in sorted(Dict1):
    print(Dict1[i], i)
