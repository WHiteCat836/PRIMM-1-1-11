"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""
#makes the code start here every time. 
def main():
  #asks the user for a number and stores the number as an integer in the variable "num1".
    num1: float = input("Enter a number: ")
    num1 = float(num1)
  #asks the user for a second number and stores the number as an integer in the variable "num2".
    num2: float = float(input("Enter another number: "))
  #adds the integers num1 and num2 and stores the answer as an integer in variable "total".
    total: float = num1+num2
    print(total)
#prints the entire mathmetic operation of adding "num1" and "num2" and prints the variable "total" as the answer. 
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {num1-num2}")
    print(f"{num1} * {num2} = {num1*num2}")
    print(f"{num1} ** {num2} = {num1**num2}")
    print(f"{num1} / {num2} = {num1/num2}")
    #The number of times num1 goes into num2
    print(f"{num1} // {num2} = {num1//num2}")
    #Gives the remainer of the long division of the two numbers.
    print(f"{num1} % {num2} = {num1%num2}")
"""
The comments above each major line of code can be much smaller and less specific. It should say the general action the chunck is doing. 
"""
if __name__ == "__main__":
  main()
