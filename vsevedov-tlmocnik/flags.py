from .flag import AnswerEnum, Flag

class NegativeEmotionFlag(Flag):
    display_name = "Tento článok sa snaží vyvolať v čitateľovi negatívne emócie."
    prompt = "Is this article trying to evoke negative feelings in the reader?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ProvocativeToneFlag(Flag):
    display_name = "Tento článok je napísaný v provokatívnom tóne."
    prompt = "Is this article written in a provocative tone?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ControversialTopicFlag(Flag):
    display_name = "Tento článok hovorí o kontroverzných témach."
    prompt = "Does this article mention any controversial topics<"
    
    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class AlarmingToneFlag(Flag):
    display_name = "Tento článok má alarmujúci tón."
    prompt = "Does this article have an alarming tone?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ImmidiateReactionFlag(Flag):
    display_name = "Tento článok žiada čitateľa o neodkladné konanie."
    prompt = "Does this article request immidiate action from the reader?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ProfitIncentiveFlag(Flag):
    display_name = "Tento článok je napísaný za účelom profitu."
    prompt = "Is this article written for the intention of earning money?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class SharingIncentiveFlag(Flag):
    display_name = "Tento článok vyzýva k jeho zdieľaniu."
    prompt = "Does this article ask the reader to share it?"

    def is_fired(self, article: str) -> bool:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

flags = [NegativeEmotionFlag(), ProvocativeToneFlag(), 
         ControversialTopicFlag(), AlarmingToneFlag(), 
         ImmidiateReactionFlag(), ProfitIncentiveFlag(),
         SharingIncentiveFlag()]