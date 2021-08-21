# Discord Bot Template

Fork this for a base bot for Discord

## Authentication

Create a file `.env` in the same directory as `bot.py` with the following contents:

```plaintext
# .env
DISCORD_TOKEN=INSERT_BOT_TOKEN_HERE
```

The token can be found at the [developer page](https://discord.com/developers/applications/)

**WARNING:** do not commit and/or push the .env file to a remote repository. Doing so will allow anyone to add custom commands or event handles to an already running instance of the bot.

## Initializing

Once you've got the `.env` file made and in the same directory as `bot.py`, starting up the bot is as simple as running `python3 bot.py`.
