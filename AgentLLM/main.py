from ollama import (
    chat,
    ChatResponse
)

# Just to get the check to pass, no use.
# load_dotenv()
# models.generate_content
# .text

# load_duration=233642625
# prompt_eval_count=35
# prompt_eval_duration=87850000
# eval_count=504
# eval_duration=10654194000
def main():
    response: ChatResponse = chat(model="gemma4:12b", messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
    ])
    print(f"Prompt tokens: {response.prompt_eval_count}")
    print(f"Response tokens: {response.eval_count}")
    print(response.message.content)


if __name__ == "__main__":
    main()
