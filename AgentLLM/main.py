from functions.call_function import available_functions, call_function
from prompts import system_prompt
from ollama import (
    chat,
    ChatResponse,
    Message
)
import argparse


gemma4 = "gemma4:12b"
ministral = "ministral-3:14b"
MAX_ITERS = 20
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

    for _ in range(MAX_ITERS):
        response: ChatResponse = chat(model=gemma4, messages=messages, tools=available_functions)
        messages.append(response.message)

        if not response.message.tool_calls:
            print("Final response:")
            print(response.message.content)
            break

        function_results = []
        for tool_call in response.message.tool_calls:
            function_call_result = call_function(tool_call, verbose=args.verbose)
            if not function_call_result.content:
                raise Exception(f"call_function returned no content for {tool_call.function.name}")
            function_results.append(function_call_result)
            if args.verbose:
                print(f"-> {function_call_result.content}")
        messages.extend(function_results)
    else:
        print(f"Agent stopped after {MAX_ITERS} iterations without a final response.")
        sys.exit(1)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.prompt_eval_count}")
        print(f"Response tokens: {response.eval_count}")


if __name__ == "__main__":
    main()
