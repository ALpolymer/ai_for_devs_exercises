from utils import ask
from utils import prompt_eval


test_questions = [
        "Explain API's",
        "Explain what an API is and give an example",
        "You are a software architect.Explain what an API is to non-technical business stakeholders. Use a real-world analogy and provide one practical example from web.development. Structure your answer in bullet points."
    ]

criteria = (
        "1. Σαφήνεια (Clarity)\n"
        "2. Πλαίσιο (Context)\n"
        "3. Καθορισμός ρόλου (Persona)\n"
        "4. Ποιότητα αναμενόμενης εξόδου (Expected output quality)\n"
        "5. Μορφοποίηση (Format)"
    )


for i, prompt in enumerate(test_questions, 1):
    print(f"\n{'-'*80}")
    print(f"Αξιολόγηση Prompt {i}:\n{prompt}")
    print(f"{'-'*80}")


    print("Generating response...")
    llm_response = ask(prompt=prompt, max_tokens=1000)

    print(f"\n{'-'*80}")
    print(f"Απάντηση LLM:\n{llm_response}")
    print(f"{'-'*80}")


    print("Evaluating prompt quality based on criteria...\n")
    evaluation = prompt_eval(
        question= prompt,
        response= llm_response,
        criteria= criteria,
        eval_provider = "anthropic",
        eval_model= "claude-sonnet-4-6"
    )

    print("ΑΠΟΤΕΛΕΣΜΑ ΑΞΙΟΛΟΓΗΣΗΣ:\n")
    print(evaluation)

