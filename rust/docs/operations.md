# Crawlora Modrinth Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `34`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| modrinth | `modrinth.collection` | `modrinth-collection` | `GET /modrinth/collection/{id}` | `id` (path String required) | `ApiKeyAuth` | `ModrinthCollectionResponse` |  |
| modrinth | `modrinth.collections` | `modrinth-collections` | `GET /modrinth/collections` | `ids` (query String required) | `ApiKeyAuth` | `ModrinthCollectionsResponse` |  |
| modrinth | `modrinth.metadata_link_platforms` | `modrinth-metadata-link-platforms` | `GET /modrinth/metadata/link-platforms` | none | `ApiKeyAuth` | `ModrinthMetadataLinkPlatformsResponse` |  |
| modrinth | `modrinth.metadata_loader_fields` | `modrinth-metadata-loader-fields` | `GET /modrinth/metadata/loader-fields` | none | `ApiKeyAuth` | `ModrinthMetadataLoaderFieldsResponse` |  |
| modrinth | `modrinth.metadata_loader_field_values` | `modrinth-metadata-loader-field-values` | `GET /modrinth/metadata/loader-fields/{field}` | `field` (path String required) | `ApiKeyAuth` | `ModrinthMetadataLoaderFieldValuesResponse` |  |
| modrinth | `modrinth.metadata_loaders` | `modrinth-metadata-loaders` | `GET /modrinth/metadata/loaders` | none | `ApiKeyAuth` | `ModrinthMetadataLoadersResponse` |  |
| modrinth | `modrinth.organization` | `modrinth-organization` | `GET /modrinth/organization/{id}` | `id` (path String required) | `ApiKeyAuth` | `ModrinthOrganizationResponse` |  |
| modrinth | `modrinth.organization_projects` | `modrinth-organization-projects` | `GET /modrinth/organization/{id}/projects` | `id` (path String required) | `ApiKeyAuth` | `ModrinthOrganizationProjectsResponse` |  |
| modrinth | `modrinth.organizations` | `modrinth-organizations` | `GET /modrinth/organizations` | `ids` (query String required) | `ApiKeyAuth` | `ModrinthOrganizationsResponse` |  |
| modrinth | `modrinth.project` | `modrinth-project` | `GET /modrinth/project/{id}` | `id` (path String required) | `ApiKeyAuth` | `ModrinthProjectResponse` |  |
| modrinth | `modrinth.check_project` | `modrinth-check-project` | `GET /modrinth/project/{id}/check` | `id` (path String required) | `ApiKeyAuth` | `ModrinthCheckProjectResponse` |  |
| modrinth | `modrinth.dependencies` | `modrinth-dependencies` | `GET /modrinth/project/{id}/dependencies` | `id` (path String required) | `ApiKeyAuth` | `ModrinthDependenciesResponse` |  |
| modrinth | `modrinth.project_disclosures` | `modrinth-project-disclosures` | `GET /modrinth/project/{id}/disclosures` | `id` (path String required) | `ApiKeyAuth` | `ModrinthProjectDisclosuresResponse` |  |
| modrinth | `modrinth.project_versions` | `modrinth-project-versions` | `GET /modrinth/project/{id}/version` | `id` (path String required)<br>`loaders` (query String)<br>`game_versions` (query String)<br>`featured` (query bool)<br>`include_changelog` (query bool) | `ApiKeyAuth` | `ModrinthProjectVersionsResponse` |  |
| modrinth | `modrinth.project_version` | `modrinth-project-version` | `GET /modrinth/project/{id}/version/{number}` | `id` (path String required)<br>`number` (path String required) | `ApiKeyAuth` | `ModrinthProjectVersionResponse` |  |
| modrinth | `modrinth.projects` | `modrinth-projects` | `GET /modrinth/projects` | `ids` (query String required) | `ApiKeyAuth` | `ModrinthProjectsResponse` |  |
| modrinth | `modrinth.random_projects` | `modrinth-random-projects` | `GET /modrinth/projects_random` | `count` (query i64 required) | `ApiKeyAuth` | `ModrinthRandomProjectsResponse` |  |
| modrinth | `modrinth.search` | `modrinth-search` | `GET /modrinth/search` | `query` (query String)<br>`facets` (query String)<br>`index` (query String enum{relevance, downloads, follows, newest, updated})<br>`offset` (query i64)<br>`limit` (query i64) | `ApiKeyAuth` | `ModrinthSearchResponse` |  |
| modrinth | `modrinth.statistics` | `modrinth-statistics` | `GET /modrinth/statistics` | none | `ApiKeyAuth` | `ModrinthStatisticsResponse` |  |
| modrinth | `modrinth.license` | `modrinth-license` | `GET /modrinth/tag/license/{id}` | `id` (path String required) | `ApiKeyAuth` | `ModrinthLicenseResponse` |  |
| modrinth | `modrinth.tags` | `modrinth-tags` | `GET /modrinth/tag/{type}` | `type` (path String enum{category, loader, game_version, license, donation_platform, report_type, project_type, side_type} required) | `ApiKeyAuth` | `ModrinthTagsResponse` |  |
| modrinth | `modrinth.forge_updates` | `modrinth-forge-updates` | `GET /modrinth/updates/{id}/forge_updates.json` | `id` (path String required)<br>`neoforge` (query String enum{include, only}) | `ApiKeyAuth` | `ModrinthForgeUpdatesResponse` |  |
| modrinth | `modrinth.search_v3` | `modrinth-search-v3` | `GET /modrinth/v3/search` | `query` (query String)<br>`index` (query String enum{relevance, downloads, follows, newest, updated, date_created, date_modified, minecraft_java_server.verified_plays_2w, minecraft_java_server.ping.data.players_online})<br>`offset` (query i64)<br>`limit` (query i64)<br>`new_filters` (query String)<br>`facets` (query String)<br>`filters` (query String)<br>`version` (query String) | `ApiKeyAuth` | `ModrinthSearchV3Response` |  |
| modrinth | `modrinth.search_v3_body` | `modrinth-search-v3-body` | `POST /modrinth/v3/search` | `body` (body ModelModrinthSearchV3BodyRequest required) | `ApiKeyAuth` | `ModrinthSearchV3BodyResponse` |  |
| modrinth | `modrinth.search_v3_options` | `modrinth-search-v3-options` | `GET /modrinth/v3/search/options` | none | `ApiKeyAuth` | `ModrinthSearchV3OptionsResponse` |  |
| modrinth | `modrinth.version` | `modrinth-version` | `GET /modrinth/version/{id}` | `id` (path String required) | `ApiKeyAuth` | `ModrinthVersionResponse` |  |
| modrinth | `modrinth.file_projects` | `modrinth-file-projects` | `POST /modrinth/version_file/project` | `body` (body ModelModrinthHashesRequest required) | `ApiKeyAuth` | `ModrinthFileProjectsResponse` |  |
| modrinth | `modrinth.file_version` | `modrinth-file-version` | `GET /modrinth/version_file/{hash}` | `hash` (path String required)<br>`algorithm` (query String enum{sha1, sha512}) | `ApiKeyAuth` | `ModrinthFileVersionResponse` |  |
| modrinth | `modrinth.file_update` | `modrinth-file-update` | `POST /modrinth/version_file/{hash}/update` | `hash` (path String required)<br>`algorithm` (query String enum{sha1, sha512})<br>`body` (body ModelModrinthFiltersRequest required) | `ApiKeyAuth` | `ModrinthFileUpdateResponse` |  |
| modrinth | `modrinth.file_versions` | `modrinth-file-versions` | `POST /modrinth/version_files` | `body` (body ModelModrinthHashesRequest required) | `ApiKeyAuth` | `ModrinthFileVersionsResponse` |  |
| modrinth | `modrinth.files_update` | `modrinth-files-update` | `POST /modrinth/version_files/update` | `body` (body ModelModrinthHashUpdatesRequest required) | `ApiKeyAuth` | `ModrinthFilesUpdateResponse` |  |
| modrinth | `modrinth.files_update_individual` | `modrinth-files-update-individual` | `POST /modrinth/version_files/update_individual` | `body` (body ModelModrinthIndividualUpdatesRequest required) | `ApiKeyAuth` | `ModrinthFilesUpdateIndividualResponse` |  |
| modrinth | `modrinth.files_update_many` | `modrinth-files-update-many` | `POST /modrinth/version_files/update_many` | `body` (body ModelModrinthHashUpdatesRequest required) | `ApiKeyAuth` | `ModrinthFilesUpdateManyResponse` |  |
| modrinth | `modrinth.versions` | `modrinth-versions` | `GET /modrinth/versions` | `ids` (query String required) | `ApiKeyAuth` | `ModrinthVersionsResponse` |  |
