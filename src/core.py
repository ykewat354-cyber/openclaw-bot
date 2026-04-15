import os, requests
class OpenClawCore:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
    def chat(self, text):
        try:
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            payload = {"model": "google/gemini-flash-1.5-free", "messages": [{"role": "user", "content": text}]}
            r = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            return r.json()['choices'][0]['message']['content']
        except Exception as e: return f"Error: {e}"
