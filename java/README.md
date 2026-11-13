# Crawlora Modrinth API client for Java

The official Java client for Crawlora's hosted Modrinth API. It exposes 34 endpoints covering project search and metadata, versions, dependencies, collections, organizations, and file compatibility. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-modrinth</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-java-console) to get an API key.

```java
import net.crawlora.modrinth.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.statistics(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Modrinth API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-modrinth)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-java-api-docs)
