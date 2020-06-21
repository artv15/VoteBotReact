#Зона import
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config
#Конец зоны import
Y = 0
N = 0
Result = 'Похоже на ошибку. МИША БЛЯТЬ ПОЧИНИ УЖЕ ЕБАНЫЙ КОД!!!'
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
    emb = discord.Embed(title=f'Начато голосование на ивент',
                        description='Ивент: ' + str(arg),
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    print('>>Sent message about voting of event. Name of event: ' + str(arg))
channel = 718792527230009374 # Получаем канал
message = await channel.fetch_message(payload.message_id)  # Получаем сообщение
author = message.author  # Получаем автора
if author == bot:
    async def on_raw_reaction_add(self, payload):
    emoji = payload.emoji # реакция пользователя
    if emoji == '✅':
        Y += 1
    if emoji == '❌':
        N += 1
#Конец startvote

#Начало endvote
if Y > N:
    Result = 'Принято'
elif Y == N:
    Result = 'Отказано(одинаковое кол-во голосов)'
else:
    Resule = 'Отказано'
@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def endvote(ctx)
    emb = discord.Embed(title=f'Окончено голосование на ивент'
                        description='Результат: ' + Result
                        colour=discord.color.purple())



Bot.run(config.TOKEN)