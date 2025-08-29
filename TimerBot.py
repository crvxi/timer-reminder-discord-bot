import discord
from discord.ext import commands

from TimerCog import TimerCog


class TimerBot(commands.Bot):
    def __init__(self, server_id: int):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.all()
        super().__init__(
            command_prefix='!',  # we won't actually use this since we're using slash commands
            intents=intents
        )

        self.server_id: int = server_id

    async def setup_hook(self):
        guild = discord.Object(id=self.server_id)
        await self.load_extension("TimerCog")
        await self.tree.sync(guild=guild)
