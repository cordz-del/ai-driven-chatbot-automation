def generate_response(user_input):
    # Placeholder for an AI response, could integrate an LLM API here.
    return f"Echoing: {user_input}"

def main():
    print("Chatbot is online. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
