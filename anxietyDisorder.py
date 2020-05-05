from mentalHealth import MentalHealth


class AnxietyDisorder(MentalHealth):
    """
    Holds all the information for the illness Anxiety Disorder

    Attributes
    ----------
    client: str
            The actual discord bot. This will allow us to access/reference the bot within the cog
    summary: str
            This contains the summary of what the specific illness is (unique depending on illness)
    affected: str
            This contains the statistics on how many people are affected by anxiety disorder
    treatment : str
            This contains the possible treatments for anxiety disorder
    """

    def __init__(self, client, summary, affected, treatment):
        """
            Holds specific information on the illness anxiety disorder

            Parameters
            ----------
            client : str
                    The client/bot created in the main file bot.py. This allows us to call the bot in the cogs folder

            summary : str
                  Prints the symptoms related to the illness

        """
        super().__init__(client, summary, affected)
        self.treatment = treatment

    def summary(self):
        """Prints on discord channel the summary of illness"""

        print("Anxiety Disorder:\nWhat is it? :\n"
              "Anxiety is a feeling of nervousness, worry, or unease that is a normal human experience. "
              "It is also present in a wide range of psychiatric disorders, "
              "including generalized anxiety disorder, panic disorder, and phobias. "
              "Although each of these disorders is different, they all feature distress and dysfunction "
              "specifically related to anxiety and fear.")

    def affected(self):
        """Information the # of affected and symptoms"""

        print("Anorexia affects over 30 million people worldwide. It is a psychological illness where people"
              "often think they are overweight. A large number of anorexia victims are females and teens as"
              "there is a strict body proportion/image that is favoured by the media and acts as an incentive"
              "for people to live up to those expectations, even through extreme means.")

    def treatment(self):
        """Possible treatments to anorexia"""

        print("Support groups are always a good start. Interventions where you approach the victim and really"
              "show them how much you care and are concerned for their health. Don't attack them but"
              "voice your concern so they understand how severe things can get. Treatment is periodic as "
              "typically an anorexic patient wont just suddenly consume more and more food right out of"
              "the gate. Set meal plans and reasonable menus for the patient and appropriately increase"
              "the increments of food. A professional dietitian/doctor is highly suggested for an expert"
              "opinion.")
