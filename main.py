#Зона import
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config
#Конец зоны import

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
#Конец startvote




Bot.run(config.TOKEN)