import asyncio
import threading
import uuid
from asyncio import AbstractEventLoop, Task

import discord


class Activity:
    def __init__(self, minutes: int, description: str, interaction: discord.Interaction):
        self.minutes = minutes
        self.description = description
        self.interaction = interaction

    async def start(self):
        await asyncio.sleep(self.minutes * 60)
        await self.interaction.followup.send(f"Timer ended: {self.description}")

    def __str__(self):
        return f"Activity(Minutes: {self.minutes}, Description: {self.description})"


class ActivityManager:
    def __init__(self):
        self.activities: dict[str, Activity] = {}

    def add_activity(self, minutes: int, description: str, interaction: discord.Interaction):
        activity = Activity(minutes, description, interaction)
        key = str(uuid.uuid4())
        self.activities[key] = activity
        task: Task = asyncio.create_task(activity.start())
        task.add_done_callback(lambda t: self.remove_activity(key))

    def remove_activity(self, activity):
        if activity in self.activities:
            self.activities.pop(activity)

    def list_activities(self):
        return self.activities.items()
