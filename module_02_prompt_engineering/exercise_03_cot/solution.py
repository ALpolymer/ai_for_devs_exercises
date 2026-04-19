from utils import ask


no_cot_prompt = """Find the result of the function below and answer ONLY with the result:

```python
    def process_numbers(nums):
        result = []
        for n in nums:
            if n%2 == 0:
                result.append(n*2)
            else:
                result.append(n+3)
        return sum(result)
```
input: nums=[1, 2, 3, 4]
output:
"""

no_cot_result = ask(prompt= no_cot_prompt, temperature=0)

cot_prompt = """Find the result of the function below and trace through the code STEP BY STEP:

```python
    def process_numbers(nums):
        result = []
        for n in nums:
            if n%2 == 0:
                result.append(n*2)
            else:
                result.append(n+3)
        return sum(result)
```
input: nums=[1, 2, 3, 4]
output:
"""

cot_result = ask(prompt= cot_prompt, temperature=0, max_tokens=1000)


print(f"No CoT result: {no_cot_result}")
print(f"CoT result: {cot_result}")