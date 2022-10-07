
pub mod auth;

use std::{env, sync::Arc, collections::HashMap};

use anyhow::Context;
use rocket::{launch, routes, get, futures::lock::Mutex, State, Config};
use sea_orm::{Database, DatabaseConnection};

type TokenState = State<Arc<Mutex<HashMap<String, i32>>>>;
type DbState = State<DatabaseConnection>;

#[launch]
async fn rocket() -> _ {
    dotenv::dotenv().context("Unable to load environment variables from .env").unwrap();
    let db_url = env::var("DB_URL").context("Unable to find DB_URL, please set it").unwrap();
    let db = Database::connect(db_url).await.context("Unable to connect to DB").unwrap();
    
    let config = Config::figment().merge(("address", "0.0.0.0"));
    
    let token_state: Arc<Mutex<HashMap<String, i32>>> = Arc::new(Mutex::new(HashMap::new()));



    rocket::custom(config)
        .mount("/api", routes![greet])
        .manage(db)
        .manage(token_state)
}
#[get("/hello")]
pub fn greet(_db: &State<DatabaseConnection>) -> &'static str {
    "Hello"
}
