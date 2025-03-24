import os
import sys

from google import genai

from gemini_client import send_text_prompt, send_n_shot_prompt

# TODO: Get API key
# TODO: Hide API key, maybe make it a CLI param
# TODO: connect to Gemini API

if __name__ == '__main__':
    text_prompt = ""
    try:
        text_prompt = sys.argv[1]
    except IndexError:
        print("Text prompt was not supplied, quitting.")
        sys.exit(1)
    api_key = ""
    try:
        api_key = sys.argv[2]
    except IndexError:
        print("Defaulting to API key saved to environment.")
        api_key = os.environ.get("gcpTrainingApiKey")
        if api_key is None or api_key.strip() == '':
            print("No API key found in environment or command line arguments.")
            sys.exit(1)
    client = genai.Client(api_key=api_key)
    # Default to lite as the model
    model = "gemini-2.0-flash-lite"
    gemini_response_text = send_text_prompt(client, model, text_prompt)
    print(gemini_response_text)
    # Experiment with few-shot prompting
    n_shots = [
        dict(role="user", chat="Theme: Clay and Sea"),
        dict(role="model", chat="['#C7522A', '#E5C185', '#FBF2C4', '#74A892', '#008585']"),
        dict(role="user", chat="Theme: Pastel Vibes"),
        dict(role="model", chat="['#D6E6FF', '#D7F9F8', '#FFFFEA', '#FFF0D4', '#FBE0E0', '#E5D4EF']"),
        dict(role="user", chat="Theme: Moody Sunset"),
        dict(role="model", chat="['#003F5C', '#58508D', '#BC5090', '#FF6361', '#FFA600']"),
        dict(role="user", chat="Theme: Forest Breeze"),
        dict(role="model", chat="['#F1DDBF', '#525E75', '#78938A', '#92BA92']")
    ]
    palette_instructions = (
        "You are an experienced graphic designer. Please provide a list of hexadecimal colour codes for a "
        "particular theme in a JSON list. Do NOT include any comments or explanations for your choices, "
        "just a list like '[#hexCode1, #hexCode2, #hexCode3]'. ")
    gemini_response_text = send_n_shot_prompt(client, model, palette_instructions, n_shots, "Theme: Calsonic Skyline")
    print(gemini_response_text)
    # Chain-of-thought prompting examples
    text_prompt = ("In the 2024 Champions League final, Real Madrid extended their record of Champions League titles"
                   "to 15 after defeating Borussia Dortmund. How were they successful? Please explain step by "
                   "step.")
    gemini_response_text = send_text_prompt(client, model, text_prompt)
    print(gemini_response_text)
    text_prompt = ("In the 2024 Formula One season, Max Verstappen won a fourth drivers' championship in a row. How "
                   "was he successful? Please explain step by step.")
    gemini_response_text = send_text_prompt(client, model, text_prompt)
    print(gemini_response_text)
    text_prompt = "What is the best strategy of Fantasy Premier League? Please explain step by step."
    gemini_response_text = send_text_prompt(client, model, text_prompt)
    print(gemini_response_text)
