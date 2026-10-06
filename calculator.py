from operator import sub

OPERATORS = ["+", "*", "/", "-"]


def split_into_tokens(text):
    text = text.replace(" ", "")
    tokens = []
    number = ""

    for character in text:
        if character.isdigit() or character == ".":
            number = number + character
        elif character in OPERATORS:
            if number == "":
                if character == "-" or character == "+":
                    number = character
                else:
                    raise ValueError("Bad expression")
            else:
                tokens.append(number)
                tokens.append(character)
                number = ""
        else:
            raise ValueError("Bad character")

    if number != "":
        tokens.append(number)

    return tokens


def calculate(text):
    tokens = split_into_tokens(text)

    if len(tokens) == 0 or len(tokens) % 2 == 0:
        raise ValueError("Bad expression")

    current = float(tokens[0])
    terms = []
    signs = []

    position = 1
    while position < len(tokens):
        sign = tokens[position]
        number = float(tokens[position + 1])

        if sign == "*":
            current = current * number
        elif sign == "/":
            if number == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            current = current / number
        else:
            terms.append(current)
            signs.append(sign)
            current = number

        position = position + 2

    terms.append(current)

    total = terms[0]
    for index in range(len(signs)):
        if signs[index] == "+":
            total = total + terms[index + 1]
        else:
            total = sub(total, terms[index + 1])

    return total
