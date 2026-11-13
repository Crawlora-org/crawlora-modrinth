use crawlora_modrinth::{Client, ModelModrinthObjectResponseDoc, ModrinthSearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .modrinth
        .search(ModrinthSearchParams {
            query: Some("sodium".to_owned()),
            limit: Some(5),
            ..Default::default()
        })
        .await?;
    let data: ModelModrinthObjectResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
