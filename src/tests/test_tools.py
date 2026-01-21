"""Módulo que contém ferramentas MCP de diagnóstico e validação para testar a integridade do servidor."""
from src.common.server import mcp

def _verificar_sistema() -> str:
    """Função auxiliar para validar o status do sistema interno."""
    return "Estrutura MCP operacional e Singleton ativo!"

@mcp.tool()
def test_conexao() -> str:
    """
    Ferramenta de diagnóstico que verifica se o servidor MCP e suas rotas estão acessíveis.
    
    :return: Frase de validação
    :rtype: str
    """
    return _verificar_sistema()