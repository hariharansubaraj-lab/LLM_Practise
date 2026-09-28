import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the local Ollama LLM
    and return the generated response.
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]


if __name__ == "__main__":

    prompt = "What is Artificial Intelligence?"

    answer = ask_llm(prompt)

    print("\nPrompt:")
    print(prompt)

    print("\nLLM Response:")
    print(answer)