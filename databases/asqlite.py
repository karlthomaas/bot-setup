import aiosqlite

class Sqldb:
    def __init__(self):
        self.db = None
        self.cursor = None

    async def create_connection(self):
        print('Connection established')
        self.db = await aiosqlite.connect('./databases/database.db')
        self.cursor = await self.db.cursor()

sqldb = Sqldb()