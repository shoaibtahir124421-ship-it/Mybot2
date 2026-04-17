import requestsAIzaSyDYrxCfGZ1wYj6Ym6Q8abBqcgFhVsqMsP4AIzaSyDYrxCfGZ1wYj6Ym6Q8abBqcgFhVsqMsP4

import os
from rich import print

API_KEY = "YOUR_OPENAI_API_KEY"

def chat_with_ai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a smart autonomous AI agent."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return response.text


def search_web(query):
    print("[yellow]Searching internet...[/yellow]")
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    res = requests.get(url).json()
    return res.get("AbstractText", "No result found")


def run_agent():
    print("[green]🤖 Custom AI Agent Started![/green]")
    
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        if user_input.startswith("search"):
            query = user_input.replace("search", "")
            result = search_web(query)
            print(f"[cyan]Result:[/cyan] {result}")
        else:
            reply = chat_with_ai(user_input)
            print(f"[magenta]AI:[/magenta] {reply}")


if __name__ == "__main__":
    run_agent()
