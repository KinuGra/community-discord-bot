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

    # 再帰的に cogs/ 以下の .py ファイルをすべて読み込む
    cogs_root = os.path.join(os.path.dirname(__file__), "cogs")
    for root, dirs, files in os.walk(cogs_root):
        for file in files:
            if file.endswith(".py") and not file.startswith("_"):
                # cogs ディレクトリからの相対パスをモジュール名に変換
                rel_path = os.path.relpath(os.path.join(root, file), os.path.dirname(__file__))
                module_path = rel_path[:-3].replace(os.path.sep, ".")  # .pyを除去、/を.に
                try:
                    await bot.load_extension(module_path)
                    print(f"{module_path} を読み込みました")
                except Exception as e:
                    print(f"{module_path} の読み込みに失敗: {e}")

# botの起動処理
load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    print("error: 環境変数が設定されていません")
else:
    bot.run(TOKEN)