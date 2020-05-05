from mentalHealth import MentalHealth


class Depression(MentalHealth):
    """
    Holds all the information for the illness Depression

    Attributes
    ----------
    client: str
            The actual discord bot. This will allow us to access/reference the bot within the cog
    summary: str
            This contains the summary of what the specific illness is (unique depending on illness)
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

            affected: str
                  This contains the number of people affected and some symptoms

        """
        super().__init__(client, summary, affected)
        self.treatment = treatment

    def summary(self):
        """A summary of depression"""

        print("Depression:\nWhat is it? :\n"
              "Depression (major depressive disorder) is a common and serious medical illness that negatively "
              "affects how you feel, the way you think and how you act. Fortunately, it is also treatable. "
              "Depression causes feelings of sadness and/or a loss of interest in activities once enjoyed. "
              "It can lead to a variety of emotional and physical problems and can decrease "
              "a person’s ability to function at work and at home.")

    def affected(self):
        """Information the # of affected and symptoms"""

        print("Depression affects over 264 million people world wide. It is a very serious illness that "
              "makes people feel horrible about themselves. Many suicides are committed due to severe"
              "depression. Depression often leads people to feel very anti social, isolated, and lacks the "
              "ability to feel a sense of joy, typically finds the worst in everything.")

    def treatment(self):
        """Possible treatments to depression"""

        print("It is very important to develop a support group of people who are willing to listen and "
              "help you in your time of need. Support from close friends or family can be very significant as"
              "if you fill yourself with people who look out and care for you, it can help clear your mental"
              "state and hopefully erase some negative thoughts. A proper sleep schedule and proper dieting "
              "are also great way to combat depression. Possibly try a new workout plan or exercise with some "
              "friends on a consistent schedule.  ")
