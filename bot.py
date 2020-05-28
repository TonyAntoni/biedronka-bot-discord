import discord
from biedronkaClass import Biedronka
from discord.ext import commands

TOKEN = 'NzExMjMzNTY4OTAyMjE3ODU4.XsACLg.BvHWTXstjkVIFVDK4afH3cLAWXQ'
PREFIX = '!'

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print("I'm ready")

@bot.command()
async def b(ctx, *, request):
    try:
        b = Biedronka()
        b.requested_url(request)
        b.get_product()

        product = b.get_product().string.lower()
        price = b.get_price()

        print(f'Cena za {product} wynosi {price} zł')
        await ctx.send(f'Cena za {product} wynosi {price} zł')
    except:
        await ctx.send('Twojego produktu nie ma na stronie lub użyłeś polskich znaków :(')

bot.run(TOKEN)