#Discord読み込み
import discord
import random
import time
from discord import Embed
from discord.ext import commands

chars1 = list("abcdefghijklmnopqrstuvwxyz" +
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
             "@@@" +
             "###" +
             "$$$" +
             "%%%%" +
             "&&&" +
             "!!!")

#指定
bot = commands.Bot(command_prefix=".",help_command=None,intents=discord.Intents.all())
first_embed = Embed(title='パスワードを送信します。',color=0x33e7ff)
new_embed = Embed(title='パスワードを作成しました。',color=0x33e7ff)


#Pass
@bot.command()
async def mpass(ctx):
    result = ''.join(random.choices(chars1, k=13))
    msg = await ctx.send(embed=first_embed)
    time.sleep(1)
    await ctx.send(result)
    time.sleep(1)
    await msg.edit(embed=new_embed)



bot.run('でぃすこーどとーくん')