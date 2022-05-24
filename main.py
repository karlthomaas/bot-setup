import disnake, os, time, json
from disnake.ext import commands
import logging as l

intents = disnake.Intents.default()
intents.members = True

with open('jsons/configs.json') as f:
    configs = json.load(f)

l.basicConfig(filename=configs['logfile'], level=l.INFO,format='%(asctime)s %(levelname)-8s - %(message)s')


client = commands.Bot(command_prefix=".", intents=intents, test_guilds=[930091138352840715])

@client.event
async def on_ready():
    print(f'{client.user} is running!')

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        l.info(f'{extension} laeti peale.')
        time.sleep(1)
        await ctx.message.add_reaction('✅')

    except Exception as ex:
        time.sleep(1)
        await ctx.message.add_reaction('❌')
        l.warning(ex)


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        l.info(f'{extension} laeti maha.')
        time.sleep(1)
        await ctx.message.add_reaction('✅')
    except Exception as ex:
        time.sleep(1)
        await ctx.message.add_reaction('❌')
        l.warning(ex)


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        time.sleep(1)
        await ctx.message.add_reaction('✅')
        l.info(f'{extension} tehti restart.')
    except Exception as ex:
        time.sleep(1)
        await ctx.message.add_reaction('❌')
        l.warning(ex)

for filenimi in os.listdir('./cogs'):
    if filenimi.endswith('.py'):
        client.load_extension(f'cogs.{filenimi[:-3]}')

with open('./jsons/token.json') as f:
    token = json.load(f)
    client.run(token["token"])