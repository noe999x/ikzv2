import random,time,os,rich,sys,uuid,datetime
#for rich print as me
from datetime import datetime
from rich import print as noe
from rich.panel import Panel
from rich.console import Console
#For animation text
def anim(strings):
    for x in strings:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)
#Real Time
_monthz_ = ["January","February","March","April","May","June","July","August","September","October","November","December"][datetime.now().month - 1]
_days_   = {'Sunday':'Sunday','Monday':'Monday','Tuesday':'Tuesday','Wednesday':'Wednesday','Thursday':'Thursday','Friday':'Friday','Saturday':'Saturday'}[str(datetime.now().strftime("%A"))]
year = datetime.now().year
clock  = datetime.now().strftime("%X")
time_now = "%s %s %s"%(datetime.now().day,_monthz_,datetime.now().year)
#Clear
def clearall():
    os.system('clear')
#Logo
def Banner():
    Logo = '''[white] @noe999x [r][white]ikz update v1.2[reset]
\t                    [bold white] ____  ____  ____      
\t   ____  ____  ___  / __ \/ __ \/ __ \_  __
\t  / __ \/ __ \/ _ \/ /_/ / /_/ / /_/ / |/_/
\t / / / / /_/ /  __/\__, /\__, /\__, />  <  
\t/_/ /_/\____/\___//____//____//____/_/|_|
[r][red bold][i]• [white]Facebook.com/noe999x[white]\n[r][red bold]• [white]Github.com/noe999x\n[r][red bold]• [white]Youtube.com/c/Anonim404'''
    Console(width=58).print(Panel(Logo,style='white'))
#Fake_APikey

def apikey():
    try:clearall();Banner();noe(Panel.fit('[bold white]Real time : %s - %s %s'%(clock,_days_,time_now)));noe("\n[r][red] INFO [reset]\n[yellow]Free source code, create login generator code for user\nlogin, check on my github.com/noe999x\n[reset]")
    except:pass
    randomname=random.choice(['jamal','kipli','junedi','katak bijer','somat','agus','priadi','mang oleh','ependi','rusli','bagas ganteng','sodikin','doclang','perdi','basuki','jokow....','ilham','badrul','bontot','lucinta luna','rahmat','alex'])
    fakekey=uuid.uuid4() 
    noe(f'Siapa namamu? {randomname} kah?')
    username=input(' • Username : ') #untuk input usename pengguna
    if len(username) <=4:
         noe(f'[bold red]ngasal ya bang? jan gitu lah pantek, mana ada nama {username}.[reset]');time.sleep(3);apikey()
    anim(f'\tWelcome... {username}')
    noe('\nYour apikey :',fakekey) #output dari uuid
    password=input(' • Apikey : ') #untuk input apikey pengguna
    anim('\tPlease wait...') #jeda untuk tujuan selanjutnya
    if password==str(fakekey):
       time.sleep(2)
       noe('\n[green]Login Succes[reset]')
       open('/sdcard/noe999x/apikey.txt'.format(time_now),'a').write('Name   : %s\nApikey : %s'%(username,fakekey))
       time.sleep(2);os.system('python ikzv2.py') #tujuan selanjutnya
    else:
        password!=str(fakekey)
        time.sleep(2)
        noe('\n[red]Login failed, check again your apikey[reset]')
        os.system('rm -rf /sdcard/noe999x/apikey.txt')
        time.sleep(2);apikey() #loop apikey

def masuk():
    try:open('/sdcard/noe999x/apikey.txt','r').read();os.system('python ikzv2.py')
    except (FileNotFoundError):apikey()

if __name__ == "__main__":
  try:os.mkdir("/sdcard/noe999x")
  except:pass
  masuk()