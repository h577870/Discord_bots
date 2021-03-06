import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_id = os.getenv('DISCORD_1')

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print(
		f'{bot.user.name} has connected to Discord!'
	)
	print(bot.guilds)

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Welcome {member.name} to my Discord Server!'
	)

@bot.event
async def on_member_update(before, after):
	online_list = [
		f"Oh lord, {before.name} is here :monkaChrist: ",
		f"Ajt, {before.name} er endelig her :pepeOK: ",
		f"{before.name} :Pepega: "
	]
	random_str = random.choice(online_list)
	# offline -> online
	if str(before.status) == "offline":
		if str(after.status) == "online":
			guild = bot.get_guild(int(guild_id))
			await guild.text_channels[0].send(random_str)
			
# Litt finere formatering hadde gjort susen.
@bot.command(name='help')
async def helper(ctx):
	help_commands = [
		f'!so -> Søk etter spørsmål på Stack Overflow, f.eks. !so "Sort list python" ',
		f'!hs -> Bruk for å søke etter dokumentasjon for Haskell, f.eks. !hs map '
	]
	response = help_commands
	await ctx.send(response)


@bot.command(name='hs')
async def haskell(ctx, keyword: str):
	if not keyword:
		response = 'Haskell docs -> <https://hoogle.haskell.org/>'
	else:
		response = f'Haskell docs for {keyword} -> <https://hoogle.haskell.org/?hoogle={keyword}>'
	await ctx.send(response)
	
@bot.command(name='so')
async def stackOverflow(ctx, keyword: str):
	if not keyword:
		response = 'Søk etter spørsmål i Stack Overflow -> <https://stackoverflow.com/search>'
	else:
		placeholder: str = keyword.replace(' ', '+')
		response = f'Søk etter "{keyword}" ga følgende resultater -> <https://stackoverflow.com/search?q={placeholder}>'
	await ctx.send(response)

@bot.command(name='cljs')
async def clojureScript(ctx, keyword: str):
	if not keyword:
		response = 'Søk etter spørsmål i clojuredocs (foreløpig kun clojure.core) -> <https://clojuredocs.org/>'
	else:
		response = f'Søk etter {keyword} ga følgende resultater -> <https://clojuredocs.org/clojure.core/{keyword}>'
	await ctx.send(response)

bot.run(TOKEN)
