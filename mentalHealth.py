import discord
from discord.ext import commands


class MentalHealth:
    """
    Mental health class calls the the subclasses which are different types of mental illnesses and their information

    Attributes
    ----------
    client: str
           The actual discord bot. This will allow us to access/reference the bot within the cog
    summary: str
            summary of the illness
    """

    def __init__(self, client, summary, affected):
        """
          Holds information that all other mental illness classes will inherit

          Parameters
          ----------
          client : str
                  The client/bot created in the main file bot.py. This allows us to call the bot in the cogs folder
          summary: str
                  summary of the illness

        """
        self.client = client
        self.summary = summary
        self.affected = affected

    def summary(self):
        """A summary of mental health"""
        print(f"There are many different types of mental health illnesses that affects millions around the"
              f"world. This will provide summaries or certain illnesses and hopefully give a "
              f"better understanding")

    def affected(self):
        """Talks about the affects mental health issues have on people"""
        print(f"Mental health can affected anyone across the world despite ethnicity, age, or upbringing."
              f"No one is considered immune and the side effects from these mental illnesses can be "
              f"devastating and extremely painful.")
