from langchain.agents import AgentExecutor, create_react_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from tools.web_search import web_search
from tools.calculator import calculate
from tools.database import database_query

# Define tools
tools = [
    {"name": "Web Search", "func": web_search, "description": "Search the web for up-to-date information"},
    {"name": "Calculator", "func": calculate, "description": "Perform mathematical calculations"},
    {"name": "Database", "func": database_query, "description": "Query the SQL database"}
]

# Initialize LLM (replace with your API key)
llm = OpenAI(model_name="text-davinci-003", openai_api_key="your_openai_api_key")

# ReAct prompt template
react_prompt = PromptTemplate(
    input_variables=["input", "tools"],
    template="Answer the following question using the provided tools if necessary: {input}\nAvailable tools: {tools}"
)

# Create ReAct agent
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def reasoner(query):
    return executor.run(input=query, tools=[t["name"] for t in tools])