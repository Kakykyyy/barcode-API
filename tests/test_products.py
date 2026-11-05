import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Import in a temporary directory so even startup uses a disposable database.
    monkeypatch.chdir(tmp_path)
    from app import database
    from app.main import app, get_db
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"sqlite:///{tmp_path / 'test.db'}",
        connect_args={"check_same_thread": False},
    )
    database.Base.metadata.create_all(bind=engine)
    sessions = sessionmaker(bind=engine)

    def override_db():
        with sessions() as session:
            yield session

    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def payload(code="7891234567890"):
    return {"codigo_barras": code, "data_entrada": "2026-11-05T12:00:00"}


def test_create_read_list_and_delete(client):
    response = client.post("/produtos/", json=payload())
    assert response.status_code == 200
    product = response.json()
    assert product["codigo_barras"] == payload()["codigo_barras"]
    assert product["data_entrada"] == payload()["data_entrada"]
    product_id = product["id"]
    assert client.get(f"/produtos/{product_id}").json() == product
    assert client.get("/produtos/").json() == [product]
    assert client.delete(f"/produtos/{product_id}").status_code == 200
    assert client.get(f"/produtos/{product_id}").status_code == 404
    assert client.get("/produtos/").json() == []


def test_duplicate_returns_400_and_keeps_original(client):
    original = client.post("/produtos/", json=payload()).json()
    duplicate = client.post("/produtos/", json=payload())
    assert duplicate.status_code == 400
    assert duplicate.json() == {"detail": "Produto já cadastrado."}
    assert client.get("/produtos/").json() == [original]
    assert client.post("/produtos/", json=payload("00001234")).status_code == 200


@pytest.mark.parametrize("date_fields", [{}, {"data_entrada": None}, {"data_entrada": "invalid"}])
def test_invalid_or_missing_date_returns_422(client, date_fields):
    response = client.post("/produtos/", json={"codigo_barras": "123", **date_fields})
    assert response.status_code == 422
    assert client.get("/produtos/").json() == []


def test_unknown_product_returns_404(client):
    assert client.get("/produtos/99999").status_code == 404
