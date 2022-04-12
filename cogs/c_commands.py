import disnake
from disnake.ext import commands, tasks

class CogName(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

def setup(client):
    client.add_cog(CogName(client))