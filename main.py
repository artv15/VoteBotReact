#Зона import
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import config
#Конец зоны import
global Y
global N
Y = 0
N = 0
Result = 'Похоже на ошибку. МИША БЛЯТЬ ПОЧИНИ УЖЕ ЕБАНЫЙ КОД!!!'
msgsent = ''
#Объявления префикса
Bot = commands.Bot(command_prefix= '!')
#Префикс объявлен

#Вывод объявления об активности
@Bot.event
async def on_ready():
    print('>>Bot started.')
#Сепаратор------------------------------------------

#Команда startvote
@Bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def startvote(ctx, arg):
    emb = discord.Embed(title=f'Начато голосование',
                        description='Голосуем за: ' + str(arg),
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    msgsent = ctx
    print('>>Sent message about voting. Voting for: ' + str(arg))
#Конец startvote

#Начало endvote
global n
global y
n = 0
y = 0
result = "?"

@Bot.event
async def on_raw_reaction_add(payload):  # №2
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji
        if emoji == "\N{WHITE HEAVY CHECK MARK}":
            y += 1
        elif emoji == "\N{CROSS MARK}":
            n += 1

@Bot.event  # № 1
async def on_raw_reaction_remove(payload):  # №2
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji # реакция пользователя
        if emoji == "\N{WHITE HEAVY CHECK MARK}":
            y -= 1
        elif emoji == "\N{CROSS MARK}":
            n -= 1

@Bot.command()  # № 4
@commands.has_permissions(administrator=True)
async def endvote(ctx):
    if y > n:
        result = 'Принято'  # № 5
    elif y == n:
        result = 'Отказано (Да = Нет)'  # № 5
    else:
        result = 'Отказано'  # № 5
    emb = discord.Embed(title=f'Окончено голосование.', description = 'Результат: ' + result, colour=discord.Color.purple())
    return await ctx.send(embed=emb) # **Возвращаем** сообщение после отправки.
    y, n = 0, 0
#Конец endvote


Bot.run(config.TOKEN)