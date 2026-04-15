def hybrid_chat(agent, text):
    if any(x in text.lower() for x in ["hi", "hello", "hey", "namaste"]):
        return "Aur bhai! OpenClaw-Bot ready hai. Bol kya kaam hai? ⚡"
    return agent.chat(text)
