import asyncio
from fastmcp import Client

async def main():
    client = Client("hello_server.py")
    async with client:
        result = await client.call_tool("say_hello", {"name": "Martin"})
        print(result.data)

asyncio.run(main())
