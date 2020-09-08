## Overview
1. Setup bot hosting environment
2. Setup service files
3. Run and verify service

## Setup bot hosting environment
1. Refer to [the server setup](../server-setup) for more information

## Setup service files
1. In [Discord's developer portal](https://discord.com/developers/applications), copy the bot token
2. Download `bot.env` to /etc/systemd/system/ and fill out `BOT_TOKEN` with the copied token
3. Download `bot.service` to /etc/systemd/system/ and fill out the path of `bot.py` in `ExecPath`

## Run and verify service
1. Run `sudo systemctl start bot.service`
2. Verify that the service is running with `systemctl status bot.service`

## Useful links
[Additional locations and options service file](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
