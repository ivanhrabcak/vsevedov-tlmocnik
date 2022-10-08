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

    classification_prompt = "Which statement could this statement be simplified to? (Yes., No., Cannot tell.)\nStatement:"

    def answer_prompt(self, article: str) -> str:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        full_prompt = f"""Here's an article::
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
        answer = completion["choices"][0]["text"]
        print(answer)

        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"""{self.classification_prompt} 
{answer}""")

        answer = completion["choices"][0]["text"]

        for _, enum_member in AnswerEnum._member_map_.items():
            if enum_member.value in answer.lower():
                return enum_member

        print(answer, self.prompt)

        return answer

    def is_fired(self, article: str) -> bool:
        raise NotImplemented("flag_fired not implemented")