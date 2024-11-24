#In this case, logs are only working on one server and channel, that you can choose below

import discord
from discord.ext import commands

token = "YOUR_TOKEN"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print(f"I am well logged to {bot.user}")

@bot.event
async def on_raw_message_edit(playload: discord.RawMessageUpdateEvent):
    author_id = playload.data.get("author", {}).get("id", None)
    if author_id == YOUR_BOT_ID:
        return
    if playload.guild_id == YOUR_SERVER:
        channel = bot.get_channel(YOUR_LOGS_CHANNEL)
        if channel:
            message_id = playload.message_id
            author_avatar = playload.data.get("author", {}).get("avatar", None)
            new_content = playload.data.get("content", None)
            if new_content:
                await channel.send(f"https://cdn.discordapp.com/avatars/{author_id}/{author_avatar}.png")
                await channel.send(f"The message with the ID {message_id} was edited by {author_id}.\nIts new content is : {new_content}")




if __name__ == "__main__":
    bot.run(token)
