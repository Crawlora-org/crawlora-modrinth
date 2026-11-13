# Crawlora Modrinth API client for PHP (`crawlora/modrinth`)

This PHP package calls Crawlora's hosted Modrinth API at `https://api.crawlora.net/api/v1`. It exposes 34 endpoints covering project search and metadata, versions, dependencies, collections, organizations, and file compatibility. It does not call or scrape Modrinth directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/modrinth
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Modrinth\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("modrinth-search", ['query' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 34 API operations.

## Supported Modrinth API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-modrinth). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/docs/usage.md).
