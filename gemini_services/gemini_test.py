import requests
import sys

# TODO: Get API key
# TODO: Hide API key, maybe make it a CLI param
# TODO: connect to Gemini API

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Hello there.")
    else:
        print("You thought I was going to print an API key, weren't you?")
