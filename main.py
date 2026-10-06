from calculator import calculate
from history import save,load

print("Welcome To CalcX")
data = load()
while True:
    try:
        text = input("calc> ")
    except (KeyboardInterrupt, EOFError):
        print()
        print("Bye")
        break
    if text == "quit":
        break
    elif text == "history":
        for n in data:
            print(f"{n}:{data.get(n)}")
			continue

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
        data[text]=result
        save(data)
