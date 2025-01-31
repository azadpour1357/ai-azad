import openai

class GPT3Answer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_answer(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
