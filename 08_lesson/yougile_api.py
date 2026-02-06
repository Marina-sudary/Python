import requests
from typing import Optional, Dict, Any


class YougileAPI:

    def __init__(self, base_url: str, api_key: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"YOUGILE-KEY {api_key}",
            "Content-Type": "application/json"
        }
        self.timeout = timeout

    def create_project(
        self,
        project_data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """Создание проекта. POST /api-v2/projects."""
        hdrs = self._merge_headers(headers)
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            headers=hdrs,
            json=project_data,
            timeout=self.timeout
        )

    def get_project(
        self,
        project_id: str,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """Получение проекта. GET /api-v2/projects/{id}."""
        hdrs = self._merge_headers(headers)
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=hdrs,
            timeout=self.timeout
        )

    def update_project(
        self,
        project_id: str,
        update_data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """Обновление проекта. PUT /api-v2/projects/{id}."""
        hdrs = self._merge_headers(headers)
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=hdrs,
            json=update_data,
            timeout=self.timeout
        )

    def delete_project(
        self,
        project_id: str,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        """Удаление проекта. DELETE /api-v2/projects/{id}."""
        hdrs = self._merge_headers(headers)
        return requests.delete(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=hdrs,
            timeout=self.timeout
        )

    def _merge_headers(
        self,
        extra: Optional[Dict[str, str]]
    ) -> Dict[str, str]:
        """Объединить базовые заголовки с дополнительными."""
        if not extra:
            return self.headers.copy()
        merged = self.headers.copy()
        merged.update(extra)
        return merged
