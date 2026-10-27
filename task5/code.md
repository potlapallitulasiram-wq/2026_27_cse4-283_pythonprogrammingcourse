## Problem statement

Create a Python program that checks each sample password against these rules:

- At least **12 characters** long.
- Contains at least one **uppercase letter**, **lowercase letter**, **digit**, and **special character**.
- Does not contain the same character **three or more times in a row**.
- Does not contain a prohibited substring: `password`, `admin`, or `qwerty` (case-insensitive).

The program must report every failed condition for each password.

## Algorithm

1. Read the number of passwords and then read each password.
2. For each password, check its length and whether it contains each required character category.
3. Find any run of three or more identical consecutive characters.
4. Search for prohibited substrings without considering letter case.
5. Report whether the password is valid. If it is invalid, list every failed condition.

## Python source code

```python
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
```

## Sample input

```text
4
Abc1!xyz
GoodPassword1!
AAAbcdef1!
Strong#River42
```

## Sample output

```text
Password 1: INVALID
  - Length is 8; minimum required is 12.
Password 2: INVALID
  - Contains prohibited substring 'password'.
Password 3: INVALID
  - Length is 10; minimum required is 12.
  - Character 'A' repeats 3 or more times in a row.
Password 4: VALID
```

## Mermaid flowchart code

```mermaid
flowchart TD
    A([Start]) --> B[/Read number of passwords/]
    B --> C[/Read a password/]
    C --> D[Create empty list of failures]
    D --> E{Length at least 12?}
    E -- No --> E1[Add length failure]
    E -- Yes --> F{Has uppercase, lowercase, digit, and special character?}
    E1 --> F
    F -- No --> F1[Add missing category failures]
    F -- Yes --> G{Has 3 identical consecutive characters?}
    F1 --> G
    G -- Yes --> G1[Add repetition failure]
    G -- No --> H{Contains prohibited substring?}
    G1 --> H
    H -- Yes --> H1[Add prohibited substring failure]
    H -- No --> I{Any failures?}
    H1 --> I
    I -- Yes --> J[Print INVALID and explain failures]
    I -- No --> K[Print VALID]
    J --> L{More passwords?}
    K --> L
    L -- Yes --> C
    L -- No --> M([End])
```
