# The if statement is a conditional statement in python, 
# That is used to determine whether a block of code will be executed or not. 
# Meaning if the program finds the condition defined in the if statement to be true, 
# It will go ahead and execute the code block inside the if statement

body_heat = 35

if body_heat > 30:
    print("It's a humid day")
    print("Stay indoors")
elif body_heat > 20:
    print("It's a beautiful day") # (20, 30]
elif body_heat > 10:
    print("It's a tad bit freezing!") #(10, 20]
else:
    print("It's freezing!")
print("Done!")