def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def subtract(a,b):
    return a - b 
def divide(a,b):
    if b == 0:
        return a
    else:
        return a / b

history = []

cont = True

print("+=+=+= Calculator =+=+=+")
while cont:
    choice = int(input("Choose one option : \n1. Calculate\n2. Watch History\n3. Exit\nChoice : "))
    if choice == 1:
        numberOfInputs = int(input("Enter number of inputs : "))
        if numberOfInputs:
            a = int(input("Enter the first number : "))
            for i in range(numberOfInputs - 1):
                b = int(input("Choose an operator : " \
                              "\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nChoice : "))
                c = int(input("Enter the next number : "))
                if b == 1:
                    d = add(a,c)
                elif b == 2:
                    d = subtract(a,c)
                elif b == 3:
                    d = multiply(a,c)
                elif b == 4:
                    if c !=0 :
                        d = divide(a,c)
                else : continue
                a = d
                print("= " , d)
        else:
            continue
        
        history.append(d)
        d = 0

    elif choice == 2:
        print("History : - " , history)
    elif choice == 3:
        print("Sayonara.")
        cont = False
    else:
        continue