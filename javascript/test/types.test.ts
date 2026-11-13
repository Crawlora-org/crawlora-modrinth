import { ModrinthClient } from "../src/index.js";

const client = new ModrinthClient({ apiKey: "test-key" });
void client.collection({"id": "sample"});
void client.request("modrinth-collection", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("modrinth-collection", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("modrinth-collection", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.collection({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("modrinth-collection", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("modrinth-collection", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.metadataLinkPlatforms();
void client.request("modrinth-metadata-link-platforms");
// @ts-expect-error The selected operation requires its documented params.
void client.collection();
