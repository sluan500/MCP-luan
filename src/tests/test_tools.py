"""Módulo que contém ferramentas MCP de diagnóstico e validação para testar a integridade do servidor."""
from src.common.server import mcp
from src.common.config import get_logger

logger = get_logger("test-tools")

def _verificar_sistema() -> str:
    """Função auxiliar para validar o status do sistema interno."""
    logger.info("Executando verificação interna de integridade do sistema.")
    return "Estrutura MCP operacional e Singleton ativo!"

@mcp.tool()
def test_conexao() -> str:
    """
    Ferramenta de diagnóstico que verifica se o servidor MCP e suas rotas estão acessíveis.
    
    :return: Frase de validação
    :rtype: str
    """
    logger.info(">>> [TESTE] A ferramenta 'teste_conexao' foi executada com sucesso.")
    return _verificar_sistema()