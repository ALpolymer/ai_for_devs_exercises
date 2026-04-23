from utils import ask
from utils import create_pctf_prompt




my_persona = "You are an expert in machine learning and LLM's.You can break down and explain complex concepts with clarity and simplicity to non-technical stakeholders"

my_context = "We are a company that tries to persuade our investors for the positive potential of using AI and LLM's in various sectors of our production"

my_task = "Describe without technical jargon to our investors who are not technical persons the builiding blocks and mechanisms of LLM's"

my_format = "Reply with  a numbered list of these mechanisms with the corresponding explanation below.Use Markdown"


system_prompt, user_prompt = create_pctf_prompt(
    persona= my_persona,
    context= my_context,
    task= my_task,
    format= my_format
)

response = ask(prompt=user_prompt, system=system_prompt, max_tokens=600)

print(response)
