import uuid
import pytest
from yougile_api import YougileAPI


url = "https://ru.yougile.com"
API_KEY = "iRrsh698igTNOkomDwSHVITWqEwHQ7PRGtK3dU7tl0Ml7qMHfLV-oQxizuuZCttX"

@pytest.fixture(scope="session")
def api_client():
    return YougileAPI(url, API_KEY)


@pytest.fixture(scope="session")
def created_project_id(api_client) -> str:
    """
    Создаёт проект, чтобы использовать в позитивных тестах GET/PUT.
    """
    payload = {
        "name": f"Fixture Project {uuid.uuid4()}",
        "description": "Created for tests"
    }
    resp = api_client.create_project(payload)
    assert resp.status_code == 201, f"Failed creating fixture project: {resp.status_code} {resp.text}"
    return resp.json()["id"]


class TestProjectsAPI:
    # ========== POST /api-v2/projects ==========
    def test_create_project_positive(self, api_client):
        payload = {"name": f"Positive create {uuid.uuid4()}"}
        resp = api_client.create_project(payload)
        assert resp.status_code == 201
        body = resp.json()
        assert "id" in body and body["name"] == payload["name"]

    def test_create_project_negative_empty_name(self, api_client):
        # Ожидаем ошибку валидации (400 или 422) при отсутствии name
        payload = {"description": "no name"}
        resp = api_client.create_project(payload)
        assert resp.status_code in (400, 422)
        # Если API возвращает структуру с errors, проверим наличие name в ошибках
        try:
            body = resp.json()
        except ValueError:
            body = {}
        errors = body.get("errors") or body
        # допустимо, что структура ошибок разная — проверяем, что есть указание на name
        assert ("name" in errors) or ("Name" in errors) or ("name" in str(body).lower())

    # ========== GET /api-v2/projects/{id} ==========
    def test_get_project_positive(self, api_client, created_project_id):
        resp = api_client.get_project(created_project_id)
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("id") == created_project_id
        assert "name" in body

    def test_get_project_negative_nonexistent_id(self, api_client):
        nonexistent_id = str(uuid.uuid4())
        resp = api_client.get_project(nonexistent_id)
        assert resp.status_code == 404

    # ========== PUT /api-v2/projects/{id} ==========
    def test_update_project_positive(self, api_client, created_project_id):
        update_payload = {"name": f"Updated name {uuid.uuid4()}", "description": "updated"}
        resp = api_client.update_project(created_project_id, update_payload)
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("name") == update_payload["name"]

    def test_update_project_negative_invalid_id(self, api_client):
        invalid_id = "invalid-uuid-format"
        update_payload = {"name": "Should fail"}
        resp = api_client.update_project(invalid_id, update_payload)
        # API может вернуть 404 (not found) или 400 (bad request) for invalid id format
        assert resp.status_code in (400, 404)

    def test_update_project_negative_empty_body(self, api_client, created_project_id):
        # Попытка обновления с пустым телом — ожидаем ошибку валидации
        resp = api_client.update_project(created_project_id, {})
        assert resp.status_code in (400, 422)
