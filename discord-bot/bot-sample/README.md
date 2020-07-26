### Overview

1. Setup Discord application on developer portal for bot credentials
2. Invite empty bot to server
3. Setup bot code
4. Host bot on local machine
5. Test bot in server

## Setup Discord application on developer portal for bot credentials
1. Create **New Application** in [Discord's developer portal](https://discord.com/developers/applications)

## Invite empty bot to server
1. In the [developer portal](https://discord.com/developers/applications), navigate to **OAuth2**
2. Select the **bot** checkmark under **scopes**
3. Copy the generated URL and paste it into a new tab
4. Select a server to add the bot and authorize it
5. [Optional] Create a role for the bot
6. [Optional] Restrict the bot to certain channels

## Setup bot code
1. Download `bot.py`, a Python code sample
2. Install the `discord` module as [per here](https://discordpy.readthedocs.io/en/latest/intro.html#installing): `python3 -m pip install -U discord.py`
3. Adjust code as needed

## Host bot on local machine
1. In the [developer portal](https://discord.com/developers/applications), go to **Bot** and press **copy** under **Token**
2. Edit your system's equivalent of `~/.bashrc`, and add this: `export BOT_TOKEN="your_client_secret_here"`
3. Load the environment variable by `source ~/.bashrc`
4. Run the code by `python3 bot.py`

## Test bot in server
1. Type `help` preceded by `!`/`$`
2. Type `echo` preceded by `!`/`$`, and any text after the command
3. Done!

## Useful links:
[Developer portal](https://discord.com/developers)

[discord.py documentation](https://discordpy.readthedocs.io/en/latest/index.html)

[More bot code examples](https://github.com/Rapptz/discord.py/tree/master/examples)
