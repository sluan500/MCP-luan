## 🚀 Como Iniciar

### 1. Instalar Dependências
```bash
uv sync
```
### 2. Configurar Política de Execução (Windows)
Caso o PowerShell bloqueie a execução de scripts:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
## 🔍 Testes e Diagnóstico (MCP Inspector)
O **Inspector** permite testar as ferramentas manualmente através de uma interface web.
### Como rodar o Inspector:
```bash
uv run fastmcp dev src/main.py
```
### Como utilizar:
1. O comando abrirá uma interface no navegador.
2. Na aba **"Tools"**, você verá ferramentas como `teste_conexao` e `predict_job_cost`.
3. Preencha os argumentos necessários e clique em **"Run Tool"** para validar a resposta JSON do servidor.