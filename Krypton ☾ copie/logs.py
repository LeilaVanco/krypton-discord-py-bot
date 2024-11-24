#In this case, logs are only working on one server and channel, that you can choose below

import discord
from discord.ext import commands

token = "YOUR_TOKEN"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)
messages_cache = {}

@bot.event
async def on_ready():
    print(f"I am well connected on {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    if not message.author.bot:  
        messages_cache[message.id] = message.content

@bot.event
async def on_raw_message_edit(payload: discord.RawMessageUpdateEvent):
    if payload.guild_id == 1308177515130654851:
        try:
            channel = bot.get_channel(payload.channel_id)
            author_id = payload.data.get("author", {}).get("id", None)
            logs_channel = bot.get_channel(1310043004677132380)
            author_avatar = payload.data.get("author", {}).get("avatar", None)
            new_message = await channel.fetch_message(payload.message_id)
            new_content = new_message.content
            messages_cache[payload.message_id] = new_content

            if payload.message_id in messages_cache:
                old_content = messages_cache[payload.message_id] 
            if new_content:
                await logs_channel.send(f"https://cdn.discordapp.com/avatars/{author_id}/{author_avatar}.png")
                await logs_channel.send(f"New modified message by <@{author_id}> in {channel.mention}:\n Before : {old_content}.\n After : [{new_content}](https://discord.com/channels/{new_message.guild.id}/{channel.id}/{new_message.id})")
                
        except discord.NotFound:
            await channel.send("Modified message not found")
        
    else:
        await channel.send("Modified message wasn't in the cache : impossible to retrieve its old content")
                




if __name__ == "__main__":
    bot.run(token)
