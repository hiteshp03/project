import random
select = ['snake, water, gun']
selec1 = ["  1      2     3 "]
print(select)
print(selec1)
user = int(input())
comp = random.randint(1,3)
if (user == 1 and comp == 1):
    print("Both Select Same")
    print("Draw")
elif(user == 1 and comp == 2):
    print("computer select :", comp)
    print("You Win")
elif(user == 1 and comp == 3):
    print("computer select :", comp)
    print("Computer Win")

if (user == 2 and comp == 1):
    print("computer select :",comp)
    print("Computer Win")
elif(user == 2 and comp == 2):
    print("Both Select Same")
    print("Draw")
elif(user == 2 and comp == 3):
    print("computer select :", comp)
    print("You Win")

if (user == 3 and comp == 1):
    print("computer select :",comp)
    print("You Win")
elif(user == 3 and comp == 2):
    print("computer select :",comp)
    print("Computer Win")
elif(user == 3 and comp == 3):
    print("Both Select Same")
    print("Draw")

