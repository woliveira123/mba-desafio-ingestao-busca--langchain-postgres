# Ingestão e Busca Semântica com LangChain e Postgres

Solução para o desafio técnico do MBA IA da Full Cycle. Lê um PDF, armazena seus chunks como vetores no PostgreSQL com pgVector e permite consultas em linguagem natural via CLI, respondendo com base exclusivamente no conteúdo do documento.

## Tecnologias

- Python + LangChain
- PostgreSQL + pgVector (Docker)
- OpenAI: `text-embedding-3-small` (embeddings) e `gpt-5-nano` (LLM)

## Estrutura

```
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── document.pdf
└── src/
    ├── ingest.py   # ingere o PDF no banco
    ├── search.py   # busca semântica + chamada ao LLM
    └── chat.py     # CLI de interação com o usuário
```

## Pré-requisitos

- Python 3.10+
- Docker e Docker Compose
- Chave de API da OpenAI

## Configuração

**1. Clone o repositório e entre na pasta:**

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

**2. Crie e ative o ambiente virtual:**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente:**

```bash
cp .env.example .env
```

Edite o arquivo `.env` e preencha sua `OPENAI_API_KEY` e o caminho do PDF em `PDF_PATH`.

## Execução

**1. Suba o banco de dados:**

```bash
docker compose up -d
```

**2. Execute a ingestão do PDF:**

```bash
python src/ingest.py
```

**3. Inicie o chat:**

```bash
python src/chat.py
```

## Exemplo de uso

```
Faça sua pergunta:

PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

---

PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

Digite `sair` para encerrar o chat.
