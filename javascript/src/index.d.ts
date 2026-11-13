import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class ModrinthClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collection(params: OperationParamsMap["modrinth-collection"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collections(params: OperationParamsMap["modrinth-collections"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  metadataLinkPlatforms(params?: OperationParamsMap["modrinth-metadata-link-platforms"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  metadataLoaderFields(params?: OperationParamsMap["modrinth-metadata-loader-fields"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  metadataLoaderFieldValues(params: OperationParamsMap["modrinth-metadata-loader-field-values"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  metadataLoaders(params?: OperationParamsMap["modrinth-metadata-loaders"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  organization(params: OperationParamsMap["modrinth-organization"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  organizationProjects(params: OperationParamsMap["modrinth-organization-projects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  organizations(params: OperationParamsMap["modrinth-organizations"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  project(params: OperationParamsMap["modrinth-project"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  checkProject(params: OperationParamsMap["modrinth-check-project"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  dependencies(params: OperationParamsMap["modrinth-dependencies"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  projectDisclosures(params: OperationParamsMap["modrinth-project-disclosures"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  projectVersions(params: OperationParamsMap["modrinth-project-versions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  projectVersion(params: OperationParamsMap["modrinth-project-version"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  projects(params: OperationParamsMap["modrinth-projects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  randomProjects(params: OperationParamsMap["modrinth-random-projects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params?: OperationParamsMap["modrinth-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  statistics(params?: OperationParamsMap["modrinth-statistics"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  license(params: OperationParamsMap["modrinth-license"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tags(params: OperationParamsMap["modrinth-tags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  forgeUpdates(params: OperationParamsMap["modrinth-forge-updates"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchV3(params?: OperationParamsMap["modrinth-search-v3"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchV3Body(params: OperationParamsMap["modrinth-search-v3-body"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchV3Options(params?: OperationParamsMap["modrinth-search-v3-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  version(params: OperationParamsMap["modrinth-version"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fileProjects(params: OperationParamsMap["modrinth-file-projects"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fileVersion(params: OperationParamsMap["modrinth-file-version"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fileUpdate(params: OperationParamsMap["modrinth-file-update"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fileVersions(params: OperationParamsMap["modrinth-file-versions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  filesUpdate(params: OperationParamsMap["modrinth-files-update"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  filesUpdateIndividual(params: OperationParamsMap["modrinth-files-update-individual"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  filesUpdateMany(params: OperationParamsMap["modrinth-files-update-many"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  versions(params: OperationParamsMap["modrinth-versions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collection(params: OperationParamsMap["modrinth-collection"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collections(params: OperationParamsMap["modrinth-collections"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  metadataLinkPlatforms(params?: OperationParamsMap["modrinth-metadata-link-platforms"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  metadataLoaderFields(params?: OperationParamsMap["modrinth-metadata-loader-fields"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  metadataLoaderFieldValues(params: OperationParamsMap["modrinth-metadata-loader-field-values"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  metadataLoaders(params?: OperationParamsMap["modrinth-metadata-loaders"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  organization(params: OperationParamsMap["modrinth-organization"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  organizationProjects(params: OperationParamsMap["modrinth-organization-projects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  organizations(params: OperationParamsMap["modrinth-organizations"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  project(params: OperationParamsMap["modrinth-project"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  checkProject(params: OperationParamsMap["modrinth-check-project"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  dependencies(params: OperationParamsMap["modrinth-dependencies"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  projectDisclosures(params: OperationParamsMap["modrinth-project-disclosures"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  projectVersions(params: OperationParamsMap["modrinth-project-versions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  projectVersion(params: OperationParamsMap["modrinth-project-version"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  projects(params: OperationParamsMap["modrinth-projects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  randomProjects(params: OperationParamsMap["modrinth-random-projects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params?: OperationParamsMap["modrinth-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  statistics(params?: OperationParamsMap["modrinth-statistics"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  license(params: OperationParamsMap["modrinth-license"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tags(params: OperationParamsMap["modrinth-tags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  forgeUpdates(params: OperationParamsMap["modrinth-forge-updates"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchV3(params?: OperationParamsMap["modrinth-search-v3"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchV3Body(params: OperationParamsMap["modrinth-search-v3-body"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchV3Options(params?: OperationParamsMap["modrinth-search-v3-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  version(params: OperationParamsMap["modrinth-version"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fileProjects(params: OperationParamsMap["modrinth-file-projects"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fileVersion(params: OperationParamsMap["modrinth-file-version"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fileUpdate(params: OperationParamsMap["modrinth-file-update"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fileVersions(params: OperationParamsMap["modrinth-file-versions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  filesUpdate(params: OperationParamsMap["modrinth-files-update"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  filesUpdateIndividual(params: OperationParamsMap["modrinth-files-update-individual"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  filesUpdateMany(params: OperationParamsMap["modrinth-files-update-many"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  versions(params: OperationParamsMap["modrinth-versions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  collection(...args: OperationRequestArgs<"modrinth-collection">): Promise<OperationResponseMap["modrinth-collection"]>;
  collections(...args: OperationRequestArgs<"modrinth-collections">): Promise<OperationResponseMap["modrinth-collections"]>;
  metadataLinkPlatforms(...args: OperationRequestArgs<"modrinth-metadata-link-platforms">): Promise<OperationResponseMap["modrinth-metadata-link-platforms"]>;
  metadataLoaderFields(...args: OperationRequestArgs<"modrinth-metadata-loader-fields">): Promise<OperationResponseMap["modrinth-metadata-loader-fields"]>;
  metadataLoaderFieldValues(...args: OperationRequestArgs<"modrinth-metadata-loader-field-values">): Promise<OperationResponseMap["modrinth-metadata-loader-field-values"]>;
  metadataLoaders(...args: OperationRequestArgs<"modrinth-metadata-loaders">): Promise<OperationResponseMap["modrinth-metadata-loaders"]>;
  organization(...args: OperationRequestArgs<"modrinth-organization">): Promise<OperationResponseMap["modrinth-organization"]>;
  organizationProjects(...args: OperationRequestArgs<"modrinth-organization-projects">): Promise<OperationResponseMap["modrinth-organization-projects"]>;
  organizations(...args: OperationRequestArgs<"modrinth-organizations">): Promise<OperationResponseMap["modrinth-organizations"]>;
  project(...args: OperationRequestArgs<"modrinth-project">): Promise<OperationResponseMap["modrinth-project"]>;
  checkProject(...args: OperationRequestArgs<"modrinth-check-project">): Promise<OperationResponseMap["modrinth-check-project"]>;
  dependencies(...args: OperationRequestArgs<"modrinth-dependencies">): Promise<OperationResponseMap["modrinth-dependencies"]>;
  projectDisclosures(...args: OperationRequestArgs<"modrinth-project-disclosures">): Promise<OperationResponseMap["modrinth-project-disclosures"]>;
  projectVersions(...args: OperationRequestArgs<"modrinth-project-versions">): Promise<OperationResponseMap["modrinth-project-versions"]>;
  projectVersion(...args: OperationRequestArgs<"modrinth-project-version">): Promise<OperationResponseMap["modrinth-project-version"]>;
  projects(...args: OperationRequestArgs<"modrinth-projects">): Promise<OperationResponseMap["modrinth-projects"]>;
  randomProjects(...args: OperationRequestArgs<"modrinth-random-projects">): Promise<OperationResponseMap["modrinth-random-projects"]>;
  search(...args: OperationRequestArgs<"modrinth-search">): Promise<OperationResponseMap["modrinth-search"]>;
  statistics(...args: OperationRequestArgs<"modrinth-statistics">): Promise<OperationResponseMap["modrinth-statistics"]>;
  license(...args: OperationRequestArgs<"modrinth-license">): Promise<OperationResponseMap["modrinth-license"]>;
  tags(...args: OperationRequestArgs<"modrinth-tags">): Promise<OperationResponseMap["modrinth-tags"]>;
  forgeUpdates(...args: OperationRequestArgs<"modrinth-forge-updates">): Promise<OperationResponseMap["modrinth-forge-updates"]>;
  searchV3(...args: OperationRequestArgs<"modrinth-search-v3">): Promise<OperationResponseMap["modrinth-search-v3"]>;
  searchV3Body(...args: OperationRequestArgs<"modrinth-search-v3-body">): Promise<OperationResponseMap["modrinth-search-v3-body"]>;
  searchV3Options(...args: OperationRequestArgs<"modrinth-search-v3-options">): Promise<OperationResponseMap["modrinth-search-v3-options"]>;
  version(...args: OperationRequestArgs<"modrinth-version">): Promise<OperationResponseMap["modrinth-version"]>;
  fileProjects(...args: OperationRequestArgs<"modrinth-file-projects">): Promise<OperationResponseMap["modrinth-file-projects"]>;
  fileVersion(...args: OperationRequestArgs<"modrinth-file-version">): Promise<OperationResponseMap["modrinth-file-version"]>;
  fileUpdate(...args: OperationRequestArgs<"modrinth-file-update">): Promise<OperationResponseMap["modrinth-file-update"]>;
  fileVersions(...args: OperationRequestArgs<"modrinth-file-versions">): Promise<OperationResponseMap["modrinth-file-versions"]>;
  filesUpdate(...args: OperationRequestArgs<"modrinth-files-update">): Promise<OperationResponseMap["modrinth-files-update"]>;
  filesUpdateIndividual(...args: OperationRequestArgs<"modrinth-files-update-individual">): Promise<OperationResponseMap["modrinth-files-update-individual"]>;
  filesUpdateMany(...args: OperationRequestArgs<"modrinth-files-update-many">): Promise<OperationResponseMap["modrinth-files-update-many"]>;
  versions(...args: OperationRequestArgs<"modrinth-versions">): Promise<OperationResponseMap["modrinth-versions"]>;
}
export { ModrinthClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default ModrinthClient;
