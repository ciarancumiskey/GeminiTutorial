from google import genai
from google.genai import client, types

from models.basic_prompt_model import ChatMessage, ChatRole


def send_text_prompt(gemini_client: client, model: str, prompt_text: str) -> str:
    print(f"Sending prompt \"{prompt_text}\" to Gemini")

    response = gemini_client.models.generate_content(
        model=model,
        contents=prompt_text
    )
    return response.text


def send_n_shot_prompt(gemini_client: client, model: str, system_instructions: str, chat_history: list[ChatMessage],
                       new_user_message: str) -> str:
    print("Sending N-shot prompts to Gemini.")

    contents = []
    for sample_chat in chat_history:
        contents.append(genai.types.Content(
            parts=[{'text': sample_chat.content}],
            role=sample_chat.role.value
        ))
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        system_instruction=system_instructions
    )

    new_chat = gemini_client.chats.create(
        model=model,
        config=generate_content_config,
        history=contents)
    response = new_chat.send_message(new_user_message)
    return response.text


def ask_close_ended_question(gemini_client: client, model: str, new_user_message: str) -> str:
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        system_instruction="You may ONLY answer 'Yes' or 'No' to ANYTHING the client asks."
    )
    new_chat = gemini_client.chats.create(
        model=model,
        config=generate_content_config)
    response = new_chat.send_message(new_user_message)
    return response.text
