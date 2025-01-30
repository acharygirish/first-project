# name_user = input("Enter your username : ")
# length = len(name_user)

# # print("the length of the string :" + length) str and int can't be concatenated
# print("the length of the string :" + str(length))
# print("the length of the string :", length)


print("Welcome to tip calculator :")
bill = float(input("What was your total bill?\n"))
tip = int(input("How would you like to tip 10,12 or 15?\n")) / 100
split = int(input("How many people to split?\n"))
calc = (bill + (bill * tip)) / split
final_amt = round(calc, 2)
print(f"Each person should pay : {final_amt}")
