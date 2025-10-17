from mcp.server.fastmcp import FastMCP

mcp = FastMCP('captcha server')

@mcp.tool(description='tool')
def print_hello():
    return "hello"

if __name__ == '__main__':
    mcp.run(transport='sse')