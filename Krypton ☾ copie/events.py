import discord

token = "YOUR_TOKEN"
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
        
    if client.user.mentioned_in(message):
        await message.channel.send("YUP IT'S ME THAT YOU JUST CALLED???")

    if message.content == "no u":
        await message.channel.send("no u")

@client.event
async def on_ready():
    print("hi hi hi it's rEADY LET'S RUN to THE FIELDS !! (in french it sounds better...)")
    

if __name__ == "__main__": 
    client.run(token)
