"""Módulo que gerencia as configurações de ambiente, autenticação GCP e parâmetros globais do projeto."""
import os
import logging
import sys
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente do sistema
load_dotenv()

# Configuração de Logging
def setup_logging():
    """Configura o logging global para emitir mensagens no stderr, preservando o transporte stdio do MCP."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
        force=True
    )
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(line_buffering=True)

# Inicializamos o logging imediatamente ao carregar as configurações
setup_logging()

def get_logger(name: str):
    """Retorna uma instância de logger configurada para o módulo específico."""
    return logging.getLogger(name)