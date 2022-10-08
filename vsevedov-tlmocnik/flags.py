from .flag import AnswerEnum, Flag

class NegativeEmotionFlag(Flag):
    display_name = "Tento článok sa snaží vyvolať v čitateľovi negatívne emócie."
    prompt = "Snaží sa článok v čitateľovi vyvolať negatívne emócie? (yes/no/cannot tell)"

    def is_fired(self, article: str) -> AnswerEnum:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ProvocativeToneFlag(Flag):
    display_name = "Tento článok je napísaný v provokatívnom tóne."
    prompt = "Má tento článok provokatívny tón? (yes/no/cannot tell)"

    def is_fired(self, article: str) -> AnswerEnum:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ControversialTopicFlag(Flag):
    display_name = "Tento článok hovorí o kontroverzných témach."
    prompt = "Píše tento článok o kontroverznej téme? (yes/no/cannot tell)"
    
    def is_fired(self, article: str) -> AnswerEnum:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class AlarmingToneFlag(Flag):
    display_name = "Tento článok má alarmujúci tón."
    prompt = "Má článok alarmujúci tón? (yes/no/cannot tell)"

    def is_fired(self, article: str) -> AnswerEnum:
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ImmidiateReactionFlag(Flag):
    display_name = "Tento článok žiada čitateľa o neodkladné konanie."
    prompt = "Žiada (priamo alebo nepriamo) článok čitateľa aby ihneď konal? (yes/no/cannot tell)"

    def is_fired(self, article: str):
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class ProfitIncentiveFlag(Flag):
    display_name = "Tento článok je napísaný za účelom profitu."
    prompt = "Je článok napísaný za účelom profitu pre autora? (yes/no/cannot tell)"

    def is_fired(self, article: str):
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

class SharingIncentiveFlag(Flag):
    display_name = "Tento článok vyzýva k jeho zdieľaniu."
    prompt = "Vyzýva článok čitateľa k šíreniu tohto článku? (yes/no/cannot tell)"

    def is_fired(self, article: str):
        return True if self.answer_prompt(article) == AnswerEnum.YES else False

flags = [NegativeEmotionFlag(), ProvocativeToneFlag(), 
         ControversialTopicFlag(), AlarmingToneFlag(), 
         ImmidiateReactionFlag(), ProfitIncentiveFlag(),
         SharingIncentiveFlag()]