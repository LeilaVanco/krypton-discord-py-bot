import discord
import time
from discord.ext import commands

token = "YOUR_TOKEN"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)


@bot.command()
async def test(ctx):
    await ctx.send("meow")

@bot.command()
async def decompte(ctx, delai: int):
    await ctx.send("ATTENTION..")
    for i in range(delai, 0, -1):
        time.sleep(1)
        await ctx.send(i)
    await ctx.send("It's over !")

@bot.command(
        description = "This is a test",
        brief = "another test",
        help = "retest"
)
async def repete(ctx, *, message):
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"ALL IS OKAY, LOGGED ON {bot.user}")
    try:
        synced = await bot.sync()
        print(f"{len(synced)} command(s) well synchronized !")
    except Exception as error:
        print(error)



if __name__ == "__main__":
    bot.run(token)
