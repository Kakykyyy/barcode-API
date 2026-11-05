<div align="center">

# Barcode API

**Cadastro de produtos por código de barras**

![Python](https://img.shields.io/badge/Python-20232a?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-20232a?style=flat-square) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-20232a?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-20232a?style=flat-square)

[Sobre](#sobre) · [Como executar](#como-executar) · [Documentação](DOCUMENTACAO.md)

</div>

---

## Sobre

API REST para organizar registros de produtos a partir de seus códigos de barras. O projeto reúne validação de dados, persistência relacional e documentação interativa em uma estrutura compacta.

## Destaques

- Cadastro de código de barras e data de entrada.
- Consulta por ID e listagem com paginação.
- Exclusão de registros.
- Documentação interativa das rotas pelo FastAPI.

## Como executar

Clone o repositório:

```sh
git clone https://github.com/Kakykyyy/barcode-API.git
cd barcode-API
```

Envie a data de entrada no cadastro. A aplicação recebe o código como texto; leitura por câmera não está implementada.

```sh
python -m venv .venv
# Ative o ambiente virtual antes de continuar.
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Acesse [a aplicação local](http://127.0.0.1:8000/docs).

Para ativar o ambiente virtual, use `.venv\Scripts\Activate.ps1` no PowerShell ou `source .venv/bin/activate` no Linux/macOS.

## Organização

```text
app/
├── main.py       # Aplicação e rotas
├── models.py     # Modelo de produto
├── schemas.py    # Contratos de entrada e saída
├── crud.py       # Operações de persistência
└── database.py   # Conexão SQLite
```

## Exemplo de uso

Envie um `POST /produtos/` com:

```json
{
  "codigo_barras": "7891234567890",
  "data_entrada": "2026-11-02T12:00:00"
}
```

| Método | Rota | Ação |
|---|---|---|
| POST | `/produtos/` | Cadastrar |
| GET | `/produtos/` | Listar |
| GET | `/produtos/{product_id}` | Consultar |
| DELETE | `/produtos/{product_id}` | Excluir |

## Documentação técnica

O [guia técnico](DOCUMENTACAO.md) reúne configuração, comportamento dos dados, limitações conhecidas e verificações manuais. Os fluxos de cadastro, consulta, listagem, exclusão, duplicidade e validação de data são cobertos por testes automatizados.

## Autor

Desenvolvido por [Kayky Erick · @Kakykyyy](https://github.com/Kakykyyy).

## Testes automatizados

Use Python 3.12 e instale as dependências de desenvolvimento:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Os testes usam SQLite temporário, sem alterar seu banco de produtos. Código duplicado retorna 400; data ausente, nula ou inválida retorna 422. A resposta de criação permanece 200. O GitHub Actions executa a suíte a cada push e pull request.
