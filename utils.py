import os
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask(prompt, system=None, temperature=0.7, max_tokens=200, provider="openai", model=None):
    """
    Στέλνει ένα prompt στο επιλεγμένο LLM (OpenAI ή Anthropic) και επιστρέφει την απάντηση.
    """
    
    # ------------------ OPENAI ------------------
    if provider.lower() == "openai":
        actual_model = model or "gpt-4o-mini" 
        
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": prompt})
        
        kwargs = {
            "model": actual_model,
            "messages": msgs,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        r = openai_client.chat.completions.create(**kwargs)
        return r.choices[0].message.content

    # ----------------- ANTHROPIC -----------------
    elif provider.lower() == "anthropic":
        actual_model = model or "claude-haiku-4-5-20251001"
        
        msgs = [{"role": "user", "content": prompt}]
        
        kwargs = {
            "model": actual_model,
            "messages": msgs,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        if system:
            kwargs["system"] = system
            
        r = anthropic_client.messages.create(**kwargs)
        return r.content[0].text

    else:
        raise ValueError("Μη υποστηριζόμενος provider. Επίλεξε 'openai' ή 'anthropic'.")
    