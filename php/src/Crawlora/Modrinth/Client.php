<?php

declare(strict_types=1);

namespace Crawlora\Modrinth;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'modrinth';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 34;
    public const OPERATION_IDS = ["modrinth-check-project", "modrinth-collection", "modrinth-collections", "modrinth-dependencies", "modrinth-file-projects", "modrinth-file-update", "modrinth-file-version", "modrinth-file-versions", "modrinth-files-update", "modrinth-files-update-individual", "modrinth-files-update-many", "modrinth-forge-updates", "modrinth-license", "modrinth-metadata-link-platforms", "modrinth-metadata-loader-field-values", "modrinth-metadata-loader-fields", "modrinth-metadata-loaders", "modrinth-organization", "modrinth-organization-projects", "modrinth-organizations", "modrinth-project", "modrinth-project-disclosures", "modrinth-project-version", "modrinth-project-versions", "modrinth-projects", "modrinth-random-projects", "modrinth-search", "modrinth-search-v3", "modrinth-search-v3-body", "modrinth-search-v3-options", "modrinth-statistics", "modrinth-tags", "modrinth-version", "modrinth-versions"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"modrinth-check-project": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-check-project", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/check", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-collection": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-collection", "method": "GET", "params": [{"description": "Base62 collection ID from a public collection URL", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/collection/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-collections": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-collections", "method": "GET", "params": [{"description": "Native JSON array of base62 collection IDs; [] is valid", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-dependencies": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-dependencies", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/dependencies", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-file-projects": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-projects", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashesRequest"}}], "path": "/modrinth/version_file/project", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-file-update": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-update", "method": "POST", "params": [{"description": "Native hash", "in": "path", "name": "hash", "required": true, "type": "string"}, {"description": "File-hash algorithm; omitted uses native auto-detection", "enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}, {"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.FiltersRequest"}}], "path": "/modrinth/version_file/{hash}/update", "pathParams": ["hash"], "produces": ["application/json"], "queryParams": [{"enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-file-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-file-version", "method": "GET", "params": [{"description": "Native hash", "in": "path", "name": "hash", "required": true, "type": "string"}, {"description": "File-hash algorithm; omitted uses native auto-detection", "enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "path": "/modrinth/version_file/{hash}", "pathParams": ["hash"], "produces": ["application/json"], "queryParams": [{"enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-file-versions": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-versions", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashesRequest"}}], "path": "/modrinth/version_files", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashUpdatesRequest"}}], "path": "/modrinth/version_files/update", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update-individual": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update-individual", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.IndividualUpdatesRequest"}}], "path": "/modrinth/version_files/update_individual", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update-many": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update-many", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashUpdatesRequest"}}], "path": "/modrinth/version_files/update_many", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-forge-updates": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-forge-updates", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native NeoForge selection; omitted retains Forge default", "enum": ["include", "only"], "in": "query", "name": "neoforge", "type": "string"}], "path": "/modrinth/updates/{id}/forge_updates.json", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["include", "only"], "in": "query", "name": "neoforge", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-license": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-license", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/tag/license/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-link-platforms": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-link-platforms", "method": "GET", "params": [], "path": "/modrinth/metadata/link-platforms", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loader-field-values": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loader-field-values", "method": "GET", "params": [{"description": "Source field name from loader-field discovery", "in": "path", "name": "field", "required": true, "type": "string"}], "path": "/modrinth/metadata/loader-fields/{field}", "pathParams": ["field"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loader-fields": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loader-fields", "method": "GET", "params": [], "path": "/modrinth/metadata/loader-fields", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loaders": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loaders", "method": "GET", "params": [], "path": "/modrinth/metadata/loaders", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organization": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organization", "method": "GET", "params": [{"description": "Organization ID or slug from a public organization URL or project metadata", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/organization/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organization-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organization-projects", "method": "GET", "params": [{"description": "Organization ID or slug from a public organization URL or project metadata", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/organization/{id}/projects", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organizations": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organizations", "method": "GET", "params": [{"description": "Native JSON array of organization IDs or slugs; [] is valid", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/organizations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-project": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-disclosures": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-disclosures", "method": "GET", "params": [{"description": "Native project ID or canonical slug", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/disclosures", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-version", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native number", "in": "path", "name": "number", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/version/{number}", "pathParams": ["id", "number"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-versions": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-versions", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "JSON array of loader names from the loader tag catalog", "in": "query", "name": "loaders", "type": "string"}, {"description": "JSON array of game versions from the game_version tag catalog", "in": "query", "name": "game_versions", "type": "string"}, {"description": "Native featured selector; false is distinct from omission", "in": "query", "name": "featured", "type": "boolean"}, {"default": true, "description": "Include changelog fields", "in": "query", "name": "include_changelog", "type": "boolean"}], "path": "/modrinth/project/{id}/version", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "loaders", "type": "string"}, {"in": "query", "name": "game_versions", "type": "string"}, {"in": "query", "name": "featured", "type": "boolean"}, {"in": "query", "name": "include_changelog", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "modrinth-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-projects", "method": "GET", "params": [{"description": "JSON-encoded array of native identifiers; absent members are omitted", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/projects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-random-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-random-projects", "method": "GET", "params": [{"description": "Number of random projects, 1 to 100", "in": "query", "name": "count", "required": true, "type": "integer"}], "path": "/modrinth/projects_random", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "modrinth-search": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search", "method": "GET", "params": [{"description": "Search text", "in": "query", "name": "query", "type": "string"}, {"description": "Native JSON array of OR groups joined by AND; see the full facet reference", "in": "query", "name": "facets", "type": "string"}, {"description": "Native search order", "enum": ["relevance", "downloads", "follows", "newest", "updated"], "in": "query", "name": "index", "type": "string"}, {"default": 0, "description": "Native result offset, at least zero", "in": "query", "name": "offset", "type": "integer"}, {"default": 10, "description": "Native result limit, zero to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/modrinth/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "facets", "type": "string"}, {"enum": ["relevance", "downloads", "follows", "newest", "updated"], "in": "query", "name": "index", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "modrinth-search-v3": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search-v3", "method": "GET", "params": [{"description": "Native search text", "in": "query", "name": "query", "type": "string"}, {"description": "Native v3 order", "enum": ["relevance", "downloads", "follows", "newest", "updated", "date_created", "date_modified", "minecraft_java_server.verified_plays_2w", "minecraft_java_server.ping.data.players_online"], "in": "query", "name": "index", "type": "string"}, {"description": "Native nonnegative offset; default0", "in": "query", "name": "offset", "type": "integer"}, {"description": "Native nonnegative limit; default10; source normalizes to1–100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Native current filter expression, forwarded unchanged", "in": "query", "name": "new_filters", "type": "string"}, {"description": "Legacy JSON array of string arrays using v3 field names", "in": "query", "name": "facets", "type": "string"}, {"description": "Legacy filter-expression clause", "in": "query", "name": "filters", "type": "string"}, {"description": "Legacy secondary filter-expression clause", "in": "query", "name": "version", "type": "string"}], "path": "/modrinth/v3/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"enum": ["relevance", "downloads", "follows", "newest", "updated", "date_created", "date_modified", "minecraft_java_server.verified_plays_2w", "minecraft_java_server.ping.data.players_online"], "in": "query", "name": "index", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "new_filters", "type": "string"}, {"in": "query", "name": "facets", "type": "string"}, {"in": "query", "name": "filters", "type": "string"}, {"in": "query", "name": "version", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-search-v3-body": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-search-v3-body", "method": "POST", "params": [{"description": "Native search body; offset/limit are strings", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.SearchV3BodyRequest"}}], "path": "/modrinth/v3/search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-search-v3-options": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search-v3-options", "method": "GET", "params": [], "path": "/modrinth/v3/search/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-statistics": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-statistics", "method": "GET", "params": [], "path": "/modrinth/statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-tags": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-tags", "method": "GET", "params": [{"description": "Native type", "enum": ["category", "loader", "game_version", "license", "donation_platform", "report_type", "project_type", "side_type"], "in": "path", "name": "type", "required": true, "type": "string"}], "path": "/modrinth/tag/{type}", "pathParams": ["type"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-version", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/version/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-versions": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-versions", "method": "GET", "params": [{"description": "JSON-encoded array of native identifiers; absent members are omitted", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/versions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-modrinth-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function collection(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-collection", $params, $responseType);
    }
    public function collections(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-collections", $params, $responseType);
    }
    public function metadata_link_platforms(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-metadata-link-platforms", $params, $responseType);
    }
    public function metadata_loader_fields(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-metadata-loader-fields", $params, $responseType);
    }
    public function metadata_loader_field_values(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-metadata-loader-field-values", $params, $responseType);
    }
    public function metadata_loaders(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-metadata-loaders", $params, $responseType);
    }
    public function organization(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-organization", $params, $responseType);
    }
    public function organization_projects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-organization-projects", $params, $responseType);
    }
    public function organizations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-organizations", $params, $responseType);
    }
    public function project(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-project", $params, $responseType);
    }
    public function check_project(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-check-project", $params, $responseType);
    }
    public function dependencies(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-dependencies", $params, $responseType);
    }
    public function project_disclosures(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-project-disclosures", $params, $responseType);
    }
    public function project_versions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-project-versions", $params, $responseType);
    }
    public function project_version(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-project-version", $params, $responseType);
    }
    public function projects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-projects", $params, $responseType);
    }
    public function random_projects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-random-projects", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-search", $params, $responseType);
    }
    public function statistics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-statistics", $params, $responseType);
    }
    public function license(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-license", $params, $responseType);
    }
    public function tags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-tags", $params, $responseType);
    }
    public function forge_updates(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-forge-updates", $params, $responseType);
    }
    public function search_v3(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-search-v3", $params, $responseType);
    }
    public function search_v3_body(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-search-v3-body", $params, $responseType);
    }
    public function search_v3_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-search-v3-options", $params, $responseType);
    }
    public function version(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-version", $params, $responseType);
    }
    public function file_projects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-file-projects", $params, $responseType);
    }
    public function file_version(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-file-version", $params, $responseType);
    }
    public function file_update(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-file-update", $params, $responseType);
    }
    public function file_versions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-file-versions", $params, $responseType);
    }
    public function files_update(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-files-update", $params, $responseType);
    }
    public function files_update_individual(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-files-update-individual", $params, $responseType);
    }
    public function files_update_many(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-files-update-many", $params, $responseType);
    }
    public function versions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("modrinth-versions", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
