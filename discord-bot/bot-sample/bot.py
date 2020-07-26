from discord.ext import commands
import os

bot = commands.Bot(
    command_prefix=["!", "$"],
    description="A sample bot",
)


@bot.command()
async def echo(ctx, *args):
    await ctx.send(args)

bot.run(os.environ["BOT_TOKEN"])
