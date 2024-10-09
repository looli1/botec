import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, num:int):
    await ctx.send(random.randint(1, int(num)))

@bot.command()
async def ecologi(ctx):
    facts = ['Около 12% поверхности нашей планеты имеют заповедный статус.', 'Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.', 'Переработка отходов важна не только потому, что это экономит ресурсы, но и потому, что обычный пластик разлагается в природе более 500 лет.', 'Повышение средней мировой температуры всего на 3-4 градуса может привести к таянию льдов, глобальному наводнению и исчезновению большей части лесов на Земле.', 'Более 50% мирового урожая зерна идёт на корм скоту и на производство биотоплива.', 'Для производства экологически чистых электромобилей используется масса вредных технологий, загрязняющих окружающую среду. В основном для производства их аккумуляторов.', 'Даже в крупном городе с грязным воздухом на улице он всё равно в 20-30 раз чище, чем в плохо проветриваемом помещении.', 'Солнечная энергия является наиболее экологически чистой, но для производства солнечных панелей всё равно используются продукты переработки нефти.']
    await ctx.send(random.choice(facts))

bot.run("token lol")
