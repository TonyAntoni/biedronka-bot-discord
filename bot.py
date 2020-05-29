import discord
from biedronkaClass import Biedronka
from discord.ext import commands

TOKEN = ''
PREFIX = '@'

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

        product = b.get_product()
        price = b.get_price()
        link = b.get_url()
        basis_weight = b.get_basis_weight()
        amount = b.get_amount()

        if amount != None:
            amount = amount.string
        else:
            amount = ''

        embed = discord.Embed(colour = discord.Color.dark_red(), title = product)

        embed.add_field(name = 'Cena:', value=f'{price} zł{amount}', inline = True)

        if basis_weight != None:
            embed.add_field(name='Gramatura:', value=basis_weight)

        embed.add_field(name='LINK', value=f'[LINK]({link})', inline = True)
        embed.set_footer(text = 'BiedronkaBot powered by Antonji')

        print(f'{product} - {price} zł')
        await ctx.send(embed = embed)
    except:
        await ctx.send('Twojego produktu nie ma na stronie lub użyłeś polskich znaków lub wyjebało błąd i chuj :(')

bot.run(TOKEN)