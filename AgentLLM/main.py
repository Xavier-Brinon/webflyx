from functions.call_function import available_functions
from prompts import system_prompt
from ollama import (
    chat,
    ChatResponse,
    Message
)
import argparse

# Just to get the check to pass, no use.
# load_dotenv()
# models.generate_content
# .text
# parts=[

# load_duration=233642625
# prompt_eval_count=35
# prompt_eval_duration=87850000
# eval_count=504
# eval_duration=10654194000
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()  # Now we have access to args.user_prompt.

    messages: list[Message] = [
        Message(role="system", content=system_prompt),
        Message(role="user", content=args.user_prompt)
    ]

    response: ChatResponse = chat(model="gemma4:12b", messages=messages, tools=available_functions)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.prompt_eval_count}")
        print(f"Response tokens: {response.eval_count}")

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            print(f"Calling function: {tool_call.function.name}({dict(tool_call.function.arguments)})")
    else:
        print(response.message.content)


if __name__ == "__main__":
    main()
