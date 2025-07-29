import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

import sys

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if len(sys.argv) <= 1:
        sys.exit(1)
    else:
        contents = sys.argv[1]
        user_prompt = contents
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        if '--verbose' in sys.argv:
            print (f'User prompt: {user_prompt}')
            print(response.text)
            response_object = response.usage_metadata
            print(f'Prompt tokens: {response_object.prompt_token_count}')
            print(f'Response tokens: {response_object.candidates_token_count}')
        else:
            print(response.text)
        

if __name__ == "__main__":
    main()
