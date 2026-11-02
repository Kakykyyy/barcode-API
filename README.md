# Barcode API

API de cadastro e consulta de códigos de barras, desenvolvida com FastAPI, SQLAlchemy e SQLite. Recebe códigos como texto; não há leitura de câmera ou geração de códigos implementada.

## Requisitos e instalação

Use Python 3.10 ou superior como ambiente de desenvolvimento sugerido. As dependências não possuem versões fixadas no repositório.

```sh
git clone https://github.com/Kakykyyy/barcode-API.git
cd barcode-API
python -m venv .venv
```

Ative o ambiente com `.venv\Scripts\Activate.ps1` no PowerShell ou `source .venv/bin/activate` no Linux/macOS.

```sh
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

A API fica em http://127.0.0.1:8000; a documentação interativa em http://127.0.0.1:8000/docs.

## Rotas

| Método | Caminho | Comportamento |
|---|---|---|
| POST | `/produtos/` | Cadastra código e data de entrada |
| GET | `/produtos/` | Lista produtos; aceita `skip` e `limit` (padrões 0 e 10) |
| GET | `/produtos/{product_id}` | Consulta por ID; retorna 404 quando ausente |
| DELETE | `/produtos/{product_id}` | Exclui por ID |

Exemplo de corpo para POST:

```json
{
  "codigo_barras": "7891234567890",
  "data_entrada": "2026-11-02T12:00:00"
}
```

A resposta contém `id`, `codigo_barras` e `data_entrada`. O POST usa o status padrão 200 do FastAPI.

## Estrutura e dados

- `app/main.py`: aplicação, CORS, rotas e ciclo de sessão do banco.
- `app/database.py`: conexão SQLite e base dos modelos.
- `app/models.py`: tabela `produtos`, com código único e data obrigatória.
- `app/schemas.py`: contratos Pydantic.
- `app/crud.py`: persistência e consultas.
- `requirements.txt`: dependências.

O arquivo `products.db` é criado no diretório de execução. As tabelas são criadas ao importar a aplicação. Preserve esse arquivo para manter os registros; não há migrações versionadas.

## Limitações conhecidas

- Envie `data_entrada`: o schema permite omiti-la, mas a coluna do banco não aceita valor nulo.
- Códigos duplicados violam a restrição única. O CRUD não trata essa exceção; o retorno 400 previsto na rota não cobre esse caso.
- DELETE informa sucesso mesmo quando o ID não existe.
- `orm_mode` é configuração do Pydantic v1. A instalação sem versões fixadas pode trazer v2 e exigir adaptação para `from_attributes`.
- Não há autenticação e o CORS está aberto. A configuração atual é de protótipo.

## Verificação manual

Cadastre um produto com data, liste os registros, consulte o ID recebido e exclua-o. A consulta posterior deve retornar 404. Não há suíte de testes no repositório.

## Licença

O README anterior mencionava MIT, mas não há arquivo LICENSE na árvore analisada. Confirme os termos com o autor antes de redistribuir.

---
Documentação baseada na leitura da branch principal em 2 de novembro de 2026. Os procedimentos não foram executados nesta revisão documental.
