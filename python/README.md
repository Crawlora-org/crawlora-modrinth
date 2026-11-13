# crawlora-modrinth — Modrinth API client for Python

Python client for Crawlora's hosted Modrinth API. It exposes 34 API endpoints covering project search and metadata, versions, dependencies, collections, organizations, and file compatibility. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-python-homepage); the package does not run a browser or scrape
Modrinth locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Modrinth or its owners.

## Install

```sh
python -m pip install crawlora-modrinth
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_modrinth import ModrinthClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ModrinthClient(api_key=api_key) as client:
    result_1 = client.search(query='sodium', limit=5)
    print(result_1)
    result_2 = client.statistics()
    print(result_2)
```

The package also exports `Client` as an alias for `ModrinthClient`. Operation
methods are available directly in snake_case and through the `modrinth`
group. The async package client is `AsyncModrinthClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_modrinth import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(query='sodium', limit=5)
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/examples/python.py) for a complete usage example.

## Supported Modrinth API endpoints

This package exposes every route below through direct snake_case methods and the `modrinth` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/modrinth/collection/{id}` | `modrinth-collection` | Read a public Modrinth collection |
| `GET` | `/modrinth/collections` | `modrinth-collections` | Resolve public Modrinth collections |
| `GET` | `/modrinth/metadata/link-platforms` | `modrinth-metadata-link-platforms` | Get Modrinth link platforms |
| `GET` | `/modrinth/metadata/loader-fields` | `modrinth-metadata-loader-fields` | Discover Modrinth loader fields |
| `GET` | `/modrinth/metadata/loader-fields/{field}` | `modrinth-metadata-loader-field-values` | Get Modrinth loader-field values |
| `GET` | `/modrinth/metadata/loaders` | `modrinth-metadata-loaders` | Get Modrinth loader capabilities |
| `GET` | `/modrinth/organization/{id}` | `modrinth-organization` | Read a public Modrinth organization |
| `GET` | `/modrinth/organization/{id}/projects` | `modrinth-organization-projects` | Read a public organization's Modrinth projects |
| `GET` | `/modrinth/organizations` | `modrinth-organizations` | Resolve public Modrinth organizations |
| `GET` | `/modrinth/project/{id}` | `modrinth-project` | Get a Modrinth project |
| `GET` | `/modrinth/project/{id}/check` | `modrinth-check-project` | Resolve a project ID or slug |
| `GET` | `/modrinth/project/{id}/dependencies` | `modrinth-dependencies` | Get project dependency metadata |
| `GET` | `/modrinth/project/{id}/disclosures` | `modrinth-project-disclosures` | Get Modrinth public project disclosures |
| `GET` | `/modrinth/project/{id}/version` | `modrinth-project-versions` | List project versions |
| `GET` | `/modrinth/project/{id}/version/{number}` | `modrinth-project-version` | Get a project version by number or ID |
| `GET` | `/modrinth/projects` | `modrinth-projects` | Get native multiple-project metadata |
| `GET` | `/modrinth/projects_random` | `modrinth-random-projects` | Get native random projects |
| `GET` | `/modrinth/search` | `modrinth-search` | Search Modrinth projects |
| `GET` | `/modrinth/statistics` | `modrinth-statistics` | Get Modrinth instance statistics |
| `GET` | `/modrinth/tag/license/{id}` | `modrinth-license` | Get source license title and text |
| `GET` | `/modrinth/tag/{type}` | `modrinth-tags` | Discover Modrinth catalog values |
| `GET` | `/modrinth/updates/{id}/forge_updates.json` | `modrinth-forge-updates` | Get native Forge update metadata |
| `GET` | `/modrinth/v3/search` | `modrinth-search-v3` | Search current Modrinth projects and servers |
| `POST` | `/modrinth/v3/search` | `modrinth-search-v3-body` | Search Modrinth using the native v3 JSON body |
| `GET` | `/modrinth/v3/search/options` | `modrinth-search-v3-options` | Discover Modrinth v3 search options |
| `GET` | `/modrinth/version/{id}` | `modrinth-version` | Get a version by ID |
| `POST` | `/modrinth/version_file/project` | `modrinth-file-projects` | Resolve file hashes to projects |
| `GET` | `/modrinth/version_file/{hash}` | `modrinth-file-version` | Resolve a version by file hash |
| `POST` | `/modrinth/version_file/{hash}/update` | `modrinth-file-update` | Resolve a compatible update for a file |
| `POST` | `/modrinth/version_files` | `modrinth-file-versions` | Resolve file hashes to versions |
| `POST` | `/modrinth/version_files/update` | `modrinth-files-update` | Resolve compatible updates for files |
| `POST` | `/modrinth/version_files/update_individual` | `modrinth-files-update-individual` | Resolve updates with per-file filters |
| `POST` | `/modrinth/version_files/update_many` | `modrinth-files-update-many` | List compatible update versions for files |
| `GET` | `/modrinth/versions` | `modrinth-versions` | Get native multiple-version metadata |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
