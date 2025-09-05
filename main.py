import asyncio
import os
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
# print(os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI()  # whichever model

stdio_server_parameters = StdioServerParameters(
    command="python",
    args=["/Users/blauerbock/workspaces/mcp/mcp-crash-course/servers/math_server.py"],
    # math server
)

async def main():
    async with stdio_client(stdio_server_parameters) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            # tools = await session.list_tools()  # tools is an mcp object
            tools = await load_mcp_tools(session)
            # print(type(tools))
            # for tool in tools:
            #     pprint(tool, indent=2, depth=9, width=90)

            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({"messages": [HumanMessage("What is 54 + 2 * 3?")]})
            print(result["messages"][-1].content)

    # print("Hello from mcp-crash-course!")

if __name__ == "__main__":
    asyncio.run(main())
