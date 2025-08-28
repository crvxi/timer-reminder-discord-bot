import os
import discord
from dotenv import load_dotenv
from discord import app_commands

# Initialize Discord Bot
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')
SERVER_ID: int = int(os.getenv('SERVER_ID'))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(
    name="timer",
    description="Set a timer",
    guild=discord.Object(id=SERVER_ID)
)
@app_commands.describe(minutes="Number of minutes for the timer",
                       message="Reminder message of the timer")
async def command_timer(interaction, minutes: int, message: str):
    await interaction.response.send_message(f"Timer set for {minutes} minutes: {message}")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=SERVER_ID))
    print("Ready!")


client.run(TOKEN)
