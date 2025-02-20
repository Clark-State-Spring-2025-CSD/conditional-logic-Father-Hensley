#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.
def month_season(month):
        if month in [2, 3, 4]:
            return "Spring"
        elif month in [5, 6, 7]:
            return "Summer"
        elif month in [8, 9, 10]:
            return "Fall"
        else:
            return "Winter"
        
month = int(input("Input the month by its number (1-12): "))
print(f"The season is: {month_season(month)}")
