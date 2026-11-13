import { ModrinthClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new ModrinthClient({ apiKey });

  const search = await client.search({ query: "sodium", limit: 5 });
  console.log("search", search);
  const statistics = await client.statistics({  });
  console.log("statistics", statistics);
