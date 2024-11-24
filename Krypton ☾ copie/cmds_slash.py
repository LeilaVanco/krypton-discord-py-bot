import discord
from discord.ext import commands

intents = discord.Intents.all()
token = "YOUR_TOKEN"
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.tree.command()
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    roles_mention = [role.mention for role in member.roles if role.name != "@everyone"]
    user = await bot.fetch_user(member.id)
    #tab = [""]
    tab2 = [member.avatar, member.mention, member.global_name, member.created_at.strftime("%d/%m/%Y à %H:%M:%S"), member.joined_at.strftime("%d/%m/%Y à %H:%M:%S"), "".join(f"{roles_mention}")]
    if user.banner:
        tab2.insert(1, user.banner.url)
    else:
        await tab2.insert(1, "The user doesn't have banner")
    await interaction.response.send_message(f"{interaction.user}, here some informations about {member.mention}")
    for i in tab2:
        await interaction.followup.send(f"{i}")

@bot.tree.command()
async def guildinfo(interaction: discord.Interaction):
    guild = interaction.guild
    await interaction.response.send_message(f"{guild.name} server was created on {guild.created_at.strftime("%d/%m/%Y à %H:%M:%S")} by {guild.owner} and has {guild.member_count} members")

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"The bot latency is {bot.latency * 1000:.2f} ms")


@bot.event
async def on_ready():
    print(f"I am well connected to {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} command(s) well synchronized !")
    except Exception as error:
        print(error)




if __name__ == "__main__":
    bot.run(token)
