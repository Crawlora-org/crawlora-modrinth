require "json"
require "net/http"
require "uri"

module Crawlora
  module Modrinth
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"modrinth-check-project": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-check-project", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/check", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-collection": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-collection", "method": "GET", "params": [{"description": "Base62 collection ID from a public collection URL", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/collection/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-collections": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-collections", "method": "GET", "params": [{"description": "Native JSON array of base62 collection IDs; [] is valid", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-dependencies": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-dependencies", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/dependencies", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-file-projects": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-projects", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashesRequest"}}], "path": "/modrinth/version_file/project", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-file-update": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-update", "method": "POST", "params": [{"description": "Native hash", "in": "path", "name": "hash", "required": true, "type": "string"}, {"description": "File-hash algorithm; omitted uses native auto-detection", "enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}, {"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.FiltersRequest"}}], "path": "/modrinth/version_file/{hash}/update", "pathParams": ["hash"], "produces": ["application/json"], "queryParams": [{"enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-file-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-file-version", "method": "GET", "params": [{"description": "Native hash", "in": "path", "name": "hash", "required": true, "type": "string"}, {"description": "File-hash algorithm; omitted uses native auto-detection", "enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "path": "/modrinth/version_file/{hash}", "pathParams": ["hash"], "produces": ["application/json"], "queryParams": [{"enum": ["sha1", "sha512"], "in": "query", "name": "algorithm", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-file-versions": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-file-versions", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashesRequest"}}], "path": "/modrinth/version_files", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashUpdatesRequest"}}], "path": "/modrinth/version_files/update", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update-individual": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update-individual", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.IndividualUpdatesRequest"}}], "path": "/modrinth/version_files/update_individual", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-files-update-many": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-files-update-many", "method": "POST", "params": [{"description": "Native metadata lookup body", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.HashUpdatesRequest"}}], "path": "/modrinth/version_files/update_many", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-forge-updates": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-forge-updates", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native NeoForge selection; omitted retains Forge default", "enum": ["include", "only"], "in": "query", "name": "neoforge", "type": "string"}], "path": "/modrinth/updates/{id}/forge_updates.json", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["include", "only"], "in": "query", "name": "neoforge", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-license": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-license", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/tag/license/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-link-platforms": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-link-platforms", "method": "GET", "params": [], "path": "/modrinth/metadata/link-platforms", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loader-field-values": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loader-field-values", "method": "GET", "params": [{"description": "Source field name from loader-field discovery", "in": "path", "name": "field", "required": true, "type": "string"}], "path": "/modrinth/metadata/loader-fields/{field}", "pathParams": ["field"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loader-fields": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loader-fields", "method": "GET", "params": [], "path": "/modrinth/metadata/loader-fields", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-metadata-loaders": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-metadata-loaders", "method": "GET", "params": [], "path": "/modrinth/metadata/loaders", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organization": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organization", "method": "GET", "params": [{"description": "Organization ID or slug from a public organization URL or project metadata", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/organization/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organization-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organization-projects", "method": "GET", "params": [{"description": "Organization ID or slug from a public organization URL or project metadata", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/organization/{id}/projects", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-organizations": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-organizations", "method": "GET", "params": [{"description": "Native JSON array of organization IDs or slugs; [] is valid", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/organizations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-project": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-disclosures": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-disclosures", "method": "GET", "params": [{"description": "Native project ID or canonical slug", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/disclosures", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-version", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "Native number", "in": "path", "name": "number", "required": true, "type": "string"}], "path": "/modrinth/project/{id}/version/{number}", "pathParams": ["id", "number"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-project-versions": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-project-versions", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}, {"description": "JSON array of loader names from the loader tag catalog", "in": "query", "name": "loaders", "type": "string"}, {"description": "JSON array of game versions from the game_version tag catalog", "in": "query", "name": "game_versions", "type": "string"}, {"description": "Native featured selector; false is distinct from omission", "in": "query", "name": "featured", "type": "boolean"}, {"default": true, "description": "Include changelog fields", "in": "query", "name": "include_changelog", "type": "boolean"}], "path": "/modrinth/project/{id}/version", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "loaders", "type": "string"}, {"in": "query", "name": "game_versions", "type": "string"}, {"in": "query", "name": "featured", "type": "boolean"}, {"in": "query", "name": "include_changelog", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "modrinth-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-projects", "method": "GET", "params": [{"description": "JSON-encoded array of native identifiers; absent members are omitted", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/projects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-random-projects": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-random-projects", "method": "GET", "params": [{"description": "Number of random projects, 1 to 100", "in": "query", "name": "count", "required": true, "type": "integer"}], "path": "/modrinth/projects_random", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "modrinth-search": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search", "method": "GET", "params": [{"description": "Search text", "in": "query", "name": "query", "type": "string"}, {"description": "Native JSON array of OR groups joined by AND; see the full facet reference", "in": "query", "name": "facets", "type": "string"}, {"description": "Native search order", "enum": ["relevance", "downloads", "follows", "newest", "updated"], "in": "query", "name": "index", "type": "string"}, {"default": 0, "description": "Native result offset, at least zero", "in": "query", "name": "offset", "type": "integer"}, {"default": 10, "description": "Native result limit, zero to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/modrinth/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "facets", "type": "string"}, {"enum": ["relevance", "downloads", "follows", "newest", "updated"], "in": "query", "name": "index", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "modrinth-search-v3": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search-v3", "method": "GET", "params": [{"description": "Native search text", "in": "query", "name": "query", "type": "string"}, {"description": "Native v3 order", "enum": ["relevance", "downloads", "follows", "newest", "updated", "date_created", "date_modified", "minecraft_java_server.verified_plays_2w", "minecraft_java_server.ping.data.players_online"], "in": "query", "name": "index", "type": "string"}, {"description": "Native nonnegative offset; default0", "in": "query", "name": "offset", "type": "integer"}, {"description": "Native nonnegative limit; default10; source normalizes to1–100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Native current filter expression, forwarded unchanged", "in": "query", "name": "new_filters", "type": "string"}, {"description": "Legacy JSON array of string arrays using v3 field names", "in": "query", "name": "facets", "type": "string"}, {"description": "Legacy filter-expression clause", "in": "query", "name": "filters", "type": "string"}, {"description": "Legacy secondary filter-expression clause", "in": "query", "name": "version", "type": "string"}], "path": "/modrinth/v3/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"enum": ["relevance", "downloads", "follows", "newest", "updated", "date_created", "date_modified", "minecraft_java_server.verified_plays_2w", "minecraft_java_server.ping.data.players_online"], "in": "query", "name": "index", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "new_filters", "type": "string"}, {"in": "query", "name": "facets", "type": "string"}, {"in": "query", "name": "filters", "type": "string"}, {"in": "query", "name": "version", "type": "string"}], "security": ["ApiKeyAuth"]}, "modrinth-search-v3-body": {"bodyParam": "body", "bodyRequired": true, "id": "modrinth-search-v3-body", "method": "POST", "params": [{"description": "Native search body; offset/limit are strings", "in": "body", "name": "body", "required": true, "schema": {"$ref": "#/definitions/modrinth.SearchV3BodyRequest"}}], "path": "/modrinth/v3/search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-search-v3-options": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-search-v3-options", "method": "GET", "params": [], "path": "/modrinth/v3/search/options", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-statistics": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-statistics", "method": "GET", "params": [], "path": "/modrinth/statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-tags": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-tags", "method": "GET", "params": [{"description": "Native type", "enum": ["category", "loader", "game_version", "license", "donation_platform", "report_type", "project_type", "side_type"], "in": "path", "name": "type", "required": true, "type": "string"}], "path": "/modrinth/tag/{type}", "pathParams": ["type"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-version": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-version", "method": "GET", "params": [{"description": "Native id", "in": "path", "name": "id", "required": true, "type": "string"}], "path": "/modrinth/version/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "modrinth-versions": {"bodyParam": null, "bodyRequired": false, "id": "modrinth-versions", "method": "GET", "params": [{"description": "JSON-encoded array of native identifiers; absent members are omitted", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/modrinth/versions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["modrinth-check-project", "modrinth-collection", "modrinth-collections", "modrinth-dependencies", "modrinth-file-projects", "modrinth-file-update", "modrinth-file-version", "modrinth-file-versions", "modrinth-files-update", "modrinth-files-update-individual", "modrinth-files-update-many", "modrinth-forge-updates", "modrinth-license", "modrinth-metadata-link-platforms", "modrinth-metadata-loader-field-values", "modrinth-metadata-loader-fields", "modrinth-metadata-loaders", "modrinth-organization", "modrinth-organization-projects", "modrinth-organizations", "modrinth-project", "modrinth-project-disclosures", "modrinth-project-version", "modrinth-project-versions", "modrinth-projects", "modrinth-random-projects", "modrinth-search", "modrinth-search-v3", "modrinth-search-v3-body", "modrinth-search-v3-options", "modrinth-statistics", "modrinth-tags", "modrinth-version", "modrinth-versions"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-modrinth-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('collection') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-collection', params, response_type: response_type)
      end
      define_method('collections') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-collections', params, response_type: response_type)
      end
      define_method('metadata_link_platforms') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-metadata-link-platforms', params, response_type: response_type)
      end
      define_method('metadata_loader_fields') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-metadata-loader-fields', params, response_type: response_type)
      end
      define_method('metadata_loader_field_values') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-metadata-loader-field-values', params, response_type: response_type)
      end
      define_method('metadata_loaders') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-metadata-loaders', params, response_type: response_type)
      end
      define_method('organization') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-organization', params, response_type: response_type)
      end
      define_method('organization_projects') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-organization-projects', params, response_type: response_type)
      end
      define_method('organizations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-organizations', params, response_type: response_type)
      end
      define_method('project') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-project', params, response_type: response_type)
      end
      define_method('check_project') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-check-project', params, response_type: response_type)
      end
      define_method('dependencies') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-dependencies', params, response_type: response_type)
      end
      define_method('project_disclosures') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-project-disclosures', params, response_type: response_type)
      end
      define_method('project_versions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-project-versions', params, response_type: response_type)
      end
      define_method('project_version') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-project-version', params, response_type: response_type)
      end
      define_method('projects') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-projects', params, response_type: response_type)
      end
      define_method('random_projects') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-random-projects', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-search', params, response_type: response_type)
      end
      define_method('statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-statistics', params, response_type: response_type)
      end
      define_method('license') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-license', params, response_type: response_type)
      end
      define_method('tags') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-tags', params, response_type: response_type)
      end
      define_method('forge_updates') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-forge-updates', params, response_type: response_type)
      end
      define_method('search_v3') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-search-v3', params, response_type: response_type)
      end
      define_method('search_v3_body') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-search-v3-body', params, response_type: response_type)
      end
      define_method('search_v3_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-search-v3-options', params, response_type: response_type)
      end
      define_method('version') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-version', params, response_type: response_type)
      end
      define_method('file_projects') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-file-projects', params, response_type: response_type)
      end
      define_method('file_version') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-file-version', params, response_type: response_type)
      end
      define_method('file_update') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-file-update', params, response_type: response_type)
      end
      define_method('file_versions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-file-versions', params, response_type: response_type)
      end
      define_method('files_update') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-files-update', params, response_type: response_type)
      end
      define_method('files_update_individual') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-files-update-individual', params, response_type: response_type)
      end
      define_method('files_update_many') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-files-update-many', params, response_type: response_type)
      end
      define_method('versions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('modrinth-versions', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
