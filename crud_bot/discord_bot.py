from typing import Type, Callable, List, Optional

import discord
from discord.ext import commands

from crud_bot.crud_manager import CrudManager
from crud_bot.resource import Resource
from crud_bot.data_source import DataSource


class DiscordBot:
    def __init__(
        self,
        bot_token: str,
        resource_type: Type[Resource],
        data_source: DataSource[Resource],
        command_prefix: str = "!",
        intents: Optional[discord.Intents] = None,  # Add an optional intents parameter
    ):
        """
        Initializes the bot manager.

        Args:
            bot_token (str): The Discord bot token.
            resource_type (Type[Resource]): The type of the resource (e.g., Hero).
            data_source (DataSource[Resource]): The data source for managing resources.
            command_prefix (str): The prefix for Discord commands.
            intents (Optional[discord.Intents]): The Discord intents for the bot. Default is None.
        """
        self.bot_token = bot_token
        self.resource_type = resource_type
        self.data_source = data_source
        self.crud_manager = CrudManager(self.data_source)

        # Default intents if none are provided
        if intents is None:
            intents = discord.Intents.default()
            intents.messages = True  # Enable message-related events
            intents.guilds = True  # Enable guild-related events

        self.bot = commands.Bot(command_prefix=command_prefix, intents=intents)
        self._setup_commands()

    def _setup_commands(self) -> None:
        """Registers the default CRUD commands for the bot."""

        @self.bot.command()
        async def create(ctx, id: int, *args):
            fields = args
            resource = self.resource_type(id=id, **self._fields_from_args(fields))
            self.crud_manager.create(resource)
            await ctx.send(
                f"{self.resource_type.__name__} created: {resource.to_dict()}"
            )

        @self.bot.command()
        async def read(ctx, id: int):
            resource = self.crud_manager.read(id)
            if resource:
                await ctx.send(
                    f"{self.resource_type.__name__} found: {resource.to_dict()}"
                )
            else:
                await ctx.send(f"{self.resource_type.__name__} not found.")

        @self.bot.command()
        async def update(ctx, id: int, *args):
            fields = args
            resource = self.resource_type(id=id, **self._fields_from_args(fields))
            updated = self.crud_manager.update(id, resource)
            if updated:
                await ctx.send(
                    f"{self.resource_type.__name__} updated: {updated.to_dict()}"
                )
            else:
                await ctx.send(f"{self.resource_type.__name__} not found.")

        @self.bot.command()
        async def delete(ctx, id: int):
            success = self.crud_manager.delete(id)
            if success:
                await ctx.send(f"{self.resource_type.__name__} with ID {id} deleted.")
            else:
                await ctx.send(f"{self.resource_type.__name__} not found.")

        @self.bot.command()
        async def list_all(ctx):
            resources = self.crud_manager.list_all()
            if resources:
                await ctx.send(
                    f"{self.resource_type.__name__}s: {[resource.to_dict() for resource in resources]}"
                )
            else:
                await ctx.send(f"No {self.resource_type.__name__}s found.")

    def _fields_from_args(self, args: List[str]) -> dict:
        """
        Converts a list of key=value pairs into a dictionary.
        Args:
            args (List[str]): List of strings in the form of key=value.

        Returns:
            dict: Parsed fields for resource creation/update.
        """
        return dict(arg.split("=", 1) for arg in args)

    def add_custom_command(self, name: str, func: Callable):
        """
        Adds a custom command to the bot.

        Args:
            name (str): The command name.
            func (Callable): The function to execute for the command.
        """
        self.bot.command(name=name)(func)

    def run(self):
        """Runs the bot."""
        self.bot.run(self.bot_token)
