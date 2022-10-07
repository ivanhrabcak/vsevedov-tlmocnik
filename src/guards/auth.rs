use rocket::{
    http::Status,
    request::{self, FromRequest, Outcome},
    Request,
};

use crate::TokenState;

struct TempUser {
    id: i32,
}
#[derive(Debug)]
enum AuthError {
    InvalidToken,
    MissingToken,
}

#[rocket::async_trait]
impl<'r> FromRequest<'r> for TempUser {
    type Error = AuthError;
    async fn from_request(request: &'r Request<'_>) -> request::Outcome<Self, Self::Error> {
        let token_store = request.guard::<&TokenState>().await.unwrap().inner();
        let token_store = token_store.lock().await;

        let token = request.headers().get_one("token");

        match token {
            Some(t) => {
                if let Some(uid) = token_store.get(t) {
                    return Outcome::Success(Self { id: *uid });
                }
                return Outcome::Failure((Status::Unauthorized, Self::Error::InvalidToken));
            }
            None => return Outcome::Failure((Status::Unauthorized, Self::Error::MissingToken)),
        }
    }
}
