import discord
from discord import app_commands
from discord.ext import commands

from ActivityManager import ActivityManager
from Properties import Properties


class TimerCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.activity_manager = ActivityManager()
        super().__init__()

    @app_commands.command(name="timer", description="Set a timer with a message")
    @app_commands.describe(minutes="Duration in minutes", message="Message to display when timer ends")
    async def command_timer(self, interaction: discord.Interaction, minutes: int, message: str):
        self.activity_manager.add_activity(minutes, message, interaction)
        await interaction.response.send_message(f"Timer set for {minutes} minutes: {message}")

    @commands.Cog.listener()
    async def on_ready(self):
        print("TimerCog is ready!")

    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")
        for get_command in self.get_commands():
            print(f"{get_command.name}: {get_command.description}")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


# global configuration function
async def setup(bot):
    cog = TimerCog(bot)
    properties = Properties()
    guild = discord.Object(id=properties.SERVER_ID)
    await bot.add_cog(cog, guild=guild)
