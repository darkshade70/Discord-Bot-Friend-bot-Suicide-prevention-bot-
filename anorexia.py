from mentalHealth import MentalHealth


class Anorexia(MentalHealth):
    """
    Holds all the information for the illness anorexia

    Attributes
    ----------
    client: str
            The actual discord bot. This will allow us to access/reference the bot within the cog
    summary: str
            This contains the summary of what the specific illness is (unique depending on illness)
    affected: str
            This contains the number of people affected and some symptoms
    """

    def __init__(self, client, summary, affected, treatment):
        """
             Holds specific information on the illness anorexia

             Parameters
             ----------
             client : str
                     The client/bot created in the main file bot.py. This allows us to call the bot in the cogs folder

             summary : str
                   Prints the symptoms related to the illness
        """
        super().__init__(client, summary, affected)
        self.treatment = treatment

    async def summary(self):
        """Prints on discord channel the summary of illness"""

        print("Anorexia:\nWhat is it? :\n"
              "Anorexia nervosa, more commonly known as anorexia, is both an eating disorder "
              "and a metabolic condition that results in excessive weight-loss "
              "and extreme thinness caused by self-starvation. The root of this problem is psychological"
              "as the victim harshly convinces themselves that they are overweight")

    def affected(self):
        """Information the # of affected and symptoms"""

        print("Around 40 million people are affected by anxiety disorder in the US alone and over 300 million"
              "people worldwide. Typically victims suffering from anxiety disorders may experience episodes "
              "of intense stress. This could result in a increase in heart beat, shortness of breath, sleep"
              "problems and forms of panic attacks.")

    def treatment(self):
        """Possible treatments to anorexia"""

        print("There are many different ways to tackle this illness. Some forms of treatment can be yoga,"
              "exercise, keeping a updated journal, or even meditation. What'simportant is to recognise when"
              "the symptoms of panic attack are occurring and to relax/calm yourself down as quickly as "
              "possible. If it means separating yourself from the rest of the group for a bit to calm or "
              "excusing yourself from an event, your health is the most important priority.")
