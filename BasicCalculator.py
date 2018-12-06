def Help():
    print('Calculator')
    print()
    print('Plus: Adds two numbers.')
    print('Minus: Subtracts two numbers.')
    print('Multi: Multiplies two numbers.')
    print('Div: Divides two numbers')
    print('Square: Square Root.')
    print('Help: Display this help screen')
    print('Exit: Exits the program.')

def mainMenu():
    print('P-Plus\nR-Minus\nM-Multiplication\nD-Division\nS-Root\nH-Help\nE-Exit')

def Plus():
    a = int(input('Number a: '))
    b = int(input('NUmber b: '))
    result = a + b
    print(f'{a}' ' + ' f'{b}' ' = ' f'{result}')

def Minus():
    a = int(input('Number a: '))
    b = int(input('Number b: '))
    result = a - b
    print(f'{a}' ' - ' f'{b}' ' = ' f'{result}')

def Multi():
    a = int(input('Number a: '))
    b = int(input('Number b: '))
    result = a * b
    print(f'{a}' ' x ' f'{b}' ' = ' f'{result}')

def Div():
    a = int(input('Number a: '))
    b = int(input('Number b: '))
    result = a/b
    print(f'{a}' ' / ' f'{b}' ' = ' f'{result}')

def Root():
    a = int(input('Number a: '))
    b = int(input('Number b: '))
    root = (1/float(b))
    result = a**root
    print(f'{a}' ' ^ ' f'{root}' ' = ' f'{result}')

def main():
    Help()
    print()
    mainMenu()
    op = 'Y'
    while op == 'Y':
        print()
        Opt = input('Choose Your Destiny: ').upper()
        if Opt == 'P':
            Plus()
        elif Opt == 'R':
            Minus()
        elif Opt == 'M':
            Multi()
        elif Opt == 'D':
            Div()
        elif Opt == 'S':
            Root()
        elif Opt == 'H':
            Help()
        elif Opt == 'E':
            print('Turn Off.')
            break

        print()
        print('Do you want to try again? Y or N')
        op = input('Choose Your Option: ').upper()
        if op == 'N':
            print('Shutdown.')
            break
    else:
        print('Invalid Option')

main()
        