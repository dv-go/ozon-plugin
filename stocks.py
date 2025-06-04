"""Retrieve stocks of an Ozon product by article."""

import argparse
from client import request

ENDPOINT = "/v3/product/info/stocks-by-sku"


def fetch_stocks(article: str):
    """Return stock information for the given article."""
    payload = {"offer_id": article}
    return request(ENDPOINT, payload)


def main() -> None:
    parser = argparse.ArgumentParser(description="Show stocks for a given Ozon article")
    parser.add_argument("article", help="Article number (offer_id) to query")
    args = parser.parse_args()

    try:
        data = fetch_stocks(args.article)
        stocks = data.get("result", {}).get("stocks", [])
        if not stocks:
            print("No stock information found")
            return
        for item in stocks:
            wh = item.get("warehouse_id")
            qty = item.get("present")
            print(f"Warehouse {wh}: {qty}")
    except Exception as exc:
        print(f"Error while requesting Ozon API: {exc}")


if __name__ == "__main__":
    main()
