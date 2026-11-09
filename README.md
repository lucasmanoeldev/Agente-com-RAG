# Agente com RAG

Agente de consulta ao PDF `data/smc.pdf` com Agno, Groq e ChromaDB. Uma API baseada no AgentOS atende a interface de chat em Streamlit.

## Estrutura

| Caminho | Responsabilidade |
|---|---|
| `backend/api_agent.py` | Agente, base de conhecimento e API |
| `frontend/app.py` | Chat Streamlit |
| `data/smc.pdf` | Documento usado como fonte |
| `api_agent.py` | Entrada compatível da API |
| `servido_tela.py` | Entrada compatível do Streamlit |
| `tmp/` | ChromaDB e SQLite gerados localmente |
| `pyproject.toml` / `uv.lock` | Dependências |

## Configuração

Requer Python 3.13+ conforme `pyproject.toml`.

```bash
git clone https://github.com/lucasmanoeldev/Agente-com-RAG.git
cd Agente-com-RAG
uv sync
```

Copie `.env.example` para `.env` e preencha `GROQ_KEY_API`. A variável mantém o nome já usado pelo projeto. `RAG_API_URL` define a API consumida pela interface; o padrão local é `http://localhost:10000`.

## Execução

Na raiz, inicie a API:

```bash
uv run python api_agent.py
```

Em outro terminal, inicie a interface:

```bash
uv run streamlit run servido_tela.py
```

O script da API indexa o documento antes de iniciar o servidor na porta 10000. O primeiro processamento pode baixar modelos e utilizar a API externa. Os dados locais continuam em `tmp/`.

Para consumir uma API hospedada, configure `RAG_API_URL` com a URL correspondente. Iniciar apenas o objeto ASGI não executa a indexação feita pelo bloco principal do script.

## Limites

As respostas dependem do documento, da recuperação e do modelo. O projeto é um exemplo de RAG; a execução completa requer credencial e serviços externos. Não há suíte de testes automatizados no repositório.
