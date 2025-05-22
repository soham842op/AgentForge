import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()


# Set your Gemini API key
# You can get a free API key from https://ai.google.dev/
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# List available models to find the correct name
print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")

# Use the gemini-1.5-flash model which is widely available
llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

# Define tools using community imports
search = DuckDuckGoSearchRun()
wikipedia = WikipediaAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for searching the web for current information"
    ),
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for getting detailed information on topics, people, places, history, etc."
    )
]

# Set up memory with the updated approach
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent with invoke method instead of run
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True
)

# Example usage using invoke instead of run
def chat_with_agent(query):
    try:
        response = agent.invoke({"input": query})
        return response.get("output", "No response generated")
    except Exception as e:
        return f"Error: {str(e)}"

# Example conversation
if __name__ == "__main__":
    print("Agent is ready! Type 'exit' to quit.")
    print(chat_with_agent("Hello, who are you?"))
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_agent(user_input)
        print(f"Agent: {response}")



