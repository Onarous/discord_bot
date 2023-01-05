import discord # Подключаем библиотеку
from discord.ext import commands

# a = 0

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='!', intents=intents)

# С помощью декоратора создаём первую команду
# @bot.command()
# async def ping(ctx):
#     global a
#     await ctx.send(a)
#     a +=1


# @bot.command()
# async def lol(ctx):
#     await ctx.send('kek')


# @bot.event
# async def on_message(message):
# # do some extra stuff here
#     await bot.process_commands(message)

#@bot.group(pass_context=True)
@bot.command()
async def re(ctx,num1:float, num2:float, sale:float):
    a = await ctx.send(num1 * num2 * (1 - (sale/100)))

bot.run('MTA1MzM2Mjc1ODc0NzQyMjgyMA.GVeHIv.o9IDmcRd7PGWCZa2kwdzUhKMoGCNizlCood78c')