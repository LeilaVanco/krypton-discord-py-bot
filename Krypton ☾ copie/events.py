import discord

token = "YOUR_TOKEN"
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

@client.event
async def on_ready():
    print("hi hi hi c pré ON COURT DANS LES PRéS!!!")
    

client.run(token=token)