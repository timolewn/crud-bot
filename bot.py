import discord
from examples.test_datasource import TestDataSource
from examples.test_resource import TestResource
from crud_bot.discord_bot import DiscordBot

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True

    data_source: TestDataSource = TestDataSource(name="Test Source")
    bot_manager: DiscordBot = DiscordBot(
        bot_token="MTMzMDU4MzUzODY1NDc3NzM5Nw.GMMTXC.wcKaOJG2D0nMGh8pMCIb9kPEo22_lcSaKRPQHw",
        resource_type=TestResource,
        data_source=data_source,
        command_prefix="!",
        intents=intents,
    )

    bot_manager.run()
