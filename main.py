import asyncio
import os

from dotenv import load_dotenv
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
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
