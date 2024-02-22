num1 = 5
num2 = 1
operation = 'Division'

match operation:
    case 'Addition':
        result = num1 + num2
        print(result)
    case 'Subtraction':
        result = num1 - num2
        print(result)
    case 'Multiplication':
        result = num1 * num2
        print(result)
    case 'Division':
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            print("num2 can't be Zero!")
    case 'Module':
        result = num1 % num2
        print(result)
