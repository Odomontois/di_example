def ask_age(max_attempts=10):
    for _attempt in range(max_attempts):
        try:
            return int(input("Enter your age: "))
        except ValueError as err:
            print(err, "try again")
    raise ValueError("too many tries, exiting")


def ask_name():
    return input("Enter your name: ")


def ask_sex(max_attempts=10):
    for _attempt in range(max_attempts):
        try:
            inp = input("Enter your sex (M[ale], F[emale]): ")
            if inp.lower() in("m", "male"):
                return "male"
            elif inp.lower() in("f", "female"):
                return "female"
            else:
                raise ValueError("undefined answer")
        except ValueError as err:
            print(err, "try again")
    raise ValueError("too many tries, exiting")
