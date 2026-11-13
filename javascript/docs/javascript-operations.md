# Crawlora Modrinth JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `34`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| modrinth | `modrinth.collection` | `modrinth-collection` | `GET /modrinth/collection/{id}` | `id` (path string required) | `ApiKeyAuth` | `ModrinthCollectionResponse` |  |
| modrinth | `modrinth.collections` | `modrinth-collections` | `GET /modrinth/collections` | `ids` (query string required) | `ApiKeyAuth` | `ModrinthCollectionsResponse` |  |
| modrinth | `modrinth.metadataLinkPlatforms` | `modrinth-metadata-link-platforms` | `GET /modrinth/metadata/link-platforms` | none | `ApiKeyAuth` | `ModrinthMetadataLinkPlatformsResponse` |  |
| modrinth | `modrinth.metadataLoaderFields` | `modrinth-metadata-loader-fields` | `GET /modrinth/metadata/loader-fields` | none | `ApiKeyAuth` | `ModrinthMetadataLoaderFieldsResponse` |  |
| modrinth | `modrinth.metadataLoaderFieldValues` | `modrinth-metadata-loader-field-values` | `GET /modrinth/metadata/loader-fields/{field}` | `field` (path string required) | `ApiKeyAuth` | `ModrinthMetadataLoaderFieldValuesResponse` |  |
| modrinth | `modrinth.metadataLoaders` | `modrinth-metadata-loaders` | `GET /modrinth/metadata/loaders` | none | `ApiKeyAuth` | `ModrinthMetadataLoadersResponse` |  |
| modrinth | `modrinth.organization` | `modrinth-organization` | `GET /modrinth/organization/{id}` | `id` (path string required) | `ApiKeyAuth` | `ModrinthOrganizationResponse` |  |
| modrinth | `modrinth.organizationProjects` | `modrinth-organization-projects` | `GET /modrinth/organization/{id}/projects` | `id` (path string required) | `ApiKeyAuth` | `ModrinthOrganizationProjectsResponse` |  |
| modrinth | `modrinth.organizations` | `modrinth-organizations` | `GET /modrinth/organizations` | `ids` (query string required) | `ApiKeyAuth` | `ModrinthOrganizationsResponse` |  |
| modrinth | `modrinth.project` | `modrinth-project` | `GET /modrinth/project/{id}` | `id` (path string required) | `ApiKeyAuth` | `ModrinthProjectResponse` |  |
| modrinth | `modrinth.checkProject` | `modrinth-check-project` | `GET /modrinth/project/{id}/check` | `id` (path string required) | `ApiKeyAuth` | `ModrinthCheckProjectResponse` |  |
| modrinth | `modrinth.dependencies` | `modrinth-dependencies` | `GET /modrinth/project/{id}/dependencies` | `id` (path string required) | `ApiKeyAuth` | `ModrinthDependenciesResponse` |  |
| modrinth | `modrinth.projectDisclosures` | `modrinth-project-disclosures` | `GET /modrinth/project/{id}/disclosures` | `id` (path string required) | `ApiKeyAuth` | `ModrinthProjectDisclosuresResponse` |  |
| modrinth | `modrinth.projectVersions` | `modrinth-project-versions` | `GET /modrinth/project/{id}/version` | `id` (path string required)<br>`loaders` (query string)<br>`game_versions` (query string)<br>`featured` (query boolean)<br>`include_changelog` (query boolean) | `ApiKeyAuth` | `ModrinthProjectVersionsResponse` |  |
| modrinth | `modrinth.projectVersion` | `modrinth-project-version` | `GET /modrinth/project/{id}/version/{number}` | `id` (path string required)<br>`number` (path string required) | `ApiKeyAuth` | `ModrinthProjectVersionResponse` |  |
| modrinth | `modrinth.projects` | `modrinth-projects` | `GET /modrinth/projects` | `ids` (query string required) | `ApiKeyAuth` | `ModrinthProjectsResponse` |  |
| modrinth | `modrinth.randomProjects` | `modrinth-random-projects` | `GET /modrinth/projects_random` | `count` (query number required) | `ApiKeyAuth` | `ModrinthRandomProjectsResponse` |  |
| modrinth | `modrinth.search` | `modrinth-search` | `GET /modrinth/search` | `query` (query string)<br>`facets` (query string)<br>`index` (query "relevance" \| "downloads" \| "follows" \| "newest" \| "updated")<br>`offset` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `ModrinthSearchResponse` |  |
| modrinth | `modrinth.statistics` | `modrinth-statistics` | `GET /modrinth/statistics` | none | `ApiKeyAuth` | `ModrinthStatisticsResponse` |  |
| modrinth | `modrinth.license` | `modrinth-license` | `GET /modrinth/tag/license/{id}` | `id` (path string required) | `ApiKeyAuth` | `ModrinthLicenseResponse` |  |
| modrinth | `modrinth.tags` | `modrinth-tags` | `GET /modrinth/tag/{type}` | `type` (path "category" \| "loader" \| "game_version" \| "license" \| "donation_platform" \| "report_type" \| "project_type" \| "side_type" required) | `ApiKeyAuth` | `ModrinthTagsResponse` |  |
| modrinth | `modrinth.forgeUpdates` | `modrinth-forge-updates` | `GET /modrinth/updates/{id}/forge_updates.json` | `id` (path string required)<br>`neoforge` (query "include" \| "only") | `ApiKeyAuth` | `ModrinthForgeUpdatesResponse` |  |
| modrinth | `modrinth.searchV3` | `modrinth-search-v3` | `GET /modrinth/v3/search` | `query` (query string)<br>`index` (query "relevance" \| "downloads" \| "follows" \| "newest" \| "updated" \| "date_created" \| "date_modified" \| "minecraft_java_server.verified_plays_2w" \| "minecraft_java_server.ping.data.players_online")<br>`offset` (query number)<br>`limit` (query number)<br>`new_filters` (query string)<br>`facets` (query string)<br>`filters` (query string)<br>`version` (query string) | `ApiKeyAuth` | `ModrinthSearchV3Response` |  |
| modrinth | `modrinth.searchV3Body` | `modrinth-search-v3-body` | `POST /modrinth/v3/search` | `body` (body string required) | `ApiKeyAuth` | `ModrinthSearchV3BodyResponse` |  |
| modrinth | `modrinth.searchV3Options` | `modrinth-search-v3-options` | `GET /modrinth/v3/search/options` | none | `ApiKeyAuth` | `ModrinthSearchV3OptionsResponse` |  |
| modrinth | `modrinth.version` | `modrinth-version` | `GET /modrinth/version/{id}` | `id` (path string required) | `ApiKeyAuth` | `ModrinthVersionResponse` |  |
| modrinth | `modrinth.fileProjects` | `modrinth-file-projects` | `POST /modrinth/version_file/project` | `body` (body string required) | `ApiKeyAuth` | `ModrinthFileProjectsResponse` |  |
| modrinth | `modrinth.fileVersion` | `modrinth-file-version` | `GET /modrinth/version_file/{hash}` | `hash` (path string required)<br>`algorithm` (query "sha1" \| "sha512") | `ApiKeyAuth` | `ModrinthFileVersionResponse` |  |
| modrinth | `modrinth.fileUpdate` | `modrinth-file-update` | `POST /modrinth/version_file/{hash}/update` | `hash` (path string required)<br>`algorithm` (query "sha1" \| "sha512")<br>`body` (body string required) | `ApiKeyAuth` | `ModrinthFileUpdateResponse` |  |
| modrinth | `modrinth.fileVersions` | `modrinth-file-versions` | `POST /modrinth/version_files` | `body` (body string required) | `ApiKeyAuth` | `ModrinthFileVersionsResponse` |  |
| modrinth | `modrinth.filesUpdate` | `modrinth-files-update` | `POST /modrinth/version_files/update` | `body` (body string required) | `ApiKeyAuth` | `ModrinthFilesUpdateResponse` |  |
| modrinth | `modrinth.filesUpdateIndividual` | `modrinth-files-update-individual` | `POST /modrinth/version_files/update_individual` | `body` (body string required) | `ApiKeyAuth` | `ModrinthFilesUpdateIndividualResponse` |  |
| modrinth | `modrinth.filesUpdateMany` | `modrinth-files-update-many` | `POST /modrinth/version_files/update_many` | `body` (body string required) | `ApiKeyAuth` | `ModrinthFilesUpdateManyResponse` |  |
| modrinth | `modrinth.versions` | `modrinth-versions` | `GET /modrinth/versions` | `ids` (query string required) | `ApiKeyAuth` | `ModrinthVersionsResponse` |  |
