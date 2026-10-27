MIN_LENGTH = 12
PROHIBITED_SUBSTRINGS = ("password", "admin", "qwerty")


def evaluate_password(password):
    failures = []

    if len(password) < MIN_LENGTH:
        failures.append(
            f"Length is {len(password)}; minimum required is {MIN_LENGTH}."
        )

    if not any(char.isupper() for char in password):
        failures.append("Missing an uppercase letter.")

    if not any(char.islower() for char in password):
        failures.append("Missing a lowercase letter.")

    if not any(char.isdigit() for char in password):
        failures.append("Missing a digit.")

    if not any(not char.isalnum() for char in password):
        failures.append("Missing a special character.")

    for index in range(len(password) - 2):
        if password[index] == password[index + 1] == password[index + 2]:
            failures.append(
                f"Character '{password[index]}' repeats 3 or more times in a row."
            )
            break

    lower_password = password.lower()
    for substring in PROHIBITED_SUBSTRINGS:
        if substring in lower_password:
            failures.append(f"Contains prohibited substring '{substring}'.")
            break

    return failures


def main():
    try:
        count = int(input("Number of passwords: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for number in range(1, count + 1):
        password = input(f"Password {number}: ")
        failures = evaluate_password(password)

        if failures:
            print(f"Password {number}: INVALID")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print(f"Password {number}: VALID")


if __name__ == "__main__":
    main()
