import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = """  

 _____           _        _              
|_   _|         | |      | |             
  | |  _ __  ___| |_ __ _| |_ __ _  __ _ 
  | | | '_ \/ __| __/ _` | __/ _` |/ _` |
 _| |_| | | \__ \ || (_| | || (_| | (_| |
|_____|_| |_|___/\__\__,_|\__\__,_|\__, |
   ___________________________________/ |
  |_____________________________________/ 
    
Instatag adalah sebuah tool yang bisa digunakan untuk mencari hastag terpopuler sesuai yang anda inginkan yang akan membantu bisnis instagram anda coded by Nor Ahmad
=========================================      
Author = Nor Ahmad
Ig = @norahm4d
Github = https://github.com/archive-code
Web = http://hepiweb.fun
=========================================
"""
print (asci)
hIG = input('Masukkan Hastag Instagram : ')
url = get("https://web.stagram.com/search?query=" + hIG)

soup = BeautifulSoup(url.text, 'html.parser')
tag = soup.find('div',{'class':'card-block text-center'})
try:
  hastag = tag.text.rstrip().lstrip()
except:
  print('Ada yang salah atau error')
print ('Link : https://www.instagram.com/'+hIG)
try:
  print ('=========================================')
  print ('Result dari hastag:'+ hIG)
  print (hastag)
except:
  exit
