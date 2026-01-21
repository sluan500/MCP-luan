"""Módulo de entrada do servidor MCP que registra as ferramentas e inicia a execução via transporte STDIO."""
from src.common.server import mcp
import src.tests.test_tools

if __name__ == "__main__":
     # O FastMCP gerencia o transporte (stdio por padrão)
    mcp.run()