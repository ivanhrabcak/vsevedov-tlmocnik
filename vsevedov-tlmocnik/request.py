from pydantic import BaseModel


class ArticleRequest(BaseModel):
    article: str