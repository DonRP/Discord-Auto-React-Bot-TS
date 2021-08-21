import os
from discord.ext import commands
from discord.ext.commands   import Bot
import asyncio

bot = commands.Bot(command_prefix="#")

emojis = [
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

@bot.event
async def on_ready():
    print ("Bot is ready!")

@bot.event
async def on_message(message):
    if(message.channel.id == 850358018394161193):
        for i in emojis:
            await message.add_reaction(i)
    else:
        pass

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
