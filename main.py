"""Example entry point for using the Ozon API client."""

from pprint import pprint

from client import request


def main() -> None:
    # Example: get list of posted offers (dummy payload)
    endpoint = "/v1/product/list"
    payload = {
        "limit": 10,
        "offset": 0,
    }

    try:
        data = request(endpoint, payload)
        pprint(data)
    except Exception as exc:
        print(f"Error while requesting Ozon API: {exc}")


if __name__ == "__main__":
    main()
