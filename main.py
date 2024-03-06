import discord
from discord.ext import commands
from credits import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Бот запущен")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(message.content + "1")
    print(message.attachments)
    await bot.process_commands(message)


@bot.command("to_pm")
async def to_pm(ctx):
    user1 = await bot.fetch_user(ctx.author.id)
    await user1.send(f"Привет! Вот твой id: {ctx.author.id}")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!', file=discord.File('суи.jpeg'))


@bot.command()
async def hi(ctx):
    await ctx.send(f'Привет !')


bot.run('MTE1MjU3MTQ5ODQ5MDUwMzIzMA.GC8Njj.AFg6hb0G3aM5Zby5H7yhA3P3LTfZwrDmIp5UlA')