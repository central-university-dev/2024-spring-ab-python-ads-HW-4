"""testing template"""
from fastapi.testclient import TestClient
import pytest
from main import app  # Убедитесь, что путь к приложению указан правильно

client = TestClient(app)

def test_get_tree_count():
    """
    Тестирует POST-запрос к эндпоинту /trees.
    Проверяет корректность ответа и наличие ключа 'trees_count' в ответе.
    """
    response = client.post("/trees", json={"city": "Berlin", "country": "Germany", "year": 2020})
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["city"] == "Berlin"
    assert data["country"] == "Germany"
    assert data["year"] == 2020
    assert "trees_count" in data
    assert isinstance(data["trees_count"], int)  # Проверяем, что 'trees_count' является числом