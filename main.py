from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_community.llms.fake import FakeListLLM

# Fake LLM (no API key needed)
llm = FakeListLLM(responses=[
    "Hello! I am a basic LangChain agent.",
    "LangChain is a framework for building LLM-powered applications."
])

prompt = PromptTemplate.from_template(
    "Answer the following question clearly:\n{question}"
)

# Chain logic
chain = prompt | llm | RunnableLambda(lambda x: x)

# Console interface
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Agent: Goodbye 👋")
        break

    result = chain.invoke({"question": user_input})
    print("Agent:", result)
    #test change