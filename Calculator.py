x = int(input('Enter the first number'))
y = int(input('Enter the second number'))
op = input('Enter the operation you want to perform')

op = op[:3].upper()

match op:
    case 'ADD':
        print(x+y)
    case 'SUB':
        print(x-y)
    case 'MUL':
        print(x*y)
    case 'DIV':
        print(x/y)
    case 'FLO':
        print(x//y)
    case 'MOD':
        print(x%y)
