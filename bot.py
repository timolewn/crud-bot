from examples.test_datasource import TestDataSource
from examples.test_resource import TestResource
from crud_bot.discord_bot import DiscordBot

if __name__ == "__main__":
    data_source: TestDataSource = TestDataSource(name="Test Source")
    bot_manager: DiscordBot = DiscordBot(
        bot_token="secret",
        resource_type=TestResource,
        data_source=data_source,
        command_prefix="!",
    )

    bot_manager.run()
