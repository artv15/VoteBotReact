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
    print('>>Sent message about voting of event. Name of event: ' + str(arg))
#Конец startvote

#Начало endvote
@Bot.event
async def on_raw_reaction_add(self, payload):
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji
        if emoji == '✅':
            global Y
            Y += 1
        elif emoji == '❌':
            global N
            N += 1
async def on_raw_reaction_remove(self, payload):
    channel = Bot.get_channel(payload.channel_id) # получаем объект канала
    message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
    for emoji in message:
        emoji = payload.emoji # реакция пользователя
        if emoji == '✅':
            global Y
            Y -= 1
        elif emoji == '❌':
            global N
            N -= 1
if Y > N:
    Result = 'Принято'
elif Y == N:
    Result = 'Отказано(одинаковое кол-во голосов(Может быть ошибкой))'
else:
    Resule = 'Отказано'
@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def endvote(ctx):
    emb = discord.Embed(title=f'Окончено голосование на ивент', description = 'Результат: ' + str(Result), colour=discord.Color.purple())
    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
Y = 0
N = 0
#Конец endvote


Bot.run(config.TOKEN)