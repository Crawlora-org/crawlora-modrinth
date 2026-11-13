# Modrinth API endpoint reference and client usage

This reference lists all 34 public Modrinth API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/modrinth`, `crawlora-modrinth`, and `crawlora-modrinth` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Modrinth locally; Crawlora is independent from and not endorsed by Modrinth or its owners.

The package tracks the public API contract revision `sha256:5341542aa3348dd1331db6d30348f76aed08640ae369839ddf821af91bd7c21f` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `modrinth`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `checkProject` | `check_project` | `modrinth.check_project` | `GET /modrinth/project/{id}/check` | `id` (path, required) | Resolve a project ID or slug |
| `collection` | `collection` | `modrinth.collection` | `GET /modrinth/collection/{id}` | `id` (path, required) | Read a public Modrinth collection |
| `collections` | `collections` | `modrinth.collections` | `GET /modrinth/collections` | `ids` (query, required) | Resolve public Modrinth collections |
| `dependencies` | `dependencies` | `modrinth.dependencies` | `GET /modrinth/project/{id}/dependencies` | `id` (path, required) | Get project dependency metadata |
| `fileProjects` | `file_projects` | `modrinth.file_projects` | `POST /modrinth/version_file/project` | `body` (body, required) | Resolve file hashes to projects |
| `filesUpdate` | `files_update` | `modrinth.files_update` | `POST /modrinth/version_files/update` | `body` (body, required) | Resolve compatible updates for files |
| `filesUpdateIndividual` | `files_update_individual` | `modrinth.files_update_individual` | `POST /modrinth/version_files/update_individual` | `body` (body, required) | Resolve updates with per-file filters |
| `filesUpdateMany` | `files_update_many` | `modrinth.files_update_many` | `POST /modrinth/version_files/update_many` | `body` (body, required) | List compatible update versions for files |
| `fileUpdate` | `file_update` | `modrinth.file_update` | `POST /modrinth/version_file/{hash}/update` | `hash` (path, required), `algorithm` (query, optional; values: `sha1`, `sha512`), `body` (body, required) | Resolve a compatible update for a file |
| `fileVersion` | `file_version` | `modrinth.file_version` | `GET /modrinth/version_file/{hash}` | `hash` (path, required), `algorithm` (query, optional; values: `sha1`, `sha512`) | Resolve a version by file hash |
| `fileVersions` | `file_versions` | `modrinth.file_versions` | `POST /modrinth/version_files` | `body` (body, required) | Resolve file hashes to versions |
| `forgeUpdates` | `forge_updates` | `modrinth.forge_updates` | `GET /modrinth/updates/{id}/forge_updates.json` | `id` (path, required), `neoforge` (query, optional; values: `include`, `only`) | Get native Forge update metadata |
| `license` | `license` | `modrinth.license` | `GET /modrinth/tag/license/{id}` | `id` (path, required) | Get source license title and text |
| `metadataLinkPlatforms` | `metadata_link_platforms` | `modrinth.metadata_link_platforms` | `GET /modrinth/metadata/link-platforms` | — | Get Modrinth link platforms |
| `metadataLoaderFields` | `metadata_loader_fields` | `modrinth.metadata_loader_fields` | `GET /modrinth/metadata/loader-fields` | — | Discover Modrinth loader fields |
| `metadataLoaderFieldValues` | `metadata_loader_field_values` | `modrinth.metadata_loader_field_values` | `GET /modrinth/metadata/loader-fields/{field}` | `field` (path, required) | Get Modrinth loader-field values |
| `metadataLoaders` | `metadata_loaders` | `modrinth.metadata_loaders` | `GET /modrinth/metadata/loaders` | — | Get Modrinth loader capabilities |
| `organization` | `organization` | `modrinth.organization` | `GET /modrinth/organization/{id}` | `id` (path, required) | Read a public Modrinth organization |
| `organizationProjects` | `organization_projects` | `modrinth.organization_projects` | `GET /modrinth/organization/{id}/projects` | `id` (path, required) | Read a public organization's Modrinth projects |
| `organizations` | `organizations` | `modrinth.organizations` | `GET /modrinth/organizations` | `ids` (query, required) | Resolve public Modrinth organizations |
| `project` | `project` | `modrinth.project` | `GET /modrinth/project/{id}` | `id` (path, required) | Get a Modrinth project |
| `projectDisclosures` | `project_disclosures` | `modrinth.project_disclosures` | `GET /modrinth/project/{id}/disclosures` | `id` (path, required) | Get Modrinth public project disclosures |
| `projects` | `projects` | `modrinth.projects` | `GET /modrinth/projects` | `ids` (query, required) | Get native multiple-project metadata |
| `projectVersion` | `project_version` | `modrinth.project_version` | `GET /modrinth/project/{id}/version/{number}` | `id` (path, required), `number` (path, required) | Get a project version by number or ID |
| `projectVersions` | `project_versions` | `modrinth.project_versions` | `GET /modrinth/project/{id}/version` | `id` (path, required), `loaders` (query, optional), `game_versions` (query, optional), `featured` (query, optional), `include_changelog` (query, optional) | List project versions |
| `randomProjects` | `random_projects` | `modrinth.random_projects` | `GET /modrinth/projects_random` | `count` (query, required) | Get native random projects |
| `search` | `search` | `modrinth.search` | `GET /modrinth/search` | `query` (query, optional), `facets` (query, optional), `index` (query, optional; values: `relevance`, `downloads`, `follows`, `newest`, `updated`), `offset` (query, optional), `limit` (query, optional) | Search Modrinth projects |
| `searchV3` | `search_v3` | `modrinth.search_v3` | `GET /modrinth/v3/search` | `query` (query, optional), `index` (query, optional; values: `relevance`, `downloads`, `follows`, `newest`, `updated`, `date_created`, `date_modified`, `minecraft_java_server.verified_plays_2w`, `minecraft_java_server.ping.data.players_online`), `offset` (query, optional), `limit` (query, optional), `new_filters` (query, optional), `facets` (query, optional), `filters` (query, optional), `version` (query, optional) | Search current Modrinth projects and servers |
| `searchV3Body` | `search_v3_body` | `modrinth.search_v3_body` | `POST /modrinth/v3/search` | `body` (body, required) | Search Modrinth using the native v3 JSON body |
| `searchV3Options` | `search_v3_options` | `modrinth.search_v3_options` | `GET /modrinth/v3/search/options` | — | Discover Modrinth v3 search options |
| `statistics` | `statistics` | `modrinth.statistics` | `GET /modrinth/statistics` | — | Get Modrinth instance statistics |
| `tags` | `tags` | `modrinth.tags` | `GET /modrinth/tag/{type}` | `type` (path, required; values: `category`, `loader`, `game_version`, `license`, `donation_platform`, `report_type`, `project_type`, `side_type`) | Discover Modrinth catalog values |
| `version` | `version` | `modrinth.version` | `GET /modrinth/version/{id}` | `id` (path, required) | Get a version by ID |
| `versions` | `versions` | `modrinth.versions` | `GET /modrinth/versions` | `ids` (query, required) | Get native multiple-version metadata |

## Client forms

- JavaScript: import `ModrinthClient` (also exported as `Client`) from `@crawlora-org/modrinth`; use `new ModrinthClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `ModrinthClient` (also exported as `Client`) from `crawlora_modrinth`; use `with ModrinthClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncModrinthClient`, used with `async with` and `await`.
- Rust: add `crawlora-modrinth` with Cargo; import `Client` and the generated operation parameter struct, then call `client.modrinth.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-modrinth/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
