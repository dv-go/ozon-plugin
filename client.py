"""Simple Ozon API client."""
from typing import Any, Dict
import requests

from config import API_URL, HEADERS


def request(endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send POST request to the given endpoint and return the JSON response."""
    url = f"{API_URL}{endpoint}"
    resp = requests.post(url, json=payload, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()
