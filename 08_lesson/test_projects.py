import uuid
import pytest
from yougile_api import YougileAPI

URL = "https://ru.yougile.com"
API_KEY = "iRrsh698igTNOkomDwSHVITWqEwHQ7PRGtK3dU7tl0Ml7qMHfLV-oQxizuuZCttX"


@pytest.fixture(scope="function")
def api_client():
    """API клиент для каждого теста."""
    return YougileAPI(URL, API_KEY)


@pytest.fixture(scope="function")
def created_project(api_client):
    """Создает проект и удаляет после теста."""
    project_name = f"test-{uuid.uuid4().hex[:8]}"
    payload = {"name": project_name, "description": "test project"}

    resp = api_client.create_project(payload)
    assert resp.status_code == 201, f"Create failed: {resp.status_code}"
    project_id = resp.json()["id"]

    yield project_id

    # Очистка: удаляем проект после теста
    delete_resp = api_client.delete_project(project_id)
    assert delete_resp.status_code in (200, 204, 404), "Cleanup failed"


class TestProjectsAPI:
    """Тесты CRUD операций с проектами."""

    def test_create_project_positive(self, api_client):
        """Позитив: создание проекта."""
        payload = {"name": f"POS-{uuid.uuid4().hex[:8]}"}
        resp = api_client.create_project(payload)

        assert resp.status_code == 201
        body = resp.json()
        assert "id" in body
        assert body["name"] == payload["name"]

    def test_create_project_negative_empty_name(self, api_client):
        """Негатив: создание без name."""
        payload = {"description": "no name"}
        resp = api_client.create_project(payload)

        assert resp.status_code in (400, 422)
        body = resp.json()
        error_text = str(body).lower()
        assert any(
            msg in error_text
            for msg in ["name", "required", "обязательно"]
        )

    def test_get_project_positive(self, api_client, created_project):
        """Позитив: получение проекта."""
        resp = api_client.get_project(created_project)
        assert resp.status_code == 200
        body = resp.json()
        assert body["id"] == created_project

    def test_get_project_negative_nonexistent(self, api_client):
        """Негатив: несуществующий проект."""
        fake_id = str(uuid.uuid4())
        resp = api_client.get_project(fake_id)

        assert resp.status_code == 404
        body = resp.json()
        error_text = str(body).lower()
        assert any(msg in error_text for msg in ["not found", "не найден"])

    def test_update_project_positive(self, api_client, created_project):
        """Позитив: обновление проекта."""
        new_name = f"UPDATED-{uuid.uuid4().hex[:8]}"
        payload = {"name": new_name}
        resp = api_client.update_project(created_project, payload)

        assert resp.status_code == 200
        body = resp.json()
        assert body["name"] == new_name

    def test_update_project_negative_invalid_id(self, api_client):
        """Негатив: неверный ID."""
        invalid_id = "invalid-uuid"
        payload = {"name": "test"}
        resp = api_client.update_project(invalid_id, payload)

        assert resp.status_code in (400, 404)
        body = resp.json()
        error_text = str(body).lower()
        assert any(msg in error_text for msg in ["invalid", "неверный"])

    def test_update_project_negative_empty_body(self, api_client, created_project):
        """Негатив: пустое тело обновления."""
        resp = api_client.update_project(created_project, {})
        assert resp.status_code in (400, 422)
        body = resp.json()
        error_text = str(body).lower()
        assert any(msg in error_text for msg in ["name", "required"])
