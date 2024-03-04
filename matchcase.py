def calculator(operator, num1, num2):
    match operator:
        case "+":
            result = num1 + num2
            print(f"{num1} - {num2} = {result}")
        case "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero!")
        case "%" :
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        case _:
            print("Invalid operator")

calculator("+",4,4 )
calculator("-",34,53)
calculator("*",50,55)
calculator("/",11,0)
calculator("%",18,6)