from user import User
from processing import preprocess_image
from prediction import analyze_oral_health
from storage import save_data, load_data
from recommendation import get_recommendation
from report import print_report
from utils import ask_input, line

def main():
    print("WELCOME TO ORAL HEALTH ANALYZER")

    data = load_data()
    if data:
        print("Previous user detected. Loading profile...")
        user = User(data["name"], data["age"])
        user.history = data["history"]
    else:
        name, age, _ = ask_input()
        user = User(name, age)

    line()
    print("1. Analyze New Image")
    print("2. Show Previous Records")
    print("3. Save & Exit")
    line()

    while True:
        choice = input("Choose option: ")

        if choice == "1":
            _, _, img_path = ask_input()

processed = preprocess_image(img_path)
            analysis = analyze_oral_health(processed)
            analysis["recommendation"] = get_recommendation(analysis["issue"])

            user.add_record(analysis)
            print_report(user, analysis)

        elif choice == "2":
            print("\nYour past analysis reports:")
            for rec in user.get_history():
                print(rec)

        elif choice == "3":
            save_data(user)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option.")

if _name_ == "_main_":
