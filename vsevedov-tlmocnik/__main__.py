from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .flags import flags
from .request import ArticleRequest

import orjson

from fastapi.responses import JSONResponse

load_dotenv()

class ORJsonResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any):
        return orjson.dumps(content)

app = FastAPI(default_response_class=ORJsonResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"]
)

@app.post("/flags")
def determine_flags_for_article(article: ArticleRequest):
    print(article)
    result = [(flag.display_name, flag.is_fired(article.article)) for flag in flags]
    print(result)
    return result