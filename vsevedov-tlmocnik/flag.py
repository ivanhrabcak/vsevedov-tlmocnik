import os
import openai
import enum

class AnswerEnum(enum.Enum):
    YES = "yes"
    NO = "no"
    CANNOT_TELL = "cannot tell"


class Flag:
    prompt: str

    def __init__(self) -> None:
        pass
    
    def answer_prompt(self, article: str) -> AnswerEnum:
    
        openai.api_key = os.getenv("OPENAI_API_KEY")
        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=article,
            max_tokens=21,
            temperature=0.7
        )
        answer = completion["choices"][0]["text"]

        for _, enum_member in AnswerEnum._member_map_.items():
            if enum_member.value in answer.lower():
                return enum_member

    def flag_fired(self) -> AnswerEnum:
        raise NotImplemented("flag_fired not implemented")