import os

def calculator():
    available_operators = [ '+' , '-' , '*' , '/' , '^' ,'^2' ]
    while True:
        input()
        os.system("clear")
        print('''
           ____            _                  _              _
          / ___|  __ _.   | |   ___.  _   _  | |  __ _.   __| |__.   ___   ._ __
         | |     /  _  |  | |  / __| | | | | | | /  _  |  |_  ___|  / _ \\  | '__|
         | |___  | (_| |. | | ( (__. |_|_| | | | | (_| |.   | |__. | (_) | | |
          \\____\\  \\__,__| |_|  \\___|  \\__,_| |_|  \\__,__|   \\_____\\ \\___/  |_|
    
             ''')
        print("\n\n")
        print(f"Available operations: {available_operators}")

        print("Type 'exit' to quit\n")

        op = input(f"Enter operator {available_operators} : \n").strip()
        if op.lower() == 'exit':
            break

        if op == '^2':
            num = input("Enter a number to square: ")
            if num.lower() == 'exit':
                break
            try:
                num = float(num)
                result = num ** 2
                print(f"\nResult: {num}² = {result}\n")
            except ValueError:
                print("\nPlease enter a valid number.\n")
            continue  # Skip rest of loop and go to next input

        # For other operators: + - * /
        else:
            num1 = input("Enter first number: ")
            if num1.lower() == 'exit':
                break

            num2 = input("Enter second number: ")

            if num2.lower() == 'exit':
                break

            try:
                num1 = float(num1)
                num2 = float(num2)

                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        print("\nError: Division by zero.\n")
                        continue
                    result = num1 / num2
                elif op == '^':
                    result = num1 ** num2
                else:
                    print(f"\nInvalid operator. Use {available_operators}.\n")
                    continue

                print(f"\nResult: {num1} {op} {num2} = {result}\n")

            except ValueError:
                print("\nPlease enter valid numbers.\n")

    print("\nCalculator closed. Goodbye!")

if __name__ == "__main__":
    calculator()
