from google import genai
import requests


def send_text_prompt(api_key: str, prompt_text: str) -> str:
    # TODO: implement sending text prompt to Gemini API
    # You can use the provided endpoint and request method as a reference
    client = genai.Client(api_key=api_key)
    print(f"Sending prompt {prompt_text} to Gemini")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_text
    )
    return response.text
