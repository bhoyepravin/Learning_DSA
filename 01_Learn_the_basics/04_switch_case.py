# Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

# Ensure only the 1st letter of the answer is capitalised.

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("sunday")
            case _: 
                print("Invalid")

day = int(input("Enter day Number:"))
solution = Solution()

solution.whichWeekDay(day)