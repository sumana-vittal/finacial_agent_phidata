from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information ",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

fianancial_agent = Agent(
    name="Financial AI Agent",
    role="Provide financial information and analysis",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), YFinanceTools(company_news=True)],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

multi_agent = Agent(
    team=[websearch_agent, fianancial_agent],
    instructions=["Always include sources","use table to display data"],
    show_tools_calls=True,
    markdown=True,
)

multi_agent.print_response("Summarize analyst recommendations and latest news for NVDA ", stream=True)