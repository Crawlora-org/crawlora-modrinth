import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class ModrinthClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-modrinth-js/0.1.0" });
    this["collection"] = (...args) => this.request("modrinth-collection", ...args);
    this["collections"] = (...args) => this.request("modrinth-collections", ...args);
    this["metadataLinkPlatforms"] = (...args) => this.request("modrinth-metadata-link-platforms", ...args);
    this["metadataLoaderFields"] = (...args) => this.request("modrinth-metadata-loader-fields", ...args);
    this["metadataLoaderFieldValues"] = (...args) => this.request("modrinth-metadata-loader-field-values", ...args);
    this["metadataLoaders"] = (...args) => this.request("modrinth-metadata-loaders", ...args);
    this["organization"] = (...args) => this.request("modrinth-organization", ...args);
    this["organizationProjects"] = (...args) => this.request("modrinth-organization-projects", ...args);
    this["organizations"] = (...args) => this.request("modrinth-organizations", ...args);
    this["project"] = (...args) => this.request("modrinth-project", ...args);
    this["checkProject"] = (...args) => this.request("modrinth-check-project", ...args);
    this["dependencies"] = (...args) => this.request("modrinth-dependencies", ...args);
    this["projectDisclosures"] = (...args) => this.request("modrinth-project-disclosures", ...args);
    this["projectVersions"] = (...args) => this.request("modrinth-project-versions", ...args);
    this["projectVersion"] = (...args) => this.request("modrinth-project-version", ...args);
    this["projects"] = (...args) => this.request("modrinth-projects", ...args);
    this["randomProjects"] = (...args) => this.request("modrinth-random-projects", ...args);
    this["search"] = (...args) => this.request("modrinth-search", ...args);
    this["statistics"] = (...args) => this.request("modrinth-statistics", ...args);
    this["license"] = (...args) => this.request("modrinth-license", ...args);
    this["tags"] = (...args) => this.request("modrinth-tags", ...args);
    this["forgeUpdates"] = (...args) => this.request("modrinth-forge-updates", ...args);
    this["searchV3"] = (...args) => this.request("modrinth-search-v3", ...args);
    this["searchV3Body"] = (...args) => this.request("modrinth-search-v3-body", ...args);
    this["searchV3Options"] = (...args) => this.request("modrinth-search-v3-options", ...args);
    this["version"] = (...args) => this.request("modrinth-version", ...args);
    this["fileProjects"] = (...args) => this.request("modrinth-file-projects", ...args);
    this["fileVersion"] = (...args) => this.request("modrinth-file-version", ...args);
    this["fileUpdate"] = (...args) => this.request("modrinth-file-update", ...args);
    this["fileVersions"] = (...args) => this.request("modrinth-file-versions", ...args);
    this["filesUpdate"] = (...args) => this.request("modrinth-files-update", ...args);
    this["filesUpdateIndividual"] = (...args) => this.request("modrinth-files-update-individual", ...args);
    this["filesUpdateMany"] = (...args) => this.request("modrinth-files-update-many", ...args);
    this["versions"] = (...args) => this.request("modrinth-versions", ...args);
  }
}

export { ModrinthClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default ModrinthClient;
