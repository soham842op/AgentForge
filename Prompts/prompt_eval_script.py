import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import WikipediaAPIWrapper

os.environ["GOOGLE_API_KEY"] = "AIzaSyDYov5wvm-1yV_fSWA7uk5qHczydoideTw"

# Load Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

# Sample prompts
prompts = [
    "Summarize this text in one paragraph.",
    "Give me a concise yet informative summary of the following article.",
    "Generate a professional summary of the given content focusing on major achievements."
]

# Get context to summarize
wiki = WikipediaAPIWrapper()
topic = "Cristiano Ronaldo"
article = wiki.run(topic)

results = []
for i, prompt in enumerate(prompts, start=1):
    full_prompt = f"{prompt}\n\n{article}"
    output = llm.invoke(full_prompt)
    results.append((prompt, output))

# Print outputs
for i, (prompt, output) in enumerate(results):
    print(f"\n--- Prompt {i+1} ---")
    print(f"Prompt:\n{prompt}")
    print(f"\nOutput:\n{output.content}")
