#code
from langchain_core.runnables import RunnableLambda
import re

print("🤖 Internship Agent Ready")
print("Type 'exit' to quit")

# Calculator + responder
def agent_logic(text):
    match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", text)
    if match:
        a, op, b = match.groups()
        a, b = int(a), int(b)
        if op == "+": return f"Result: {a + b}"
        if op == "-": return f"Result: {a - b}"
        if op == "*": return f"Result: {a * b}"
        if op == "/": return f"Result: {a / b}"
    return "I can answer simple questions or solve math like 4 + 5"

# LangChain runnable
chain = RunnableLambda(agent_logic)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Agent: Bye 👋")
        break
    print("Agent:", chain.invoke(user_input))
