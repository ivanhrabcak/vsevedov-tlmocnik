pub mod guards;
pub mod routes;
pub mod services;

use std::{collections::HashMap, env, sync::Arc};

use anyhow::Context;
use rocket::{futures::lock::Mutex, get, launch, routes, Config, State};
use sea_orm::{Database, DatabaseConnection};
use services::openai::{CompletionParams, OpenAI};

type TokenState = State<Arc<Mutex<HashMap<String, i32>>>>;
type DbState = State<DatabaseConnection>;

#[launch]
async fn rocket() -> _ {

    dotenv::dotenv()
        .context("Unable to load environment variables from .env")
        .unwrap();
    let db_url = env::var("DB_URL")
        .context("Unable to find DB_URL, please set it")
        .unwrap();
    let db = Database::connect(db_url)
        .await
        .context("Unable to connect to DB")
        .unwrap();

    let config = Config::figment().merge(("address", "0.0.0.0"));

    let token_state: Arc<Mutex<HashMap<String, i32>>> = Arc::new(Mutex::new(HashMap::new()));

    rocket::custom(config)
        .mount("/api", routes![])
        .manage(db)
        .manage(token_state)
}
