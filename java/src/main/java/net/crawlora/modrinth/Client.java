package net.crawlora.modrinth;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Modrinth endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 34;
    public static final List<String> OPERATION_IDS = List.of(
            "modrinth-check-project",
            "modrinth-collection",
            "modrinth-collections",
            "modrinth-dependencies",
            "modrinth-file-projects",
            "modrinth-file-update",
            "modrinth-file-version",
            "modrinth-file-versions",
            "modrinth-files-update",
            "modrinth-files-update-individual",
            "modrinth-files-update-many",
            "modrinth-forge-updates",
            "modrinth-license",
            "modrinth-metadata-link-platforms",
            "modrinth-metadata-loader-field-values",
            "modrinth-metadata-loader-fields",
            "modrinth-metadata-loaders",
            "modrinth-organization",
            "modrinth-organization-projects",
            "modrinth-organizations",
            "modrinth-project",
            "modrinth-project-disclosures",
            "modrinth-project-version",
            "modrinth-project-versions",
            "modrinth-projects",
            "modrinth-random-projects",
            "modrinth-search",
            "modrinth-search-v3",
            "modrinth-search-v3-body",
            "modrinth-search-v3-options",
            "modrinth-statistics",
            "modrinth-tags",
            "modrinth-version",
            "modrinth-versions"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("modrinth-collection", new Operation("modrinth-collection", "GET", "/modrinth/collection/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-collections", new Operation("modrinth-collections", "GET", "/modrinth/collections", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-metadata-link-platforms", new Operation("modrinth-metadata-link-platforms", "GET", "/modrinth/metadata/link-platforms", Map.of(), List.of("application/json")));
        operations.put("modrinth-metadata-loader-fields", new Operation("modrinth-metadata-loader-fields", "GET", "/modrinth/metadata/loader-fields", Map.of(), List.of("application/json")));
        operations.put("modrinth-metadata-loader-field-values", new Operation("modrinth-metadata-loader-field-values", "GET", "/modrinth/metadata/loader-fields/{field}", Map.ofEntries(Map.entry("field", new Param("field", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-metadata-loaders", new Operation("modrinth-metadata-loaders", "GET", "/modrinth/metadata/loaders", Map.of(), List.of("application/json")));
        operations.put("modrinth-organization", new Operation("modrinth-organization", "GET", "/modrinth/organization/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-organization-projects", new Operation("modrinth-organization-projects", "GET", "/modrinth/organization/{id}/projects", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-organizations", new Operation("modrinth-organizations", "GET", "/modrinth/organizations", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-project", new Operation("modrinth-project", "GET", "/modrinth/project/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-check-project", new Operation("modrinth-check-project", "GET", "/modrinth/project/{id}/check", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-dependencies", new Operation("modrinth-dependencies", "GET", "/modrinth/project/{id}/dependencies", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-project-disclosures", new Operation("modrinth-project-disclosures", "GET", "/modrinth/project/{id}/disclosures", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-project-versions", new Operation("modrinth-project-versions", "GET", "/modrinth/project/{id}/version", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("loaders", new Param("loaders", "query", false, "string", List.of(), "csv")), Map.entry("game_versions", new Param("game_versions", "query", false, "string", List.of(), "csv")), Map.entry("featured", new Param("featured", "query", false, "boolean", List.of(), "csv")), Map.entry("include_changelog", new Param("include_changelog", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-project-version", new Operation("modrinth-project-version", "GET", "/modrinth/project/{id}/version/{number}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("number", new Param("number", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-projects", new Operation("modrinth-projects", "GET", "/modrinth/projects", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-random-projects", new Operation("modrinth-random-projects", "GET", "/modrinth/projects_random", Map.ofEntries(Map.entry("count", new Param("count", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-search", new Operation("modrinth-search", "GET", "/modrinth/search", Map.ofEntries(Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("facets", new Param("facets", "query", false, "string", List.of(), "csv")), Map.entry("index", new Param("index", "query", false, "string", List.of("relevance", "downloads", "follows", "newest", "updated"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-statistics", new Operation("modrinth-statistics", "GET", "/modrinth/statistics", Map.of(), List.of("application/json")));
        operations.put("modrinth-license", new Operation("modrinth-license", "GET", "/modrinth/tag/license/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-tags", new Operation("modrinth-tags", "GET", "/modrinth/tag/{type}", Map.ofEntries(Map.entry("type", new Param("type", "path", true, "string", List.of("category", "loader", "game_version", "license", "donation_platform", "report_type", "project_type", "side_type"), "csv"))), List.of("application/json")));
        operations.put("modrinth-forge-updates", new Operation("modrinth-forge-updates", "GET", "/modrinth/updates/{id}/forge_updates.json", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("neoforge", new Param("neoforge", "query", false, "string", List.of("include", "only"), "csv"))), List.of("application/json")));
        operations.put("modrinth-search-v3", new Operation("modrinth-search-v3", "GET", "/modrinth/v3/search", Map.ofEntries(Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("index", new Param("index", "query", false, "string", List.of("relevance", "downloads", "follows", "newest", "updated", "date_created", "date_modified", "minecraft_java_server.verified_plays_2w", "minecraft_java_server.ping.data.players_online"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("new_filters", new Param("new_filters", "query", false, "string", List.of(), "csv")), Map.entry("facets", new Param("facets", "query", false, "string", List.of(), "csv")), Map.entry("filters", new Param("filters", "query", false, "string", List.of(), "csv")), Map.entry("version", new Param("version", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-search-v3-body", new Operation("modrinth-search-v3-body", "POST", "/modrinth/v3/search", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-search-v3-options", new Operation("modrinth-search-v3-options", "GET", "/modrinth/v3/search/options", Map.of(), List.of("application/json")));
        operations.put("modrinth-version", new Operation("modrinth-version", "GET", "/modrinth/version/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("modrinth-file-projects", new Operation("modrinth-file-projects", "POST", "/modrinth/version_file/project", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-file-version", new Operation("modrinth-file-version", "GET", "/modrinth/version_file/{hash}", Map.ofEntries(Map.entry("hash", new Param("hash", "path", true, "string", List.of(), "csv")), Map.entry("algorithm", new Param("algorithm", "query", false, "string", List.of("sha1", "sha512"), "csv"))), List.of("application/json")));
        operations.put("modrinth-file-update", new Operation("modrinth-file-update", "POST", "/modrinth/version_file/{hash}/update", Map.ofEntries(Map.entry("hash", new Param("hash", "path", true, "string", List.of(), "csv")), Map.entry("algorithm", new Param("algorithm", "query", false, "string", List.of("sha1", "sha512"), "csv"))), List.of("application/json"), "body"));
        operations.put("modrinth-file-versions", new Operation("modrinth-file-versions", "POST", "/modrinth/version_files", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-files-update", new Operation("modrinth-files-update", "POST", "/modrinth/version_files/update", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-files-update-individual", new Operation("modrinth-files-update-individual", "POST", "/modrinth/version_files/update_individual", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-files-update-many", new Operation("modrinth-files-update-many", "POST", "/modrinth/version_files/update_many", Map.of(), List.of("application/json"), "body"));
        operations.put("modrinth-versions", new Operation("modrinth-versions", "GET", "/modrinth/versions", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Modrinth operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object collection(Map<String, ?> params) { return request("modrinth-collection", params); }
    public Object collections(Map<String, ?> params) { return request("modrinth-collections", params); }
    public Object metadataLinkPlatforms(Map<String, ?> params) { return request("modrinth-metadata-link-platforms", params); }
    public Object metadataLoaderFields(Map<String, ?> params) { return request("modrinth-metadata-loader-fields", params); }
    public Object metadataLoaderFieldValues(Map<String, ?> params) { return request("modrinth-metadata-loader-field-values", params); }
    public Object metadataLoaders(Map<String, ?> params) { return request("modrinth-metadata-loaders", params); }
    public Object organization(Map<String, ?> params) { return request("modrinth-organization", params); }
    public Object organizationProjects(Map<String, ?> params) { return request("modrinth-organization-projects", params); }
    public Object organizations(Map<String, ?> params) { return request("modrinth-organizations", params); }
    public Object project(Map<String, ?> params) { return request("modrinth-project", params); }
    public Object checkProject(Map<String, ?> params) { return request("modrinth-check-project", params); }
    public Object dependencies(Map<String, ?> params) { return request("modrinth-dependencies", params); }
    public Object projectDisclosures(Map<String, ?> params) { return request("modrinth-project-disclosures", params); }
    public Object projectVersions(Map<String, ?> params) { return request("modrinth-project-versions", params); }
    public Object projectVersion(Map<String, ?> params) { return request("modrinth-project-version", params); }
    public Object projects(Map<String, ?> params) { return request("modrinth-projects", params); }
    public Object randomProjects(Map<String, ?> params) { return request("modrinth-random-projects", params); }
    public Object search(Map<String, ?> params) { return request("modrinth-search", params); }
    public Object statistics(Map<String, ?> params) { return request("modrinth-statistics", params); }
    public Object license(Map<String, ?> params) { return request("modrinth-license", params); }
    public Object tags(Map<String, ?> params) { return request("modrinth-tags", params); }
    public Object forgeUpdates(Map<String, ?> params) { return request("modrinth-forge-updates", params); }
    public Object searchV3(Map<String, ?> params) { return request("modrinth-search-v3", params); }
    public Object searchV3Body(Map<String, ?> params) { return request("modrinth-search-v3-body", params); }
    public Object searchV3Options(Map<String, ?> params) { return request("modrinth-search-v3-options", params); }
    public Object version(Map<String, ?> params) { return request("modrinth-version", params); }
    public Object fileProjects(Map<String, ?> params) { return request("modrinth-file-projects", params); }
    public Object fileVersion(Map<String, ?> params) { return request("modrinth-file-version", params); }
    public Object fileUpdate(Map<String, ?> params) { return request("modrinth-file-update", params); }
    public Object fileVersions(Map<String, ?> params) { return request("modrinth-file-versions", params); }
    public Object filesUpdate(Map<String, ?> params) { return request("modrinth-files-update", params); }
    public Object filesUpdateIndividual(Map<String, ?> params) { return request("modrinth-files-update-individual", params); }
    public Object filesUpdateMany(Map<String, ?> params) { return request("modrinth-files-update-many", params); }
    public Object versions(Map<String, ?> params) { return request("modrinth-versions", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
