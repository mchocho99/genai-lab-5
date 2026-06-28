from openai import OpenAI
from dotenv import load_dotenv
import os

url = "https://genai-ort.fastmcp.app"

load_dotenv()

token = os.getenv("MCP_API_KEY")

client = OpenAI()

resp = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "mcp",
            "server_label": "count_letters_server",
            "server_url": f"{url}/mcp/",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {token}"
            },
        },
    ],
    input="Count the letter 'a' in the string 'banana'",
)

print(resp.output_text)