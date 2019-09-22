# -*- coding: utf-8 -*-
import lcddriver
from time import *
import lcd_rus
import sys
from requests.auth import HTTPBasicAuth
import requests
from daemon import Daemon

class LCDDaemon(Daemon):
    def delchar(self,strtext):
        strtext = strtext.replace(chr(32),"")
        strtext = strtext.replace(chr(10),"")
        strtext = strtext.replace(chr(13),"")
        strtext = strtext.replace(" ","")
        strtext = strtext.replace("\t","")
        strtext = strtext.replace(u"↓","")
        strtext = strtext.replace(u"↑","")
        strtext = strtext.replace(u"mm.рт.ст.","")
        return strtext

    def setrestext(self,text,stringalph,restext):
        for ich in text:
            if((stringalph.find(ich)!=-1)&(restext.find(ich)==-1)):
                restext=restext+ich
        return restext

    def setdata(self,l,text1="",text2=""):
        list=[]
        if(text1!=""):
            list.append({'line':1,'text':text1})
        if(text2!=""):
            list.append({'line':2,'text':text2})
        stringalph = lcd_rus.getstringalph()
        restext = ''
        restext = self.setrestext(text1,stringalph,restext)
        restext = self.setrestext(text2,stringalph,restext)
        l.append({"list":list,"alltext":restext})

    def getdata(self):

        l = []

        r = requests.get('http://46.42.16.80/arduinonew/',auth=HTTPBasicAuth('Rootkit', 'InDiFfErEnCe'))
        alltext = r.text
        #Комната
        s = alltext.find(u'Tемпература =')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        textkom = alltext[:(f)].replace(u"Tемпература =","")
        textkom = self.delchar(textkom)
        alltext =  alltext[(f+3):]
        #Влажность комната
        s = alltext.find(u'Влажность =')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlkom = alltext[:(f)].replace(u"Влажность =","")
        vlkom = self.delchar(vlkom)
        alltext =  alltext[(f+3):]
        text1 = u"t Бкомн-"+str(textkom)
        text2 = u"% Бкомн-"+str(vlkom)
        self.setdata(l,text1,text2)

        #Tемпература на балконе
        s = alltext.find(u'Tемпература на балконе =')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        tbal = alltext[:(f)].replace(u"Tемпература на балконе =","")
        tbal = self.delchar(tbal)
        alltext =  alltext[(f+3):]
        #На балконе влажность
        s = alltext.find(u'На балконе влажность =')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlbal = alltext[:(f)].replace(u"На балконе влажность =","")
        vlbal = self.delchar(vlbal)
        alltext =  alltext[(f+3):]


        #Давление
        s = alltext.find(u'Давление =')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        press = alltext[:(f)].replace(u"Давление =","")
        if(press.find(u"↓")!=-1):
            d="|"
        elif(press.find(u"↑")!=-1):
            d="/"
        else:
            d=""
        press = self.delchar(press)
        alltext =  alltext[(f+3):]
        text1 = "    "+u"Атм.давл"+d
        text2 = " "+press.encode('ascii').decode('utf-8')+'mm.pt.st'
        self.setdata(l,text1,text2)
        #print(alltext)
        #Tемпература улица
        s = alltext.find(u'Tемпература улица')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        tul = alltext[:(f)].replace(u"Tемпература улица","")
        if(tul.find(u"↓")!=-1):
            d="|"
        elif(tul.find(u"↑")!=-1):
            d="/"
        else:
            d=""
        tul = self.delchar(tul)+d
        alltext =  alltext[(f+3):]
        #Влажность улица
        s = alltext.find(u'Влажность улица')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlul = alltext[:(f)].replace(u"Влажность улица","")
        vlul = self.delchar(vlul)
        alltext =  alltext[(f+3):]
        text1 = u"t улица-"+str(tul)
        text2 = u"% улица-"+str(vlul)
        self.setdata(l,text1,text2)

        #Температура коридор
        s = alltext.find(u'Коридор')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        tkor = alltext[:(f)].replace(u"Коридор","")
        tkor = self.delchar(tkor)
        alltext =  alltext[(f+3):]
        #Влажность коридор
        s = alltext.find(u'Влажность коридор')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlkor = alltext[:(f)].replace(u"Влажность коридор","")
        vlkor = self.delchar(vlkor)
        alltext =  alltext[(f+3):]
        text1 = u"t коридор-"+str(tkor)
        text2 = u"% коридор-"+str(vlkor)
        self.setdata(l,text1,text2)

        #Температура кухня
        s = alltext.find(u'Температура кухня')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        tkuh = alltext[:(f)].replace(u"Температура кухня","")
        tkuh = self.delchar(tkuh)
        alltext =  alltext[(f+3):]
        #Влажность кухня
        s = alltext.find(u'Влажность кухня')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlkuh = alltext[:(f)].replace(u"Влажность кухня","")
        vlkuh = self.delchar(vlkuh)
        alltext =  alltext[(f+3):]
        text1 = u"t кухня-"+str(tkuh)
        text2 = u"% кухня-"+str(vlkuh)
        self.setdata(l,text1,text2)

        #Температура маленькая комната
        s = alltext.find(u'Температура D1')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        tD1 = alltext[:(f)].replace(u"Температура D1","")
        tD1 = self.delchar(tD1)
        alltext =  alltext[(f+3):]
        #Влажность маленькая комната
        s = alltext.find(u'Влажность D1')
        alltext =  alltext[(s):]
        f = alltext.find('<br>')
        vlD1 = alltext[:(f)].replace(u"Влажность D1","")
        vlD1 = self.delchar(vlD1)
        alltext =  alltext[(f+3):]
        text1 = u"t Мкомн-"+str(tD1)
        text2 = u"% Мкомн-"+str(vlD1)
        self.setdata(l,text1,text2)


        return l

    def display(self,structtext,line,lcd):
        if (line==1):
            lcd.lcd_write(0x80)
        else:
            lcd.lcd_write(0xC0)
        for data in structtext['res']:
            if(data['type']==2):
                lcd.lcd_write_char(int(data['char']))
            else:
                lcd.lcd_display_string(data['char'],line,data['pos'])

    def run(self):
        i=0
        while(True):
            try:
                if(i==0):
                    data = self.getdata()
                for pak in data:
                    lcd = lcddriver.lcd()
                    lcd.lcd_clear()
                    st = lcd_rus.convertToRUSchar1602(pak['alltext'])
                    lcd.lcd_load_custom_chars(st['chardata'])
                    for l in pak['list']:
                        structtext = lcd_rus.convertToRUSchar1602(l['text'])
                        self.display(structtext,l['line'],lcd)
                    sleep(5)
                if(i==6):
                    i=-1
            except:
                lcd = lcddriver.lcd()
                lcd.lcd_clear()
                st = lcd_rus.convertToRUSchar1602(u'Ошибка!!!')
                lcd.lcd_load_custom_chars(st['chardata'])
                self.display(st,1,lcd)
                sleep(120)
            i+=1
if __name__ == "__main__":
    daemon = LCDDaemon('/var/run/LCDDaemon.pid')
    if 'start' == sys.argv[1]:
        daemon.start()
    elif 'stop' == sys.argv[1]:
        daemon.stop()
    elif 'restart' == sys.argv[1]:
        daemon.restart()
    else:
        print ("Unknown command")
        sys.exit(2)
        sys.exit(0)
    # text = u'Пак temp↑ *С!'
    # lcd.lcd_clear()
    # line = 1
    # structtext = lcd_rus.convertToRUSchar1602(text)
    # lcd.lcd_load_custom_chars(structtext['chardata'])
    # if (line==1):
    #     lcd.lcd_write(0x80)
    # else:
    #     lcd.lcd_write(0xC0)
    # for data in structtext['res']:
    #     print (data)
    #     if(data['type']==2):
    #         print(int(data['char']))
    #         lcd.lcd_write_char(int(data['char']))
    #     else:
    #         lcd.lcd_display_string(data['char'],line,data['pos'])
