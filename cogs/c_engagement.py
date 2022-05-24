import disnake
from disnake.ext import commands, tasks
from databases.asqlite import sqldb

class Engagement(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.connect_db.start()
        
    @tasks.loop(count=1)
    async def connect_db(self):
        await self.client.wait_until_ready()
        await sqldb.create_connection()
        
        
    @commands.Cog.listener()
    async def on_message(self, message):
        """
        User / Message Author gets +1 point for each new message.
        """
        await sqldb.add_points(DiscordID=message.author.id, points=1)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        userid = payload.user_id
        await sqldb.add_points(DiscordID=userid, points=1)
        
    @commands.slash_command()
    async def Points(self, inter):
        """Command used for viewing your points!"""
        points = await sqldb.get_points(inter.author.id)
        await inter.send(f'You currently have **{points}** points!', ephemeral=True)
        
    @commands.slash_command()
    async def Leaderboard(self, inter):
        data = await sqldb.get_leaderboard()
        print(data)
        
        
def setup(client):
    client.add_cog(Engagement(client))