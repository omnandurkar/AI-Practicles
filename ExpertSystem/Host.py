# Implement any one of the following Expert System
# I. Information management
# II. Hospitals and medical facilities
# III. Help desks management
# IV. Employee performance evaluation
# V. Stock market trading
# VI. Airline scheduling and cargo schedules


def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def get_age():
    print("Could you please tell me your age?")
    age = int(input())
    return age

def ask_symptoms():
    print("Do you have any of the following symptoms?")
    print("1. Fever")
    print("2. Cough")
    print("3. Headache")
    print("4. Sore throat")
    print("5. None of the above")
    answer = input("Enter the number corresponding to your symptom (1-5): ")
    return answer

def suggest_home_remedy(symptom):
    if symptom == '1':
        print("You can try drinking warm water and taking rest.")
    elif symptom == '2':
        print("You can try inhaling steam and avoiding cold drinks.")
    elif symptom == '3':
        print("You can try applying a cold compress to your forehead.")
    elif symptom == '4':
        print("You can try gargling with warm salt water.")
    else:
        print("Since you don't have any symptoms, here are some general tips: Stay hydrated, eat nutritious food, and get plenty of rest.")

def chatbot():
    greet("Hospital Bot", "2024")
    age = get_age()
    print(f"Great! You're {age} years old.")
    symptom_answer = ask_symptoms()
    suggest_home_remedy(symptom_answer)

    print("Are you feeling okay now? (yes/no)")
    response = input().lower()
    if response == 'no':
        print("Since the home remedy didn't work, I recommend consulting a doctor.")

chatbot()