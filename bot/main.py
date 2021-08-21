import os
from discord.ext import commands
from discord.ext.commands   import Bot
import asyncio

bot = commands.Bot(command_prefix="#")

emojis = [
            "a:weewoo:878395500448083998",
            "a:CoolDoge:878395321749737552",
            "a:confetti:878395401995169792",
            "a:clap:878394777765314650",
            "a:pepeAhh:878395533276901466",
            "a:incest:878396964998373436",
            "a:lust:878391146211070003",
            "a:handjob:702546745988612157",
            "a:trippypepe:702541364306509935",
            "a:analvirgin:702539631555641534",
            "a:whatspoppin:878402018161610752",
            "a:pepeHmm:878401392505679905",
            "a:AngryPing:878395183950098524",
            "a:hypepepe:702546747376926790",
            ":facepalm:878396076888051712",
            "a:animebooty:702546752070353007"
        ]

@bot.event
async def on_ready():
    print ("Bot is ready!")

@bot.event
async def on_message(message):
    if(message.channel.id == 772881252105453609):
        for i in emojis:
            await message.add_reaction(i)
    else:
        pass

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
