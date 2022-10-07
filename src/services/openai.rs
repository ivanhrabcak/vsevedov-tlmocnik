use std::collections::HashMap;

use reqwest::Client;
use serde::{Deserialize, Serialize};
use serde_json::Value;
pub struct OpenAI {
    api_key: String,
    client: Client,
}
#[derive(Debug, Serialize, Deserialize)]
pub struct CompletionParams {
    pub prompt: String,
    pub max_tokens: i64,
    pub top_p: f32, // A number called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
    pub temperature: f32, // The higher the value, for example, 0.9, the more “creative” the completion text will be.
    pub n: i32, // An integer that specifies the number of completions to generate for each prompt.
    pub stream: bool, // A boolean value to determine if partial progress should be streamed back.
    pub echo: bool, // A boolean value that tells the API to ech back the prompt along with the completion
    pub stop: String, // A string or array that acts as a delimiter to tell the API will stop generating further tokens.
    pub frequency_penalty: f32,
}

impl CompletionParams {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn prompt(mut self, prompt: String) -> Self {
        self.prompt = prompt;
        self
    }

    pub fn max_tokens(mut self, max_tokens: i64) -> Self {
        self.max_tokens = max_tokens;
        self
    }

    pub fn top_p(mut self, top_p: f32) -> Self {
        self.top_p = top_p;
        self
    }

    pub fn temperature(mut self, temperature: f32) -> Self {
        self.temperature = temperature;
        self
    }

    pub fn n(mut self, n: i32) -> Self {
        self.n = n;
        self
    }

    pub fn stream(mut self, stream: bool) -> Self {
        self.stream = stream;
        self
    }

    pub fn echo(mut self, echo: bool) -> Self {
        self.echo = echo;
        self
    }

    pub fn stop(mut self, stop: String) -> Self {
        self.stop = stop;
        self
    }

    pub fn frequency_penalty(mut self, frequency_penalty: f32) -> Self {
        self.frequency_penalty = frequency_penalty;
        self
    }
}

impl Default for CompletionParams {
    fn default() -> Self {
        Self {
            prompt: " ".into(),
            max_tokens: 24,
            top_p: 1.0,
            temperature: 0.25,
            n: 1,
            stream: false,
            echo: true,
            stop: "\n".into(),
            frequency_penalty: 0.0,
        }
    }
}

impl OpenAI {
    pub fn new(api_key: String) -> Self {
        Self {
            api_key,
            client: Client::new(),
        }
    }

    pub async fn complete(&self, params: CompletionParams, engine: String) -> String {
        let params = match serde_json::to_string(&params) {
            Ok(params) => params,
            Err(_) => panic!("Unable to serialize params"),
        };

        let endpoint = format!("https://api.openai.com/v1/engines/{}/completions", engine);
        let response = self
            .client
            .post(endpoint)
            .bearer_auth(self.api_key.clone())
            .header("Content-Type", "application/json")
            .body(params)
            .send()
            .await;

        match response {
            Ok(r) => {
                let text = r.text().await.unwrap();
                println!("{text}");
                let response: HashMap<String, Value> = serde_json::from_str(&text).unwrap();

                if let Some(choices) = response.get("choices") {
                    match choices {
                        Value::Null => {
                            println!("Null response json!");
                            "The AI returned no response.".to_string()
                        }
                        Value::Array(array) => {
                            let ai_output_map = array[0].as_object().unwrap();

                            // we know the 'text' key is string and present if we get to this line of code
                            let ai_output_text =
                                ai_output_map.get("text").unwrap().as_str().unwrap();
                            return String::from(ai_output_text);
                        }
                        _ => {
                            println!("Unexpected response!");
                            "The AI returned no response.".to_string()
                        }
                    }
                } else {
                    println!("Null choices!");
                    "The AI returned no response.".to_string()
                }
            }
            Err(_) => "Request building error!".to_string(),
        }
    }
}
