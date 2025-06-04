"""Configuration for Ozon API access."""

import os

# Base URL for Ozon Seller API
API_URL = "https://api-seller.ozon.ru"

# Client ID and API key must be set as environment variables
CLIENT_ID = os.getenv("OZON_CLIENT_ID")
API_KEY = os.getenv("OZON_API_KEY")

HEADERS = {
    "Client-Id": CLIENT_ID or "",
    "Api-Key": API_KEY or "",
    "Content-Type": "application/json",
}
