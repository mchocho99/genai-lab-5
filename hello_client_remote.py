import asyncio
import os
from dotenv import load_dotenv
from fastmcp import Client

load_dotenv()

async def main():
    client = Client(
        "https://genai-ort.fastmcp.app/mcp",
        auth=os.getenv("MCP_API_KEY"),
    )
    async with client:
        result = await client.call_tool("say_hello", {"name": "Remote"})
        print(result.data)

asyncio.run(main())