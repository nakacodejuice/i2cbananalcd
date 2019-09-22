# -*- coding: utf-8 -*-
from time import *
import lcd_rus
from requests.auth import HTTPBasicAuth
import requests

def delchar(strtext):
    strtext = strtext.replace(chr(32),"")
    strtext = strtext.replace(chr(10),"")
    strtext = strtext.replace(chr(13),"")
    strtext = strtext.replace(" ","")
    strtext = strtext.replace("\t","")
    strtext = strtext.replace(u"mm.рт.ст.","")
    return strtext

def setrestext(text,stringalph,rtext):
    # for ich in text:
        # if((stringalph.find(ich)!=-1)):
    print(text)
    return rtext+text


def setdata(l,text1="",text2=""):
    list=[]
    if(text1!=""):
        list.append({'line':1,'text':text1})
    if(text2!=""):
        list.append({'line':2,'text':text2})
    stringalph = lcd_rus.getstringalph()
    rtext = 'st'
    rtext = setrestext(text1,stringalph,rtext)
    rtext = setrestext(text2,stringalph,rtext)
    print("f"+rtext)
    l.append({"list":list,"alltext":rtext})

def getdata():

    l = []

    r = requests.get('http://46.42.16.80/arduinonew/',auth=HTTPBasicAuth('Rootkit', 'InDiFfErEnCe'))
    alltext = r.text
    #Комната
    s = alltext.find(u'Tемпература =')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    textkom = alltext[:(f)].replace(u"Tемпература =","")
    textkom = delchar(textkom)
    alltext =  alltext[(f+3):]
    #Влажность комната
    s = alltext.find(u'Влажность =')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlkom = alltext[:(f)].replace(u"Влажность =","")
    vlkom = delchar(vlkom)
    alltext =  alltext[(f+3):]
    text1 = u"t Бкомн-"+str(textkom)
    text2 = u"% Бкомн-"+str(vlkom)
    setdata(l,text1,text2)

    #Tемпература на балконе
    s = alltext.find(u'Tемпература на балконе =')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    tbal = alltext[:(f)].replace(u"Tемпература на балконе =","")
    tbal = delchar(tbal)
    alltext =  alltext[(f+3):]
    #На балконе влажность
    s = alltext.find(u'На балконе влажность =')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlbal = alltext[:(f)].replace(u"На балконе влажность =","")
    vlbal = delchar(vlbal)
    alltext =  alltext[(f+3):]


    #Давление
    s = alltext.find(u'Давление =')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    press = alltext[:(f)].replace(u"Давление =","")
    press = delchar(press)
    alltext =  alltext[(f+3):]
    text1 = u"Атм.дав"
    text2 = str(press)+u"мм.рт.ст"
    print(press.encode().decode('utf-8'))
    setdata(l,text1,text2)
    #print(alltext)
    #Tемпература улица
    s = alltext.find(u'Tемпература улица')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    tul = alltext[:(f)].replace(u"Tемпература улица","")
    tul = delchar(tul)
    alltext =  alltext[(f+3):]
    #Влажность улица
    s = alltext.find(u'Влажность улица')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlul = alltext[:(f)].replace(u"Влажность улица","")
    vlul = delchar(vlul)
    alltext =  alltext[(f+3):]
    text1 = u"t улица-"+str(tul)
    text2 = u"% улица-"+str(vlul)
    setdata(l,text1,text2)

    #Температура коридор
    s = alltext.find(u'Коридор')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    tkor = alltext[:(f)].replace(u"Коридор","")
    tkor = delchar(tkor)
    alltext =  alltext[(f+3):]
    #Влажность коридор
    s = alltext.find(u'Влажность коридор')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlkor = alltext[:(f)].replace(u"Влажность коридор","")
    vlkor = delchar(vlkor)
    alltext =  alltext[(f+3):]
    text1 = u"t коридор-"+str(tkor)
    text2 = u"% коридор-"+str(vlkor)
    setdata(l,text1,text2)

    #Температура кухня
    s = alltext.find(u'Температура кухня')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    tkuh = alltext[:(f)].replace(u"Температура кухня","")
    tkuh = delchar(tkuh)
    alltext =  alltext[(f+3):]
    #Влажность кухня
    s = alltext.find(u'Влажность кухня')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlkuh = alltext[:(f)].replace(u"Влажность кухня","")
    vlkuh = delchar(vlkuh)
    alltext =  alltext[(f+3):]
    text1 = u"t кухня-"+str(tkuh)
    text2 = u"% кухня-"+str(vlkuh)
    setdata(l,text1,text2)

    #Температура маленькая комната
    s = alltext.find(u'Температура D1')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    tD1 = alltext[:(f)].replace(u"Температура D1","")
    tD1 = delchar(tD1)
    alltext =  alltext[(f+3):]
    #Влажность маленькая комната
    s = alltext.find(u'Влажность D1')
    alltext =  alltext[(s):]
    f = alltext.find('<br>')
    vlD1 = alltext[:(f)].replace(u"Влажность D1","")
    vlD1 = delchar(vlD1)
    alltext =  alltext[(f+3):]
    text1 = u"t Мкомн-"+str(tD1)
    text2 = u"% Мкомн-"+str(vlD1)
    setdata(l,text1,text2)


    return l

def display(structtext,line):
    print("hello")
    # if (line==1):
    #     lcd.lcd_write(0x80)
    # else:
    #     lcd.lcd_write(0xC0)
    # for data in structtext['res']:
    #     if(data['type']==2):
    #         lcd.lcd_write_char(int(data['char']))
    #     else:
    #         lcd.lcd_display_string(data['char'],line,data['pos'])

if __name__ == "__main__":
    i=0
    while(True):
        data = getdata()
        for pak in data:
            #lcd = lcddriver.lcd()
            #lcd.lcd_clear()
            print("all"+pak['alltext'])
            st = lcd_rus.convertToRUSchar1602(pak['alltext'])
            #lcd.lcd_load_custom_chars(st['chardata'])
            for l in pak['list']:
                structtext = lcd_rus.convertToRUSchar1602(l['text'])
                display(structtext,l['line'])
            sleep(5)
        i+=1
