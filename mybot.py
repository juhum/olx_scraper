import discord
from discord.ext import commands
import subprocess
import main

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello')
async def say_hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')


@bot.command(name='jp2')
async def say_hello(ctx):
    await ctx.send(f'JP2GMD')


@bot.command(name='olx')
async def scrape_olx(ctx):
    # Call the scrape function
    titles, prices, mileages, years = main.scrape()

    # Send each list as a separate message
    for title, price, mileage, year in zip(titles, prices, mileages, years):
        message = f"{title} - {price} - {mileage} - {year}"
        await ctx.send(message)



bot.run('MTA4OTg0NzE1MDk5NDc5MjQ4OQ.GsduM5.4d9wsI8VW_J7VLmCCDWr7lKq2NRGDS4dK2nEfw')
