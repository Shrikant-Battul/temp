def table(number):
    for i in range(0,11):
        print(f"{number}* {i} = {number*i}")
    
table(int(input("Enter a number: ")))