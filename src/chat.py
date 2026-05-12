from search import search_prompt

def main():
    print("Faça sua pergunta:\n")

    while True:
        question = input("PERGUNTA: ").strip()

        if not question:
            continue
        if question.lower() == "sair":
            break

        search_prompt(question)

if __name__ == "__main__":
    main()
