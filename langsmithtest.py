import os
from langsmith import traceable
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools.wikipedia.tool import WikipediaQueryRun

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "soham_api"
@traceable(name="soham_api")
def run_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

    wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    wiki_tool = Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Useful for answering factual questions using Wikipedia."
    )

    agent = initialize_agent(
        tools=[wiki_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent.run("Tell me something interesting about Alan Turing.")

run_agent()
