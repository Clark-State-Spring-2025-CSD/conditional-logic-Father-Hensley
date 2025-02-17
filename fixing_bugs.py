
#Updated 1 Feb 2025
#Fix the below code so the file will run. Do not add additional lines of code, only fix the existing lines.
#You may have to add or remove characters. Remember, you can restore the file from the repo in GitHub Desktop if you
#want to start over.

#The output should be:
#"You entered a" if the user enters a
#"You entered a b" if the user enters b
#"Well it wasn't an a or b" if the user enters anything else


selection = input("Enter a lowercase letter - ")

if selection == "a":
    print("You entered a")
elif selection == "b":
    print("You entered a b")
else:
    print("Well it wasn't an a or b.")

