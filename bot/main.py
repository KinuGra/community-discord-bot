from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を取得する権限

# Botをインスタンス化
bot = commands.Bot(
    command_prefix=['/', '.'], # / or . でコマンドを実行できるようになる
    case_insensitive=True, # コマンドの大文字小文字を区別しない（$helloも$Helloも同じ）
    intents=intents # 権限を設定
)

# bot正常起動時に一度だけ呼ばれる
@bot.event
async def on_ready():
    print(f"{bot.user} が起動しました")

    # cogsディレクトリの.pyファイルを全て読み込む
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# botの起動処理
load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    print("error: 環境変数が設定されていません")
else:
    bot.run(TOKEN)