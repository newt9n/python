#small program to conduct simple payroll
name = input("Tell me your name? ")
print ("Let's do payroll", name + "!")
rate = input("What is your current hourly rate? ")
rate = float(rate)
hours = input("How many Hours have you worked? ")
hours = int(hours)
print("Your total pay is $", rate*hours)
print("You need to work harder", name + "!")
#end
