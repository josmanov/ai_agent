import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Api key not found!")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages
    )
    if not response.usage_metadata:
        raise RuntimeError("Response metadata not found.\nApi key potentially not found")
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if args.verbose == True:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(f"Response:\n{response.text}")

if __name__ == "__main__":
    main()
