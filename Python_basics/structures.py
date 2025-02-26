def classify_number(number):
    """Classifies a number as even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:  
    try:
        user_input = int(input("Enter an integer: "))
        break  
    except ValueError:
        print("Invalid input. Please enter an integer.")

classification = classify_number(user_input)
print(f"The number {user_input} is {classification}.")

even_numbers = []
for i in range(2, 51, 2):  
    even_numbers.append(i)

print("\nEven numbers from 1 to 50:", even_numbers)
print("\nNumbers from 10 down to 1:")
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1

