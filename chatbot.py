import openai

def chatbot():
    openai.api_key = "SUA_CHAVE_API"  # Substitua pela sua chave da OpenAI
    
    print("Chatbot: Olá! Digite sua pergunta ou 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Até mais!")
            break
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        
        bot_reply = response["choices"][0]["message"]["content"]
        print(f"Chatbot: {bot_reply}")

if __name__ == "__main__":
    chatbot()
