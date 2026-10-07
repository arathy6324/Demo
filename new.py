name = "Alice"
print("Hello, " + name + "!")
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        number = int(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("That's not a valid number. Please try again.")