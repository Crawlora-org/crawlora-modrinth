import os

from crawlora_modrinth import ModrinthClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ModrinthClient(api_key=api_key) as client:
    search = client.search(query='sodium', limit=5)
    print('search', search)
    statistics = client.statistics()
    print('statistics', statistics)
