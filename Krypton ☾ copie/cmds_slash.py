import discord
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.all()
token = "YOUR_TOKEN"
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.tree.command(description= "Some informations on the specified user")
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    roles_mention = [role.mention for role in member.roles if role.name != "@everyone"]
    user = await bot.fetch_user(member.id)
    tab = ["Pfp : ", "Banner : ","Mention of the user: ", "Username : ", "Discord account creation date : ", "Arrival date : ", "Role(s) : "]
    tab2 = [member.avatar, member.mention, member.name, f"<t:{int(datetime.fromisoformat(f"{member.created_at}").timestamp())}:R>", f"<t:{int(datetime.fromisoformat(f"{member.joined_at}").timestamp())}:R>", "".join(f"{roles_mention if roles_mention else "No roles"}")]
    if user.banner:
        tab2.insert(1, user.banner.url)
    else:
        tab2.insert(1, "User doesn't have banner")
    
    await interaction.response.send_message(f"{interaction.user}, here some informations on {member.mention}")
    for i, k in zip(tab, tab2):
        await interaction.followup.send(f"{i}{k}")

@bot.tree.command(description= "Informations on the server")
async def guildinfo(interaction: discord.Interaction):
    guild = interaction.guild
    await interaction.response.send_message(f"{guild.name} server was created on <t:{int(datetime.fromisoformat(f"{guild.created_at}").timestamp())}:R> by {guild.owner.mention} ({guild.owner}) and has {guild.member_count} member(s).")

@bot.tree.command(description= "Return bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Bot latency is {bot.latency * 1000:.2f} ms")


@bot.event
async def on_ready():
    print(f"I am well connected on {bot.user}")
    try:
        await bot.tree.sync(guild = discord.Object(id = 1308177515130654851))
        #or await bot.tree.sync() if you don't want specific a server
        print(f"{len(bot.tree.get_commands())} command(s) well synchronized !")
    except Exception as error:
        print(f"Error while synchronizing commands : {error}")




if __name__ == "__main__":
    bot.run(token)
