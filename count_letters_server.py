from fastmcp import FastMCP

mcp = FastMCP("HelloServer")

@mcp.tool
def count_letter(text: str, letter: str) -> int:
    return text.count(letter)

if __name__ == "__main__":
    mcp.run()