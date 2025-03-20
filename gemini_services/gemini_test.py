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
        print("Text prompt was not supplied, switching to default.")
        text_prompt = ("You are an experienced mechanic. I have bought a car, and the brake pedal goes soft when I "
                       "turn the ignition key. What are the likely causes of this?")
    api_key = ""
    try:
        api_key = sys.argv[2]
    except IndexError:
        print("Defaulting to API key saved to environment.")
        api_key = os.environ.get("gcpTrainingApiKey")
        if api_key.strip() == '':
            print("No API key found in environment or command line arguments.")
            sys.exit(1)
    gemini_response_text = send_text_prompt(api_key, text_prompt)
    print(gemini_response_text)
    # TODO: Experiment with zero-shot, few-shot and chain-of-thought prompting
