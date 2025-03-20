import os
import sys

from gemini_client import send_text_prompt

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
    gemini_response_text = send_text_prompt(api_key, text_prompt)
    print(gemini_response_text)
    # Experiment with few-shot prompting
    text_prompt = ("You are an experienced graphic designer. Please provide a list of hexadecimal colour codes for a "
                   "particular theme in a JSON list. Do NOT include any comments or explanations for your choices, "
                   "just a list like '[#hexCode1, #hexCode2, #hexCode3]'. "
                   "Your responses must follow the following format:\n"
                   "Theme: Clay and Sea\n"
                   "['#C7522A', '#E5C185', '#FBF2C4', '#74A892', '#008585']\n"
                   "Theme: Pastel Vibes\n"
                   "['#D6E6FF', '#D7F9F8', '#FFFFEA', '#FFF0D4', '#FBE0E0', '#E5D4EF']\n"
                   "Theme: Moody Sunset\n"
                   "['#003F5C', '#58508D', '#BC5090', '#FF6361', '#FFA600']\n"
                   "Theme: Forest Breeze\n"
                   "['#F1DDBF', '#525E75', '#78938A', '#92BA92']\n"
                   "Theme: Calsonic Skyline\n")
    gemini_response_text = send_text_prompt(api_key, text_prompt)
    print(gemini_response_text)
    # TODO: chain-of-thought prompting
