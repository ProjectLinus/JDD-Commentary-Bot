import sys
import os
import random
import time
import Skype4Py
from constants import *
#import requests
#import selenium
#from bs4 import BeautifulSoup


"""
key das divas:
#pinkmew/$sexymirage;2cca35da2d6d400d
"""

file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "phrases.txt"),'r')
phrases = list(file)
file.close()

"""
Criei a classe SkypeGroup por questoes de organizacao, e possivelmente
sera util para alguns metodos em especifico
"""
class SkypeGroup:
    def __init__(self, topic, group):
        self.Topic = topic;
        self.Group = group;
        
    def getTopic(self):
        return self.Topic;
    
    def getGroup(self):
        return self.Group;
    

"""
Caso nao esteja aberto, abre uma instancia do skype, e associa
o programa a essa instancia
"""


def startSkype():
    instance = Skype4Py.Skype();
    if not instance.Client.IsRunning:
        instance.Client.Start();
    instance.Attach();
    return instance;


"""
Devolve uma lista que contem os chats de grupo existentes numa 
instancia do skype
"""

def getGroups(instance):
    
    groupList = [];
    for i in instance.Chats:
        topic = (i.Topic);
        if (topic != ""):
            newGroup = SkypeGroup(topic,i);
            groupList.append(newGroup);
    if (groupList != []):
        return groupList;



"""
Apresenta ao utilizador a lista dos grupos existentes na sua sessao 
de skype, pede ao utilizador para escolher para que grupo quer enviar
a sua mensagem, pede-lhe tambem a mensagem e envia-a para o grupo escolhido.
"""

def sendMessageGroup(group):
    
    instance = startSkype();
    if(group == -1):
        print("Grupo nao definido, por favor defina o grupo.\n");
        return;
    chat = getGroups(instance)[group].Group;
    msg = raw_input("Escreva a mensagem:\n").decode(sys.stdin.encoding);
    chat.SendMessage(msg);
    print("Mensagem enviada.\n");
    


"""
Mostra ao utilizador os chats de grupo existentes no seu skype e pede-lhe input
correspondente ao numero representativo desse chat. Caso esse numero nao seja
valido, o identificador do grupo e resetado para -1.
"""


def changeGroup():
    
    instance = startSkype();
    groupList = getGroups(instance);
    print("Grupos existentes: \n");
    for i in range(len(groupList)):
        print(str(i) + ": " + (groupList[i].Topic).encode("utf-8"));
    a = int(raw_input("Mudar para qual grupo? (introduzir o numero correspondente)\n"));
    if((a >= 0) and (a < len(groupList))):
        print("Grupo mudado para " + str(a) + "\n");
        return a;
    else:
        print("Grupo resetado, defina-o novamente.\n");
        return -1;
    
def teste(group):
    
    list = [];
    instance = startSkype();
    if(group == -1):
            print("Grupo nao definido, por favor defina o grupo.\n");
            return;
    chat = getGroups(instance)[group].Group;    
    for i in chat.RecentMessages:
        list.append((i.Body).encode("utf-8"));
    print(list[-1]);

    
"""
main function: executa-la para correr o programa
"""


def main():
    group = -1;
    menu = {};
    menu["0"] = "Exit";
    menu["1"] = "Send Message";
    menu["2"] = "Change Group";
    menu["3"] = "teste";
    
    while(1):
        options = menu.keys();
        options.sort();
        for i in options:
            print(i + ": " + menu[i]);
        select = raw_input("Qual o menu a escolher? ");
        if select == "0":
            print("A sair do programa...");
            break;        
        elif select == "1":
            sendMessageGroup(group);
        elif select == "2":
            group = changeGroup();
        elif select == "3":
            teste(group);
        else:
            print("Opcao invalida.\n");












def group_message(topic,text):
    
    client = Skype4Py.Skype()
    client.Attach()
    for i in client.ActiveChats:
        if len(i._GetMembers()) > 2 and i.Topic == topic:
            i.SendMessage(text)


def solo_message(receiver,text):
    
    skype = Skype4Py.Skype()
    skype.SendMessage(receiver,text)
    

def funcao_main(fich1,nome,limite,modo):
    
    fin = open(fich1, "r")
    lines = list(fin)
    fin.close()
    
    if modo == "group":
        for x in range(0,limite,1):
            output = gerador_texto(lines)
            group_message_true(nome,output)
    
    if modo == "solo":
        for x in range(0,limite,1):
            output = gerador_texto(lines)
            solo_message(nome,output)


def sms_wdelay(fich1,nome,limite,modo,delay):
    
    if limite == 0:
        while True:
            funcao_main(fich1,nome,1,modo)
            time.sleep(delay)
    else:
        x = 0
        while x < limite:
            funcao_main(fich1,nome,1,modo)
            x += 1
            time.sleep(delay)


            
            
def group_message_true(name,text):
    
    client = Skype4Py.Skype()
    client.Attach()
    for i in client.ActiveChats:
        if len(i._GetMembers()) > 2 and i.Name == name:
            i.SendMessage(text)

    
def sms_mood(username):

    client = Skype4Py.Skype()
    client.Attach()
    
    for i in client.Friends:
        if i._GetHandle() == username:
            moodtext = i._GetMoodText()
            solo_message(username,moodtext)


def read_last_message(idgroup):
    
    client = Skype4Py.Skype()
    client.Attach()
    
    for i in client.ActiveChats:
        if len(i._GetMembers()) > 2 and i.Name == idgroup:
            message_list = list(i.RecentMessages)
            last_message = message_list[-1]._GetBody().encode('latin1','ignore').decode('utf8','ignore').encode('utf8',"ignore").split()
            return last_message
        
        
def generate_phrase():
    phrase = phrases[random.randrange(len(phrases))]
    while("[" in phrase):
        term = (phrase.split('['))[1].split(']')[0]
        phrase = phrase.replace('[' + term + ']', constant_dic[term][random.randrange(len(constant_dic[term]))], 1)
    return phrase
                

                

def encontrar_palavra(lista,dictionary):
    
    for x in range(len(lista)):
        if lista[x] in dictionary:
            return lista[x]
        
    return ''



def filtra_texto(fich1,fich2,texto):
    
    fin = open(fich1, "r")
    lines = list(fin)
    lista_final = []
    
    for x in range(len(lines)):
        if (lines[x][0:len(texto)] != texto):
            lista_final.append(lines[x])
    fin.close()
    
    fout = open(fich2, "w")
    for x in range(len(lista_final)):
        fout.write(lista_final[x])
    fout.close()
    
    
def apaga_curtas(fich1,fich2):
    
    fin = open(fich1, "r")
    lines = list(fin)
    lista_final = []
    
    for x in range(len(lines)):
        if (len(lines[x]) > 9 and len(lines[x]) < 150):
            lista_final.append(lines[x])
    fin.close()
    
    fout = open(fich2, "w")
    for x in range(len(lista_final)):
        fout.write(lista_final[x])
    fout.close()
  

def gerador_texto(lista):
    
    random_variable = random.randrange(0,len(lista),1)
    texto = lista[random_variable]
    return texto
	
    
def jdd_text_sender(username,limit,delay):
    for x in range(0, limit, 1):
        output = generate_phrase()
        solo_message(username,output)
        time.sleep(delay)

        
group_message_true("test","123")