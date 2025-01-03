def answer_question(question):
    # Basic rules for common questions
    question = question.lower()
    if "your name" in question:
        return "I am your basic AI assistant!"
    elif "time" in question:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "weather" in question:
        return "I can't fetch live weather data yet, but you can check a weather app!"
    elif "capital of" in question:
        # Simple lookup for capitals
        capitals = {
            "france": "Paris",
            "japan": "Tokyo",
            "india": "New Delhi",
            "usa": "Washington, D.C."
        }
        for country, capital in capitals.items():
            if country in question:
                return f"The capital of {country.capitalize()} is {capital}."
        return "I don't know the capital of that country yet."
    else:
        return "I'm sorry, I can't answer that question right now."

def main():
    print("Welcome to Real-Life Question Answering AI!")
    print("Type 'exit' to quit.")
    while True:
        # Take user input
        user_input = input("Ask me a question: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Respond to the question
        print(answer_question(user_input))

if __name__ == "__main__":
    main()
