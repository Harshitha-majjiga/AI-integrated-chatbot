import google.generativeai as genai

# Configure the SDK with your Gemini API key
genai.configure(api_key="YOUR_API_KEY_HERE")

# Function to send user input + chat history to the AI model
def ask_ai(user_input, chat_history):
    # Create model instance
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Prepare conversation history
    messages = []
    for role, text in chat_history:
        messages.append(f"{role}: {text}")
    messages.append(f"user: {user_input}")

    # Send conversation to Gemini
    response = model.generate_content("\n".join(messages))

    return response.text


# Main program entry point
if __name__ == "__main__":
    print("🚀 Education Guidance ChatBot by FIXITY EDX is running! Type 'quit' or 'exit' to stop.")

    chat_history = []  # Store past conversations

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break

        try:
            # Get AI reply
            bot_reply = ask_ai(user_input, chat_history)

            # Print bot reply
            print(f"Bot: {bot_reply}")

            # Save conversation
            chat_history.append(("user", user_input))
            chat_history.append(("bot", bot_reply))

        except Exception as e:
            print(f"⚠️ Error: {e}")
