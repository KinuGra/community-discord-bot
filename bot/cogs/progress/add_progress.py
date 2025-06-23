from discord.ext import commands
import discord
from mysql.connector import Error
from db.queries import insert_progress

class Progress(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add_progress", aliases=["ap"])
    async def add_progress(self, ctx, title: str, *, detail: str = ""):
        """進捗を記録する 使い方：/ap タイトル [詳細（省略可）]"""
        author_id = ctx.author.id
        try:
            insert_progress(author_id, title, detail)
            await ctx.send(f"進捗を記録しました : {title}")
        except Error as err:
            if len(title) > 100:
                await ctx.send("titleは100文字以内で入力してください")
            else:
                await ctx.send("ERROR: add_progress")
                print(err)

# Cogをセットアップする関数
async def setup(bot):
    await bot.add_cog(Progress(bot))