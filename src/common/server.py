"""Módulo que centraliza a inicialização da instância FastMCP para garantir o Singleton em todo o projeto."""
from fastmcp import FastMCP
from src.common.config import get_logger

logger = get_logger("mcp-server")

logger.info("Inicializando instância Singleton do FastMCP...")
mcp = FastMCP("MCP-luan-server")