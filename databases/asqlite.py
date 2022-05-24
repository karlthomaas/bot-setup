import aiosqlite, time

class Sqldb:
    def __init__(self):
        self.db = None
        self.cursor = None

    async def create_connection(self):
        print('> DB Connection established')
        self.db = await aiosqlite.connect('./databases/database.db')
        self.cursor = await self.db.cursor()

    async def check_user(self, userid=None):
        await self.cursor.execute("Select * From Users Where DiscordID = ?", (userid, ))
        data = await self.cursor.fetchall()
        
        if len(data) == 0:
            # User is not inside database
            await self.cursor.execute("Insert Into Users (DiscordID) Values(?)", (userid, ))
            await self.db.commit()
            
            print(f'{userid} has been added to Database!')
            
    async def add_points(self, DiscordID = None, TwitterID = None, points=None):
        """Function which adds points to desired user"""
        await self.check_user(DiscordID)
        if DiscordID is not None:
            await self.cursor.execute("Update Users Set Points=Points + ? Where DiscordID = ?", (points, DiscordID, ))
            await self.db.commit()
            print(f'{DiscordID} was added {points} points!')
            
    async def get_points(self, DiscordID = None, TwitterID = None, points=None):
        await self.check_user(DiscordID)
        
        if DiscordID is not None:
            await self.cursor.execute("Select Points From Users Where DiscordID = ?", (DiscordID, ))
            data = await self.cursor.fetchall()
            
            return data[0][0]
                
                
    async def get_leaderboard(self):
        await self.cursor.execute("Select * From Users Order By Points DESC Limit 25")
        data = await self.cursor.fetchall()
        return data
    
sqldb = Sqldb()