#Age group project

user_age = int(input("Enter your age: "))

while user_age < 1:
    print("Please enter a real age.")
    user_age = int(input("Enter your age again: "))
print(f"Thank you! Your age ({user_age}) is accepted.")

if user_age < 18:
    print("You are a Child.")
elif user_age >= 18 and user_age < 60:
    print("You are an Adult.")
elif user_age >= 60 and user_age < 100:
    print("You are a Senior Citizen.")
else:
    print("You are a Bollywood Hero!")
