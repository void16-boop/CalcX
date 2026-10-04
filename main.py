from calculator import calculate

print("Welcome To CalcX")

while True:
    try:
        text = input("calc> ")
    except (KeyboardInterrupt, EOFError):
        print()
        print("Bye")
        break
    if text == "quit":
        break

    try:
        result = calculate(text)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("Check Your Arithmetic and Try again")
    else:
        if result == int(result):
            result = int(result)
        print(result)
