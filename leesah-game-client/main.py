import os

from client_lib import quiz_rapid

# LEESAH QUIZ GAME CLIENT
# This is a template for the quiz game client.
# The client is a Python application that connects to the quiz game.

# Config #
# 1. Set `TEAM_NAME` to your preferred team name
TEAM_NAME = "sist_men_ikke_minst"
# 2. Set `HEX_CODE` to your preferred team color
HEX_CODE = "#FFFF00"
# ###### #


class MyParticipant(quiz_rapid.QuizParticipant):
    def __init__(self):
        super().__init__(TEAM_NAME)

    def handle_question(self, question: quiz_rapid.Question):
        if question.category == "team-registration":
            self.handle_register_team(question)

        if question.category == "NAV":
            self.handle_NAV(question)
            

    def handle_assessment(self, assessment: quiz_rapid.Assessment):
        pass

    # ---------------------------------------------------------------------------- Question handlers

    def handle_register_team(self, question: quiz_rapid.Question):
        # Add code here to solve the first question! Hint: Check Readme 😎
        self.publish_answer(
                question_id=question.messageId, category=question.category, answer=HEX_CODE
            )
    
    def handle_NAV(self, question: quiz_rapid.Question):

        if question.question == "På hvilken nettside finner man informasjon om rekruttering til NAV IT?":
            self.publish_answer(
                    question_id=question.messageId, category=question.category, answer="https://www.detsombetyrnoe.no/"
                )
    
        


        

            
        

def main():
    rapid = quiz_rapid.QuizRapid(
    team_name=TEAM_NAME,
    topic=os.getenv("QUIZ_TOPIC"),
    bootstrap_servers=os.getenv("KAFKA_BROKERS"),
    auto_commit=False,  # Bare skru på denne om du vet hva du driver med :)
    log_questions=True,  # Logg spørsmålene appen mottar
    log_answers=True,  # Logg svarene appen sender
    short_log_line=False,  # Logg bare en forkortet versjon av meldingene
    log_ignore_list=[],  # Liste med spørsmålskategorier loggingen skal ignorere
)
    return MyParticipant(), rapid