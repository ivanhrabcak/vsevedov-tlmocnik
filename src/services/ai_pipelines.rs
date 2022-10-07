use std::env;

use super::openai::{CompletionParams, OpenAI};

async fn sumarize(prompt: &String) -> String {
    let openai = OpenAI::new(env::var("OPENAI_TOKEN").unwrap());

    let mut input: String = String::from("Tu je článok:\n");
    input += &prompt;

    let response = openai
        .complete(
            CompletionParams::default().prompt(input),
            "davinci-002".into(),
        )
        .await;

    response
}

pub trait Classifier {
    fn classify(self, prompt: String) -> String;
}



pub struct AiPipelineManager {
    queue: Vec<Box<dyn Classifier>>,
    intermediate: String
}

impl AiPipelineManager {

    pub fn new() -> Self {
        Self {
            queue: Vec::new(),
            intermediate: String::new()
        }
    }

    pub fn prompt(mut self, prompt: String) -> Self {
        self.intermediate = prompt;
        self
    }

    pub fn add_pipe(mut self, pipe: Box<dyn Classifier>) -> Self {
        self.queue.push(pipe);
        self
    }

    pub fn add_pipe_at(mut self, pipe: Box<dyn Classifier>, index: usize) -> Self {
        self.queue.insert(index, pipe);
        self
    }

    pub fn execute(self: Box<Self>) -> String {
        // TODO: Finish This
        // Iterate over all the items in queue, call the .classify() with the prompt
        // Then update the prompt with the result of the last iteration
        unimplemented!()
    }

}
