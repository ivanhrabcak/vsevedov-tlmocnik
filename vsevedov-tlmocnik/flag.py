import os
import openai
import enum

class AnswerEnum(enum.Enum):
    YES = "yes"
    NO = "no"
    CANNOT_TELL = "cannot tell"


class Flag:
    prompt: str
    display_name: str

    def answer_prompt(self, article: str) -> AnswerEnum:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        full_prompt = f"""Tu je článok:
\"\"\"
{article}
\"\"\"
{self.prompt}"""
        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=full_prompt,
            max_tokens=256,
            temperature=0.7
        )
        answer = completion["choices"][0]["text"].replace(self.prompt, "")
        print(answer, self.prompt)

        for _, enum_member in AnswerEnum._member_map_.items():
            if enum_member.value in answer.lower():
                return enum_member

    def is_fired(self, article: str) -> AnswerEnum:
        raise NotImplemented("flag_fired not implemented")