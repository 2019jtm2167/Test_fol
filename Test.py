def switch():
    num1 = int(input("enter a velue:"))
    num2 = int(input("enter another value:"))
    print("press 1 for adition \n press 2 for sub \n press 3 for mul \n press 4 for div ")
    option = int(input("ur option:"))

    def add():
        result = num1 + num2
        print(result)

    def sub():
        result = num1 - num2
        print(result)

    def mul():
        result = num1 * num2
        print(result)

    def div():
        result = num1 / num2
        print(result)

    dict = {
        1: add,
        2: sub,
        3: mul,
        4: div}
    dict.get(option)()  # () this indicate the () used in add, sub, mul, div
    # or we can say that calling of functions

while(1):
    buffer=int(input("1 : Calculator \n 2 : Exit "))
    if(buffer == 1 ):
        switch()
    elif(buffer ==2 ):
        exit()
    else:
        print("U entered wrong choice")