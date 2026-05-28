import os
from groq import Groq

# It is highly recommended to set your API key as an environment variable,
# but for a quick test, you can replace os.environ.get(...) with "your_api_key_here"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# You can update this later when you want to enforce a specific theme
system_prompt = "You are a helpful and concise AI assistant."

chat_history = [
    {"role": "system", "content": system_prompt}
]

print("Groq Chatbot Initialized. Type 'quit' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['quit', 'exit']:
        print("Shutting down chatbot...")
        break

    # Add the user's message to the history
    chat_history.append({"role": "user", "content": user_input})

    try:
        # Call the Groq API
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", # You can change this to mixtral-8x7b-32768 or others
            messages=chat_history,
            temperature=0.7,
            max_tokens=1024,
        )

        # Extract and print the response
        bot_response = completion.choices[0].message.content
        print(f"Bot: {bot_response}")

        # Add the bot's response to the history so it remembers the conversation
        chat_history.append({"role": "assistant", "content": bot_response})

    except Exception as e:
        print(f"An error occurred: {e}")
