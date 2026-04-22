#write a python function which will take user input as a number and will print table of that number
#git add
#git commit -m 
#git push 
def table(number):
    for i in range(1,11):
        print(f"{number}* {i} = {number*i}")
    
table(int(input("Enter a number: ")))