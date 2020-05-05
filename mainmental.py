from depression import Depression
from anorexia import Anorexia
from anxietyDisorder import AnxietyDisorder
from mentalHealth import MentalHealth
import discord
from discord.ext import commands


def func(obj):
    """The summary, affected nd treatment functions of each mental health illness class"""
    obj.summary()
    obj.affected()
    obj.treatment()


onj_mentalHealth = MentalHealth()
obj_depression = Depression()
obj_anxietyDisorder = AnxietyDisorder()
obj_anorexia = Anorexia()

onj_mentalHealth[0].summary()
onj_mentalHealth[1].affected()

obj_anorexia.summary[0]()
obj_anorexia.affected[1]()
obj_anorexia.treatment[2]()

obj_anxietyDisorder.summary[0]()
obj_anxietyDisorder.treatment[2]()
obj_anxietyDisorder.affected[1]()

obj_depression.affected[1]()
obj_depression.treatment[2]()
obj_depression.summary[0]()

