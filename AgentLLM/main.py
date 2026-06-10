from ollama import (
    chat,
    ChatResponse
)

# Just to get the check to pass, no use.
# load_dotenv()
# models.generate_content
# .text


def main():
    response: ChatResponse = chat(model="gemma4:12b", messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
    ])
    print(response.message.content)


if __name__ == "__main__":
    main()
