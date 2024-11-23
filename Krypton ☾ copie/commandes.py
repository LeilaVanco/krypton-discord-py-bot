import discord
from discord.ext import commands

token = "YOUR_TOKEN"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)


@bot.command()
async def test(ctx):
    await ctx.send("meow")

if __name__ == "__main__":
    bot.run(token=token)