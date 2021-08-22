import os
from discord.ext import commands
from discord.ext.commands   import Bot
import asyncio

bot = commands.Bot(command_prefix="#")

emojis_annuncements = [
            "a:weewoo:878418421572841493",
            "a:CoolDoge:878418843737948211",
            "a:confetti:878418500287361108",
            "a:clap:878419052618481684",
            "a:pepeAhh:878418334532657163",
            "a:incest:878418954622763078",
            "a:lust:878390258318848070",
            "a:handjob:878390203264430110",
            "a:whatspoppin:878418104420544552",
            "a:pepeHmm:878418140579639326",
            "a:AngryPing:878418810338705439",
            ":facepalm:878735715196870708",
            "a:animebooty:878419019164696657"
        ]

emojis_feedback = [
            ":heart:",
            ":thumbsup:",
            ":thumbsdown:",
        ]

emojis_fanart = [
            ":100:db009c8fa13d0f303df266e9d42c8e30",
            ":heart:0483f2b648dcc986d01385062052ae1c",
            ":thumbsup:28b51c7a7a5cf0f7690d36408f7646e1",
            ":thumbsdown:28b51c7a7a5cf0f7690d36408f7646e1",
            ":face_palm:28b51c7a7a5cf0f7690d36408f7646e1",
            ":face_vomiting:4c931151fd94ebc6aa6034427624b2ea"
        ]

emojis_fanart_approved = [
            "a:clap:878419052618481684",
            "a:incest:878418954622763078",
            "a:lust:878390258318848070",
            "a:handjob:878390203264430110",
            "a:pepeHmm:878418140579639326",
            ":facepalm:878735715196870708",
        ]

@bot.event
async def on_ready():
    print ("Bot is ready!")

@bot.event
async def on_message(message):
    if(message.channel.id == 850358018394161193):
        for i in emojis_annuncements:
            await message.add_reaction(i)
    elif(message.channel.id == 850344438344974378):
        for i in emojis_feedback:
            await message.add_reaction(i)
    elif(message.channel.id == 850344312327241728):
        for i in emojis_fanart:
            await message.add_reaction(i)
    elif(message.channel.id == 850344378399981588):
        for i in emojis_fanart_approved:
            await message.add_reaction(i)
    else:
        pass

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
