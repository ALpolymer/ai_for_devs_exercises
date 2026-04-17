from utils import ask

my_querie = "Find all customers from Athens"

system = """You are an experienced SQL engineer
You are an expert on writing SQL queries following the best SQL queries practices
"""
my_prompt = """Translate natural language queries to SQL queries.

Input: "Find all customers"
Output: "SELECT * FROM customers;“

Input: "Find all products with price above 100"
Output: "SELECT * FROM products WHERE price > 100;"

Input: {my_querie}
Output:
"""

response = ask(prompt=my_prompt.format(my_querie= my_querie), system=system, temperature=0)

print(f"Natural language querie: {my_querie} \n\nSQL querie: {response}")
