#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import telepot
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton ,InlineKeyboardMarkup , InlineKeyboardButton ,ReplyKeyboardRemove
import time
import sys
import os
import numpy as np
import requests 
import csv
import requests
import  email
import smtplib  


bot = telepot.Bot('996900145:AAGsx_EoL1-D68sTLZGZWGm305wPhCMpep0')
dicts = {}#state of person
dicts_Fname = {}#1
dicts_Lname = {}#2
dicts_Email = {}
dicts_phone = {}#3
dicts_mobile = {}#11
dicts_birthday = {}#4
dicts_madrak = {}#5
dicts_job = {}#6
dicts_position = {}#7
dicts_method = {}#8
dicts_goal = {}#9
dicts_expect = {}#10
dicts_ie = {}
dicts_sn = {}
dicts_tf = {}
dicts_pj= {}
dicts_tip= {}
listF = []

listF.append(('chat ID','state','first name','last name','e-mail','phone no.','mobile no.','birthday date','degree','job','post','way of introdution','goal','expect','ie','sn','tf','pj','tip'))
tmp = {}



def inserTolist(i):
    listF.append((i,dicts[i],dicts_Fname[i],dicts_Lname[i],dicts_Email[i],dicts_phone[i],dicts_mobile[i],dicts_birthday[i],dicts_madrak[i],dicts_job[i],dicts_position[i],dicts_method[i],dicts_goal[i],dicts_expect[i],dicts_ie[i],dicts_sn[i],dicts_tf[i],dicts_pj[i],dicts_tip[i]))
    print("insert down")

def readFromlist():
    tmp=0
    for i in range(0,len(listF)):
        if i==0: 
            continue
        tmp=listF[i][0]
        dicts[tmp] = listF[i][1]
        print(dicts[tmp])
        dicts_Fname[tmp] = listF[i][2]
        dicts_Lname[tmp] = listF[i][3]
        dicts_Email[tmp] = listF[i][4]
        dicts_phone[tmp] = listF[i][5]
        dicts_mobile[tmp] = listF[i][6]
        dicts_birthday[tmp] = listF[i][7]
        dicts_madrak[tmp] = listF[i][8]
        dicts_job[tmp] = listF[i][9]
        dicts_position[tmp] = listF[i][10]
        dicts_method[tmp] = listF[i][11]
        dicts_goal[tmp] = listF[i][12]
        dicts_expect[tmp] = listF[i][13]
        dicts_ie[tmp] = listF[i][14]
        dicts_sn[tmp] = listF[i][15]
        dicts_tf[tmp] = listF[i][16]
        dicts_pj[tmp] = listF[i][17]
        dicts_tip[tmp] = listF[i][18]

        

def saveToCSV():
    with open('person.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(listF)
    csvFile.close()
def loadFormCSV():    
    with open('person.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for item in reader:
            listF.append(item)


# url = 'http://smsg.ir/index2.php?goto=webservice/json&method=send&arg1=ali&arg2=maedeh&arg3=09397201006&arg4=30001341213594&arg5='
# resp = requests.get(url)
# print(resp.text)

# initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
loadFormCSV()
print(listF)
readFromlist()
print(dicts)

def cmp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]

def handle(msg):

        content_type, chat_type, chat_id = telepot.glance(msg)
        print(chat_id)
        if chat_id in dicts:
                print('in in in!')
        # print(dicts[chat_id])        

        
#initialazation  phaze
        if content_type == 'text':
                if msg['text'] == 'save':
                        # saveToCSV()
                        bot.sendDocument(chat_id,document=open('person.csv', 'rb'))
                        print('sent')
        if chat_id in dicts :
                # initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # initialization----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                if tmp[chat_id] == 1 :
                        dicts_Fname[chat_id] = msg['text']
                        bot.sendMessage(chat_id, " لطفا نام خانوادگی خود را بنویسید")
                        dicts[chat_id] = 2
                        print("end of p 2")


                if tmp[chat_id] == 2 :
                        dicts_Lname[chat_id] = msg['text']
                        bot.sendMessage(chat_id,dicts_Fname[chat_id]+" "+dicts_Lname[chat_id]+ " عزیز لطفا شماره ی تلفن منزلتان را با اعداد انگلیسی وارد کنید")
                        dicts[chat_id] = 31
                        print("end of p 3")
                

                if tmp[chat_id] == 31 :
                        dicts_phone[chat_id] = msg['text']
                        bot.sendMessage(chat_id,dicts_Fname[chat_id]+" "+dicts_Lname[chat_id]+ " عزیز لطفا آدرس ایمیل خود را وارد کنید")
                        dicts[chat_id] = 3
                        print("end of p 3۱")
                
                if tmp[chat_id] == 3 :
                        dicts_Email[chat_id] = msg['text']
                        bot.sendMessage(chat_id, "جناب "+dicts_Fname[chat_id]+" "+dicts_Lname[chat_id]+ " لطفا تاریخ تولدتان را با اعداد انگلسی مانند نمونه وارد کنید( نمونه:1399/10/1 !) ")
                        dicts[chat_id] = 4
                        print("end of p 4")


                if tmp[chat_id] == 4 :
                        dicts_birthday[chat_id] = msg['text']
                        keyboard = ReplyKeyboardMarkup(keyboard=[['زیر دیپلم','دیپلم', 'فوق دیپلم'], ['لیسانس','فوق لیسانس', 'دکتری']])
                        bot.sendMessage(chat_id, " لطفا آخرین مدرک تحصیلیتان را انتخاب کنید",reply_markup = keyboard)
                        dicts[chat_id] = 5
                        print("end of p 5")
                
                if tmp[chat_id] == 5 :
                        dicts_madrak[chat_id] = msg['text']
                        bot.sendMessage(chat_id, "لطفا شغلتان را بنویسید",reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
                        dicts[chat_id] = 6
                        print("end of p 6")

                if tmp[chat_id] == 6 :
                        dicts_job[chat_id] = msg['text']
                        bot.sendMessage(chat_id, "لطفا سمتتان را بنویسید")
                        dicts[chat_id] = 7
                        print("end of p 7")        
                
                if tmp[chat_id] == 7 :
                        dicts_position[chat_id] = msg['text']
                        bot.sendMessage(chat_id, "چگونه با کلنیک آرامش مالی آشنا شدید؟")
                        dicts[chat_id] = 8
                        print("end of p 8") 

                if tmp[chat_id] == 8 :
                        dicts_method[chat_id] = msg['text']
                        bot.sendMessage(chat_id, "هدف شما از شرکت در این دوره چیست؟")
                        dicts[chat_id] = 9
                        print("end of p 9") 


                if tmp[chat_id] == 9 :
                        dicts_goal[chat_id] = msg['text']
                        bot.sendMessage(chat_id,"انتظار دارید پس از پایان دوره به چه دست آورد هایی برسید؟")
                        dicts[chat_id] = 10
                        print("end of p 10") 


                if tmp[chat_id] == 10 :
                        dicts_expect[chat_id] = msg['text']
                        bot.sendMessage(chat_id,"شماره ی تلفن همراه خود را با اعداد انگلیسی وارد کنید")
                        dicts[chat_id] = 11
                        print("end of p 11") 


                if tmp[chat_id] == 11 :
                        dicts_mobile[chat_id] = msg['text']
                        bot.sendMessage(chat_id,"یک کد فعال سازی به شماره ی شما پیامک خواهد شد لطفا برای شروع آزمون آنرا با اعداد انگلیسی وارد کنید")
                        u1 = 'http://smsg.ir/index2.php?goto=webservice/json&method=send&arg1=ali&arg2=maedeh&arg3='
                        no = dicts_mobile[chat_id]
                        u2 = '&arg4=30001341213594&arg5='
                        msg= 'سلام\n کد فعالسازی:\n '+str(chat_id)+' \nبا احترام. کلینیک آرامش مالی'
                        uu = u1+no+u2+msg
                        resp = requests.get(uu)
                        dicts[chat_id] = 12
                        print("end of p 12") 
                        saveToCSV()
                
                if tmp[chat_id] == 12 :
                        print(msg['text'])
                        print(chat_id)
                        if msg['text']==str(chat_id) or msg['text']=='cheat':
                                bot.sendMessage(chat_id,"با تشکر از همکاری شما . لطفا به ۶۰ پرسش که در ادامه می آید با دقت و در زمان حدود ۱۵ دقیقه پاسخ دهید")
                                # q1
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً احساسات و عواطف خود را در خويش نگه می دارم.'], ['معمولاً احساسات و عواطف خودرا با ديگران و به راحتی درميان مي گذارم. ']])
                                bot.sendMessage(chat_id, " سوال اول: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts[chat_id] = 101
                                dicts_ie[chat_id] = 0
                                dicts_sn[chat_id] = 0
                                dicts_tf[chat_id] = 0
                                dicts_pj[chat_id] = 0
                        else :
                                bot.sendMessage(chat_id,"کد وارد شده اشتباه است لطفا دوباره تلاش کنید. اگر شماره ی تلفنتان را اشتباه وارد کرده اید حرف «r» را وارد کنید")    
                                dicts[chat_id] = 12

                        if msg['text']=='r' or msg['text']=='R':
                                dicts[chat_id] = 10


    
                        print("end of p 13") 

                # Questions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # Questions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # Questions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # Questions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                if tmp[chat_id] == 101 :
                        # r1
                        if cmp(msg['text'] , 'معمولاً احساسات و عواطف خود را در خويش نگه می دارم.') :
                                # q2
                                keyboard = ReplyKeyboardMarkup(keyboard=[['براي من امور قطعی، عينی و مشخص مهم هستند. '], ['براي من ايده ها، استنباط ها و الهامات مهم هستند.']])
                                bot.sendMessage(chat_id, " سوال دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 102
                        elif cmp(msg['text'] , 'معمولاً احساسات و عواطف خودرا با ديگران و به راحتی درميان مي گذارم. ' ):
                                # q2
                                keyboard = ReplyKeyboardMarkup(keyboard=[['براي من امور قطعی، عينی و مشخص مهم هستند. '], ['براي من ايده ها، استنباط ها و الهامات مهم هستند.']])
                                bot.sendMessage(chat_id, " سوال دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts[chat_id] = 102

                        else : 
                                tmp[chat_id] = 100    
                        print("end of p 101")




                if tmp[chat_id] == 102 :
                        # r2
                        if cmp(msg['text'] , 'براي من امور قطعی، عينی و مشخص مهم هستند. ' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هنگام تصميم گيری به آنچه که منطق و خرد بر آن حکم می کند، عمل می کنم.'], ['هنگام تصميم گيری به آنچه که احساسات و دلم گواه می دهد، عمل می کنم.']])
                                bot.sendMessage(chat_id, " سوال سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 103
                        elif cmp(msg['text'] , 'براي من ايده ها، استنباط ها و الهامات مهم هستند.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هنگام تصميم گيری به آنچه که منطق و خرد بر آن حکم می کند، عمل می کنم.'], ['هنگام تصميم گيری به آنچه که احساسات و دلم گواه می دهد، عمل می کنم.']])
                                dicts[chat_id] = 103
                                bot.sendMessage(chat_id, " سوال سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100     
                        print("end of p 102")        




                if tmp[chat_id] == 103 :
                        # r3
                        if cmp(msg['text'] , 'هنگام تصميم گيری به آنچه که منطق و خرد بر آن حکم می کند، عمل می کنم.') :
                                # q4
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم در شرايط انعطاف پذير و متغيری زندگی کنم.'], ['دوست دارم همه چيز منظم و برنامه ريزی شده باشد.']])
                                bot.sendMessage(chat_id, " سوال چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 104
                        elif cmp(msg['text'] , 'هنگام تصميم گيری به آنچه که احساسات و دلم گواه می دهد، عمل می کنم.') :
                                # q4
                                dicts[chat_id] = 104
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم در شرايط انعطاف پذير و متغيری زندگی کنم.'], ['دوست دارم همه چيز منظم و برنامه ريزی شده باشد.']])
                                bot.sendMessage(chat_id, " سوال چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 103")




                if tmp[chat_id] == 104 :
                        # r4
                        if cmp(msg['text'] , 'دوست دارم در شرايط انعطاف پذير و متغيری زندگی کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم در زمينه های محدودی اطلاعات داشته باشم ولي در هر زمينه عميق و کامل.'], ['دوست دارم در زمينه های زيادی اطلاعات داشته باشم ولی در هر زمينه تا حد کم و سطحی.']])
                                bot.sendMessage(chat_id, " سوال پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 105
                        elif cmp(msg['text'] , 'دوست دارم همه چيز منظم و برنامه ريزی شده باشد.') :
                                # q3
                                dicts[chat_id] = 105
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم در زمينه های محدودی اطلاعات داشته باشم ولي در هر زمينه عميق و کامل.'], ['دوست دارم در زمينه های زيادی اطلاعات داشته باشم ولی در هر زمينه تا حد کم و سطحی.']])
                                bot.sendMessage(chat_id, " سوال پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")
         



                if tmp[chat_id] == 105 :
                        # r5
                        if cmp(msg['text'] , 'دوست دارم در زمينه های محدودی اطلاعات داشته باشم ولي در هر زمينه عميق و کامل.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر اوقات به واقعيات عينی (آنچه که وجود دارد ) توجه می کنم. '], ['بيشتر اوقات حقايق ( آنچه که بايد وجود داشته باشد ) را در ذهن و تخيل خود مجسم مي کنم.']])
                                bot.sendMessage(chat_id, " سوال ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 106
                        elif cmp(msg['text'] , 'دوست دارم در زمينه های زيادی اطلاعات داشته باشم ولی در هر زمينه تا حد کم و سطحی.') :
                                # q3
                                dicts[chat_id] = 106
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر اوقات به واقعيات عينی (آنچه که وجود دارد ) توجه می کنم. '], ['بيشتر اوقات حقايق ( آنچه که بايد وجود داشته باشد ) را در ذهن و تخيل خود مجسم مي کنم.']])
                                bot.sendMessage(chat_id, " سوال ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 106:
                        # r6
                        if cmp(msg['text'] , 'بيشتر اوقات به واقعيات عينی (آنچه که وجود دارد ) توجه می کنم. ') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از نظر من يک قاضی و داور عادل براي جامعه مفيدتر است.'], ['از نظر من يک معلم و مربی مهربان برای جامعه مفيدتر است.']])
                                bot.sendMessage(chat_id, " سوال هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 107
                        elif cmp(msg['text'] , 'بيشتر اوقات حقايق ( آنچه که بايد وجود داشته باشد ) را در ذهن و تخيل خود مجسم مي کنم.') :
                                # q3
                                dicts[chat_id] = 107
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از نظر من يک قاضی و داور عادل براي جامعه مفيدتر است.'], ['از نظر من يک معلم و مربی مهربان برای جامعه مفيدتر است.']])
                                bot.sendMessage(chat_id, " سوال هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 107 :
                        # r7
                        if cmp(msg['text'] , 'از نظر من يک قاضی و داور عادل براي جامعه مفيدتر است.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ترجيحاً ملاقاتها و ديدارهای خود را بدون برنامه قبلی و آزادانه انجام می دهم. '], ['ترجيحاً ديدار با افراد و وعده ملاقات خود را از پيش تعيين می کنم.']])
                                bot.sendMessage(chat_id, " سوال هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 108
                        elif cmp(msg['text'] , 'از نظر من يک معلم و مربی مهربان برای جامعه مفيدتر است.') :
                                # q3
                                dicts[chat_id] = 108
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ترجيحاً ملاقاتها و ديدارهای خود را بدون برنامه قبلی و آزادانه انجام می دهم. '], ['ترجيحاً ديدار با افراد و وعده ملاقات خود را از پيش تعيين می کنم.']])
                                bot.sendMessage(chat_id, " سوال هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 108 :
                        # r8
                        if cmp(msg['text'] , 'ترجيحاً ملاقاتها و ديدارهای خود را بدون برنامه قبلی و آزادانه انجام می دهم. ') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کم حرف و محتاط هستم و علاقه ای به جلب توجه ديگران به خود ندارم.'], ['توجه ديگران را به خود جلب می کنم.']])
                                bot.sendMessage(chat_id, " سوال نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 109
                        elif cmp(msg['text'] , 'ترجيحاً ديدار با افراد و وعده ملاقات خود را از پيش تعيين می کنم.') :
                                # q3
                                dicts[chat_id] = 109
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کم حرف و محتاط هستم و علاقه ای به جلب توجه ديگران به خود ندارم.'], ['توجه ديگران را به خود جلب می کنم.']])
                                bot.sendMessage(chat_id, " سوال نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 109 :
                        # r9
                        if cmp(msg['text'] , 'کم حرف و محتاط هستم و علاقه ای به جلب توجه ديگران به خود ندارم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['اگر معلم بودم ترجيح می دادم دروسي را تدريس کنم که واقعيات و امور قطعی وعينی را شامل شوند.'], ['اگر معلم بودم، ترجيحاً دروسی را تدريس می کردم که حقايق و نظريه ها و تئوری ها را شامل شوند (مانند فلسفه).']])
                                bot.sendMessage(chat_id, " سوال دهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 110
                        elif cmp(msg['text'] , 'توجه ديگران را به خود جلب می کنم.') :
                                # q3
                                dicts[chat_id] = 110
                                keyboard = ReplyKeyboardMarkup(keyboard=[['اگر معلم بودم ترجيح می دادم دروسي را تدريس کنم که واقعيات و امور قطعی وعينی را شامل شوند.'], ['اگر معلم بودم، ترجيحاً دروسی را تدريس می کردم که حقايق و نظريه ها و تئوری ها را شامل شوند (مانند فلسفه).']])
                                bot.sendMessage(chat_id, " سوال دهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 110 :
                        # r10
                        if cmp(msg['text'] , 'اگر معلم بودم ترجيح می دادم دروسي را تدريس کنم که واقعيات و امور قطعی وعينی را شامل شوند.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['قاطع، محکم و استوار هستم.'], ['انعطاف پذير ، ملايم و لطيف هستم. ']])
                                bot.sendMessage(chat_id, " سوال یازدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 111
                        elif cmp(msg['text'] , 'اگر معلم بودم، ترجيحاً دروسی را تدريس می کردم که حقايق و نظريه ها و تئوری ها را شامل شوند (مانند فلسفه).') :
                                # q3
                                dicts[chat_id] = 111
                                keyboard = ReplyKeyboardMarkup(keyboard=[['قاطع، محکم و استوار هستم.'], ['انعطاف پذير ، ملايم و لطيف هستم. ']])
                                bot.sendMessage(chat_id, " سوال یازدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 111 :
                        # r11
                        if cmp(msg['text'] , 'قاطع، محکم و استوار هستم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['غالباً انجام کارهای پيش پا افتاده و جزئی را فراموش می کنم.'], ['به منظور جلوگيری از فراموش شدن انجام کارها، آن ها را يادداشت می کنم.']])
                                bot.sendMessage(chat_id, " سوال دوازدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 112
                        elif cmp(msg['text'] , 'انعطاف پذير ، ملايم و لطيف هستم. ') :
                                # q3
                                dicts[chat_id] = 112
                                keyboard = ReplyKeyboardMarkup(keyboard=[['غالباً انجام کارهای پيش پا افتاده و جزئی را فراموش می کنم.'], ['به منظور جلوگيری از فراموش شدن انجام کارها، آن ها را يادداشت می کنم.']])
                                bot.sendMessage(chat_id, " سوال دوازدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 112 :
                        # r12
                        if cmp(msg['text'] , 'غالباً انجام کارهای پيش پا افتاده و جزئی را فراموش می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در مهمانی ها، جلسات وگردهمايی ها منتظر مي مانم تا ديگران به سوی من بيايند.'], ['در مهماني ها، جلسات وگردهمايی ها من سر صحبت را با ديگران باز می کنم.']])
                                bot.sendMessage(chat_id, " سوال سیزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 113
                        elif cmp(msg['text'] , 'به منظور جلوگيری از فراموش شدن انجام کارها، آن ها را يادداشت می کنم.') :
                                # q3
                                dicts[chat_id] = 113
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در مهمانی ها، جلسات وگردهمايی ها منتظر مي مانم تا ديگران به سوی من بيايند.'], ['در مهماني ها، جلسات وگردهمايی ها من سر صحبت را با ديگران باز می کنم.']])
                                bot.sendMessage(chat_id, " سوال سیزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 113 :
                        # r13
                        if cmp(msg['text'] , 'در مهمانی ها، جلسات وگردهمايی ها منتظر مي مانم تا ديگران به سوی من بيايند.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به جزئيات امور توجه زيادی دارم.'], ['بيشتر کليت هر موضوعی برايم مهم است و به جزئيات آن توجه زيادی نمی کنم.']])
                                bot.sendMessage(chat_id, " سوال چهاردهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 114
                        elif cmp(msg['text'] , 'در مهماني ها، جلسات وگردهمايی ها من سر صحبت را با ديگران باز می کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به جزئيات امور توجه زيادی دارم.'], ['بيشتر کليت هر موضوعی برايم مهم است و به جزئيات آن توجه زيادی نمی کنم.']])
                                dicts[chat_id] = 114
                                bot.sendMessage(chat_id, " سوال چهاردهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 114 :
                        # r14
                        if cmp(msg['text'] , 'به جزئيات امور توجه زيادی دارم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به آينده اهميت زيادی داده و  برای آن برنامه ريزی می کنم.'], ['خيلی به آينده فکر نمی کنم.']])
                                bot.sendMessage(chat_id, " سوال پانزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 115
                        elif cmp(msg['text'] , 'بيشتر کليت هر موضوعی برايم مهم است و به جزئيات آن توجه زيادی نمی کنم.') :
                                # q3
                                dicts[chat_id] = 115
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به آينده اهميت زيادی داده و  برای آن برنامه ريزی می کنم.'], ['خيلی به آينده فکر نمی کنم.']])
                                bot.sendMessage(chat_id, " سوال پانزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 115 :
                        # r15
                        if cmp(msg['text'] , 'به آينده اهميت زيادی داده و  برای آن برنامه ريزی می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً کارها را شروع می کنم و حين اجرا به رفع اشکالات اجرايی وتدارک مورد نياز می پردازم.'], ['قبل از اجرای طرح ها وکارها برنامه ريزی  انجام می دهم.']])
                                bot.sendMessage(chat_id, " سوال شانزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 116
                        elif cmp(msg['text'] , 'خيلی به آينده فکر نمی کنم.') :
                                # q3
                                dicts[chat_id] = 116
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً کارها را شروع می کنم و حين اجرا به رفع اشکالات اجرايی وتدارک مورد نياز می پردازم.'], ['قبل از اجرای طرح ها وکارها برنامه ريزی  انجام می دهم.']])
                                bot.sendMessage(chat_id, " سوال شانزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 116 :
                        # r16
                        if cmp(msg['text'] , 'معمولاً کارها را شروع می کنم و حين اجرا به رفع اشکالات اجرايی وتدارک مورد نياز می پردازم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['مايل هستم دوستان کم همراه با ارتباط زياد و صميمانه داشته باشم.'], ['مايل هستم دوستان زياد همراه با ارتباط محدود داشته باشم.']])
                                bot.sendMessage(chat_id, " سوال هفدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 117
                        elif cmp(msg['text'] , 'قبل از اجرای طرح ها وکارها برنامه ريزی  انجام می دهم.') :
                                # q3
                                dicts[chat_id] = 117
                                keyboard = ReplyKeyboardMarkup(keyboard=[['مايل هستم دوستان کم همراه با ارتباط زياد و صميمانه داشته باشم.'], ['مايل هستم دوستان زياد همراه با ارتباط محدود داشته باشم.']])
                                bot.sendMessage(chat_id, " سوال هفدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 117 :
                        # r17
                        if cmp(msg['text'] , 'مايل هستم دوستان کم همراه با ارتباط زياد و صميمانه داشته باشم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به استفاده از امکانات و توانايی های موجود تاکيد دارم.'], ['نوآوری و خلاقيت داشتن در کارها برايم اولويت دارد.']])
                                bot.sendMessage(chat_id, " سوال هجدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 118
                        elif cmp(msg['text'] , 'مايل هستم دوستان زياد همراه با ارتباط محدود داشته باشم.') :
                                # q3
                                dicts[chat_id] = 118
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به استفاده از امکانات و توانايی های موجود تاکيد دارم.'], ['نوآوری و خلاقيت داشتن در کارها برايم اولويت دارد.']])
                                bot.sendMessage(chat_id, " سوال هجدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 118 :
                        # r18
                        if cmp(msg['text'] , 'به استفاده از امکانات و توانايی های موجود تاکيد دارم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر پيرو منطق و دليل هستم.'], ['بيشتر پيرو احساس و عاطفه هستم. ']])
                                bot.sendMessage(chat_id, " سوال نوزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 119
                        elif cmp(msg['text'] , 'نوآوری و خلاقيت داشتن در کارها برايم اولويت دارد.') :
                                # q3
                                dicts[chat_id] = 119
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر پيرو منطق و دليل هستم.'], ['بيشتر پيرو احساس و عاطفه هستم. ']])
                                bot.sendMessage(chat_id, " سوال نوزدهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 119 :
                        # r19
                        if cmp(msg['text'] , 'بيشتر پيرو منطق و دليل هستم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در انجام کارهايی که از قبل پيش بينی نشده و يا فعاليت هايی که به سرعت و عکس العمل فوری نياز دارد، موفق هستم.'], ['در انجام کارهايی که بر اساس طرح و برنامه قبلی مي باشد موفق هستم.']])
                                bot.sendMessage(chat_id, " سوال بیستم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 120
                        elif cmp(msg['text'] , 'بيشتر پيرو احساس و عاطفه هستم. ') :
                                # q3
                                dicts[chat_id] = 120
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در انجام کارهايی که از قبل پيش بينی نشده و يا فعاليت هايی که به سرعت و عکس العمل فوری نياز دارد، موفق هستم.'], ['در انجام کارهايی که بر اساس طرح و برنامه قبلی مي باشد موفق هستم.']])
                                bot.sendMessage(chat_id, " سوال بیستم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 120 :
                        # r20
                        if cmp(msg['text'] , 'در انجام کارهايی که از قبل پيش بينی نشده و يا فعاليت هايی که به سرعت و عکس العمل فوری نياز دارد، موفق هستم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به طور معمول دوستان کمی داشته ولي روابط صميمانه ای با آنها دارم.'], ['به طور معمول با افراد زيادی دوستی و آشنايی دارم.']])
                                bot.sendMessage(chat_id, " سوال بیست و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 121
                        elif cmp(msg['text'] , 'در انجام کارهايی که بر اساس طرح و برنامه قبلی مي باشد موفق هستم.') :
                                # q3
                                dicts[chat_id] = 121
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به طور معمول دوستان کمی داشته ولي روابط صميمانه ای با آنها دارم.'], ['به طور معمول با افراد زيادی دوستی و آشنايی دارم.']])
                                bot.sendMessage(chat_id, " سوال بیست و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 121 :
                        # r21
                        if cmp(msg['text'] , 'به طور معمول دوستان کمی داشته ولي روابط صميمانه ای با آنها دارم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['عمدتا از زندگی در زمان حال لذت زيادی برده و خيلي به آينده فکر نمی کنم.'], ['به آينده توجه زيادي داشته و آن را پيش بيني مي کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 122
                        elif cmp(msg['text'] , 'به طور معمول با افراد زيادی دوستی و آشنايی دارم.') :
                                # q3
                                dicts[chat_id] = 122
                                keyboard = ReplyKeyboardMarkup(keyboard=[['عمدتا از زندگی در زمان حال لذت زيادی برده و خيلي به آينده فکر نمی کنم.'], ['به آينده توجه زيادي داشته و آن را پيش بيني مي کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 122 :
                        # r22
                        if cmp(msg['text'] , 'عمدتا از زندگی در زمان حال لذت زيادی برده و خيلي به آينده فکر نمی کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولا مغز من بر قلب من حاکم است.'], ['معمولا قلب من بر مغز من حاکم است.']])
                                bot.sendMessage(chat_id, " سوال بیست و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 123
                        elif cmp(msg['text'] , 'به آينده توجه زيادي داشته و آن را پيش بيني مي کنم.') :
                                # q3
                                dicts[chat_id] = 123
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولا مغز من بر قلب من حاکم است.'], ['معمولا قلب من بر مغز من حاکم است.']])
                                bot.sendMessage(chat_id, " سوال بیست و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 123 :
                        # r23
                        if cmp(msg['text'] , 'معمولا مغز من بر قلب من حاکم است.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً در کارهای روزانه مايلم بر حسب ضرورتها و فوريت هايی که پيش می آيد عمل کنم.'], ['معمولاً در کارهاي روزانه مايلم که طبق برنامه عمل کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 124
                        elif cmp(msg['text'] , 'معمولا قلب من بر مغز من حاکم است.') :
                                # q3
                                dicts[chat_id] = 124
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً در کارهای روزانه مايلم بر حسب ضرورتها و فوريت هايی که پيش می آيد عمل کنم.'], ['معمولاً در کارهاي روزانه مايلم که طبق برنامه عمل کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 124 :
                        # r24
                        if cmp(msg['text'] , 'معمولاً در کارهای روزانه مايلم بر حسب ضرورتها و فوريت هايی که پيش می آيد عمل کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از احساسات و عواطف درونی خود کمتر با ديگران صحبت می کنم.'], ['افکار و عواطف خود را آزاد و راحت بيان می کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 125
                        elif cmp(msg['text'] , 'معمولاً در کارهاي روزانه مايلم که طبق برنامه عمل کنم.') :
                                dicts[chat_id] = 125
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از احساسات و عواطف درونی خود کمتر با ديگران صحبت می کنم.'], ['افکار و عواطف خود را آزاد و راحت بيان می کنم.']])
                                bot.sendMessage(chat_id, " سوال بیست و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 125 :
                        # r25
                        if cmp(msg['text'] , 'از احساسات و عواطف درونی خود کمتر با ديگران صحبت می کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کلمات مشخص و دقيق را ترجيح داده و بکار مي برم.'], ['کلمات تمثيلی و کنايه ای را ترجيح داده و بکار می برم.']])
                                bot.sendMessage(chat_id, " سوال بیست و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 126
                        elif cmp(msg['text'] , 'افکار و عواطف خود را آزاد و راحت بيان می کنم.' ):
                                # q3
                                dicts[chat_id] = 126
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کلمات مشخص و دقيق را ترجيح داده و بکار مي برم.'], ['کلمات تمثيلی و کنايه ای را ترجيح داده و بکار می برم.']])
                                bot.sendMessage(chat_id, " سوال بیست و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 126 :
                        # r26
                        if cmp(msg['text'] , 'کلمات مشخص و دقيق را ترجيح داده و بکار مي برم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در تصميم گيری ها رعايت عدالت و انصاف از همه چيز برايم مهم تر است.'], ['در تصميم گيری ها رعايت حال و شرايط ديگران از همه چيز برايم مهم تر است. ']])
                                bot.sendMessage(chat_id, " سوال بیست و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 127
                        elif cmp(msg['text'] , 'کلمات تمثيلی و کنايه ای را ترجيح داده و بکار می برم.') :
                                # q3
                                dicts[chat_id] = 127
                                keyboard = ReplyKeyboardMarkup(keyboard=[['در تصميم گيری ها رعايت عدالت و انصاف از همه چيز برايم مهم تر است.'], ['در تصميم گيری ها رعايت حال و شرايط ديگران از همه چيز برايم مهم تر است. ']])
                                bot.sendMessage(chat_id, " سوال بیست و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 127 :
                        # r27
                        if cmp(msg['text'] , 'در تصميم گيری ها رعايت عدالت و انصاف از همه چيز برايم مهم تر است.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً کارها را شروع می کنم و در حين اجرا به رفع مشکلات پيش آمده می پردازم.'], ['معمولاً قبل از شروع کارها مقدمات کار را آماده و مشکلات را پيش بينی می کنم. ']])
                                bot.sendMessage(chat_id, " سوال بیست و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 128
                        elif cmp(msg['text'] , 'در تصميم گيری ها رعايت حال و شرايط ديگران از همه چيز برايم مهم تر است. ') :
                                # q3
                                dicts[chat_id] = 128
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً کارها را شروع می کنم و در حين اجرا به رفع مشکلات پيش آمده می پردازم.'], ['معمولاً قبل از شروع کارها مقدمات کار را آماده و مشکلات را پيش بينی می کنم. ']])
                                bot.sendMessage(chat_id, " سوال بیست و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 128 :
                        # r28
                        if cmp(msg['text'] , 'معمولاً کارها را شروع می کنم و در حين اجرا به رفع مشکلات پيش آمده می پردازم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کارهای فردی را ترجيح می دهم.'], ['کارهای گروهی را ترجيح می دهم.']])
                                bot.sendMessage(chat_id, " سوال بیست و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 129
                        elif cmp(msg['text'] , 'معمولاً قبل از شروع کارها مقدمات کار را آماده و مشکلات را پيش بينی می کنم. ') :
                                # q3
                                dicts[chat_id] = 129
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کارهای فردی را ترجيح می دهم.'], ['کارهای گروهی را ترجيح می دهم.']])
                                bot.sendMessage(chat_id, " سوال بیست و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 129 :
                        # r29
                        if cmp(msg['text'] , 'کارهای فردی را ترجيح می دهم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['واقعيات ( آنچه که هست ) و پديده ها برايم جالب اند.'], ['حقايق ( آنچه که بايد باشد) و ايده ها برايم جالب اند.']])
                                bot.sendMessage(chat_id, " سوال سی ام: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 130
                        elif cmp(msg['text'] , 'کارهای گروهی را ترجيح می دهم.') :
                                # q3
                                dicts[chat_id] = 130
                                keyboard = ReplyKeyboardMarkup(keyboard=[['واقعيات ( آنچه که هست ) و پديده ها برايم جالب اند.'], ['حقايق ( آنچه که بايد باشد) و ايده ها برايم جالب اند.']])
                                bot.sendMessage(chat_id, " سوال سی ام: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 130 :
                        # r30
                        if cmp(msg['text'] , 'واقعيات ( آنچه که هست ) و پديده ها برايم جالب اند.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['برای عدل و انصاف ارزش زيادی قائلم.'], ['برای بذل و بخشش ارزش زيادی قائلم.']])
                                bot.sendMessage(chat_id, " سوال سی و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 131
                        elif cmp(msg['text'] , 'حقايق ( آنچه که بايد باشد) و ايده ها برايم جالب اند.') :
                                # q3
                                dicts[chat_id] = 131
                                keyboard = ReplyKeyboardMarkup(keyboard=[['برای عدل و انصاف ارزش زيادی قائلم.'], ['برای بذل و بخشش ارزش زيادی قائلم.']])
                                bot.sendMessage(chat_id, " سوال سی و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 131 :
                        # r31
                        if cmp(msg['text'] , 'برای عدل و انصاف ارزش زيادی قائلم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['تهيه فهرست از کار هايی که بايد در روز تعطيل انجام داد را کاری بيهوده و عبث می دانم.'], ['تهيه فهرست از کارهايی که بايد در روز تعطيل انجام داد را کاری جدی و سودمند می دانم.']])
                                bot.sendMessage(chat_id, " سوال سی و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 132
                        elif cmp(msg['text'] , 'برای بذل و بخشش ارزش زيادی قائلم.') :
                                # q3
                                dicts[chat_id] = 132
                                keyboard = ReplyKeyboardMarkup(keyboard=[['تهيه فهرست از کار هايی که بايد در روز تعطيل انجام داد را کاری بيهوده و عبث می دانم.'], ['تهيه فهرست از کارهايی که بايد در روز تعطيل انجام داد را کاری جدی و سودمند می دانم.']])
                                bot.sendMessage(chat_id, " سوال سی و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 132 :
                        # r32
                        if cmp(msg['text'] , 'تهيه فهرست از کار هايی که بايد در روز تعطيل انجام داد را کاری بيهوده و عبث می دانم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً در مهمانی ها و مجالس با شخص يا اشخاصی که از قبل می شناسم گفتگو می کنم.'], ['معمولاً در مهمانی ها و مجالس به دنبال اشخاص جديدی هستم تا با آنها گفتگو کرده و آشنا شوم.']])
                                bot.sendMessage(chat_id, " سوال سی و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 133
                        elif cmp(msg['text'] , 'تهيه فهرست از کارهايی که بايد در روز تعطيل انجام داد را کاری جدی و سودمند می دانم.') :
                                # q3
                                dicts[chat_id] = 133
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً در مهمانی ها و مجالس با شخص يا اشخاصی که از قبل می شناسم گفتگو می کنم.'], ['معمولاً در مهمانی ها و مجالس به دنبال اشخاص جديدی هستم تا با آنها گفتگو کرده و آشنا شوم.']])
                                bot.sendMessage(chat_id, " سوال سی و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 133 :
                        # r33
                        if cmp(msg['text'] , 'معمولاً در مهمانی ها و مجالس با شخص يا اشخاصی که از قبل می شناسم گفتگو می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوستان من اکثراً واقع گرا و واقع بين هستند.'], ['دوستان من اکثراً کسانی هستند که قوه تخيل قوی دارند.']])
                                bot.sendMessage(chat_id, " سوال سی و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 134
                        elif cmp(msg['text'] , 'معمولاً در مهمانی ها و مجالس به دنبال اشخاص جديدی هستم تا با آنها گفتگو کرده و آشنا شوم.' ):
                                # q3
                                dicts[chat_id] = 134
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوستان من اکثراً واقع گرا و واقع بين هستند.'], ['دوستان من اکثراً کسانی هستند که قوه تخيل قوی دارند.']])
                                bot.sendMessage(chat_id, " سوال سی و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 134 :
                        # r34
                        if cmp(msg['text'] , 'دوستان من اکثراً واقع گرا و واقع بين هستند.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به نظر من فردی که با دلايل و استدلال با موضوعات برخورد می کند، بهتر است.'], ['به نظر من فردی که با عاطفه و احساس واقعی و دلسوزی با موضوعات برخورد می کند، بهتر است.']])
                                bot.sendMessage(chat_id, " سوال سی و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 135
                        elif cmp(msg['text'] , 'دوستان من اکثراً کسانی هستند که قوه تخيل قوی دارند.') :
                                # q3
                                dicts[chat_id] = 135
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به نظر من فردی که با دلايل و استدلال با موضوعات برخورد می کند، بهتر است.'], ['به نظر من فردی که با عاطفه و احساس واقعی و دلسوزی با موضوعات برخورد می کند، بهتر است.']])
                                bot.sendMessage(chat_id, " سوال سی و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 135 :
                        # r35
                        if cmp(msg['text'] , 'به نظر من فردی که با دلايل و استدلال با موضوعات برخورد می کند، بهتر است.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['غالباً خود را ملزم به انجام کارها در سر وقت معين و مشخص ندانسته و خود را در محدوده زمان مقيد نمی کنم.'], ['غالباً برنامه خود را  به طور مشخص و دقيق تعيين کرده و بر انجام آنها در سر وقت مقرر اصرار می ورزم.']])
                                bot.sendMessage(chat_id, " سوال سی و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 136
                        elif cmp(msg['text'] , 'به نظر من فردی که با عاطفه و احساس واقعی و دلسوزی با موضوعات برخورد می کند، بهتر است.') :
                                # q3
                                dicts[chat_id] = 136
                                keyboard = ReplyKeyboardMarkup(keyboard=[['غالباً خود را ملزم به انجام کارها در سر وقت معين و مشخص ندانسته و خود را در محدوده زمان مقيد نمی کنم.'], ['غالباً برنامه خود را  به طور مشخص و دقيق تعيين کرده و بر انجام آنها در سر وقت مقرر اصرار می ورزم.']])
                                bot.sendMessage(chat_id, " سوال سی و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 136 :
                        # r36
                        if cmp(msg['text'] , 'غالباً خود را ملزم به انجام کارها در سر وقت معين و مشخص ندانسته و خود را در محدوده زمان مقيد نمی کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['آرام و متفکر هستم.'], ['با نشاط و فعال هستم.']])
                                bot.sendMessage(chat_id, " سوال سی و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 137
                        elif cmp(msg['text'] , 'غالباً برنامه خود را  به طور مشخص و دقيق تعيين کرده و بر انجام آنها در سر وقت مقرر اصرار می ورزم.') :
                                # q3
                                dicts[chat_id] = 137
                                keyboard = ReplyKeyboardMarkup(keyboard=[['آرام و متفکر هستم.'], ['با نشاط و فعال هستم.']])
                                bot.sendMessage(chat_id, " سوال سی و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 137 :
                        # r37
                        if cmp(msg['text'] ,'آرام و متفکر هستم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم فردی واقع گرا و دقيق باشم.'], ['دوست دارم فردی مبتکر و خلاق باشم.']])
                                bot.sendMessage(chat_id, " سوال سی و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 138
                        elif cmp(msg['text'] , 'با نشاط و فعال هستم.' ):
                                # q3
                                dicts[chat_id] = 138
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم فردی واقع گرا و دقيق باشم.'], ['دوست دارم فردی مبتکر و خلاق باشم.']])
                                bot.sendMessage(chat_id, " سوال سی و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 138 :
                        # r38
                        if cmp(msg['text'] , 'دوست دارم فردی واقع گرا و دقيق باشم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به تجزيه وتحليل موضوعات علاقه دارم.'], ['به فيلم ها و بحث های عاطفی که به مسائل انسانی می پردازند، علاقه دارم.']])
                                bot.sendMessage(chat_id, " سوال سی و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 139
                        elif cmp(msg['text'] , 'دوست دارم فردی مبتکر و خلاق باشم.') :
                                # q3
                                dicts[chat_id] = 139
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به تجزيه وتحليل موضوعات علاقه دارم.'], ['به فيلم ها و بحث های عاطفی که به مسائل انسانی می پردازند، علاقه دارم.']])
                                bot.sendMessage(chat_id, " سوال سی و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 139 :
                        # r39
                        if cmp(msg['text'] , 'به تجزيه وتحليل موضوعات علاقه دارم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً زندگی خود را با توجه به اوضاع واحوالی که پيش مي آيد ، تنظيم و اداره می کنم.'], ['معمولاً کارهايی را که مايل به انجام آن هستم يادداشت کرده يا حداقل به طور مرتب به خاطر می سپارم.']])
                                bot.sendMessage(chat_id, " سوال چهلم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 140
                        elif cmp(msg['text'] , 'به فيلم ها و بحث های عاطفی که به مسائل انسانی می پردازند، علاقه دارم.') :
                                # q3
                                dicts[chat_id] = 140
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً زندگی خود را با توجه به اوضاع واحوالی که پيش مي آيد ، تنظيم و اداره می کنم.'], ['معمولاً کارهايی را که مايل به انجام آن هستم يادداشت کرده يا حداقل به طور مرتب به خاطر می سپارم.']])
                                bot.sendMessage(chat_id, " سوال چهلم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 140 :
                        # r40
                        if cmp(msg['text'] , 'معمولاً زندگی خود را با توجه به اوضاع واحوالی که پيش مي آيد ، تنظيم و اداره می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کم حرف هستم.'], ['خوش صحبت هستم.']])
                                bot.sendMessage(chat_id, " سوال چهل و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 141
                        elif cmp(msg['text'] , 'معمولاً کارهايی را که مايل به انجام آن هستم يادداشت کرده يا حداقل به طور مرتب به خاطر می سپارم.' ):
                                # q3
                                dicts[chat_id] = 141
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کم حرف هستم.'], ['خوش صحبت هستم.']])
                                bot.sendMessage(chat_id, " سوال چهل و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 141 :
                        # r41
                        if cmp(msg['text'] , 'کم حرف هستم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هر ايده جديدی را اگر قابل اجرا باشد می پذيرم.'], ['براي هر ايده جديدی به دليل نو بودن آن (بدون توجه به اجرايی بودن يا نبودن آن) ارزش زيادی قائل هستم. ']])
                                bot.sendMessage(chat_id, " سوال چهل و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 142
                        elif cmp(msg['text'] , 'خوش صحبت هستم.') :
                                # q3
                                dicts[chat_id] = 142
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هر ايده جديدی را اگر قابل اجرا باشد می پذيرم.'], ['براي هر ايده جديدی به دليل نو بودن آن (بدون توجه به اجرايی بودن يا نبودن آن) ارزش زيادی قائل هستم. ']])
                                bot.sendMessage(chat_id, " سوال چهل و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 142 :
                        # r42
                        if cmp(msg['text'] , 'هر ايده جديدی را اگر قابل اجرا باشد می پذيرم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم فردی متفکر باشم که عاقلانه رفتار می کند.'], ['دوست دارم فردی عاطفی باشم که با احساسات انسانی رفتار می کند.']])
                                bot.sendMessage(chat_id, " سوال چهل و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 143
                        elif cmp(msg['text'] , 'براي هر ايده جديدی به دليل نو بودن آن (بدون توجه به اجرايی بودن يا نبودن آن) ارزش زيادی قائل هستم. ') :
                                # q3
                                dicts[chat_id] = 143
                                keyboard = ReplyKeyboardMarkup(keyboard=[['دوست دارم فردی متفکر باشم که عاقلانه رفتار می کند.'], ['دوست دارم فردی عاطفی باشم که با احساسات انسانی رفتار می کند.']])
                                bot.sendMessage(chat_id, " سوال چهل و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 143 :
                        # r43
                        if cmp(msg['text'] , 'دوست دارم فردی متفکر باشم که عاقلانه رفتار می کند.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بعضی افراد مرا آدمی بی نظم و دارای زندگی شلوغ می دانند.'], ['بعضی افراد مرا آدمی خشک و غير قابل انعطاف می دانند.']])
                                bot.sendMessage(chat_id, " سوال چهل و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 144
                        elif cmp(msg['text'] , 'دوست دارم فردی عاطفی باشم که با احساسات انسانی رفتار می کند.' ):
                                # q3
                                dicts[chat_id] = 144
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بعضی افراد مرا آدمی بی نظم و دارای زندگی شلوغ می دانند.'], ['بعضی افراد مرا آدمی خشک و غير قابل انعطاف می دانند.']])
                                bot.sendMessage(chat_id, " سوال چهل و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 144 :
                        # r44
                        if cmp(msg['text'] , 'بعضی افراد مرا آدمی بی نظم و دارای زندگی شلوغ می دانند.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['پس از مکث و تأمل کافی، نسبت به بحث يا سؤالات مطرح شده  اظهار نظر مي کنم.'], ['در هر لحظه که فرصت شد سؤالات را مطرح يا نظر خود را اعلام می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 145
                        elif cmp(msg['text'] , 'بعضی افراد مرا آدمی خشک و غير قابل انعطاف می دانند.' ):
                                # q3
                                dicts[chat_id] = 145
                                keyboard = ReplyKeyboardMarkup(keyboard=[['پس از مکث و تأمل کافی، نسبت به بحث يا سؤالات مطرح شده  اظهار نظر مي کنم.'], ['در هر لحظه که فرصت شد سؤالات را مطرح يا نظر خود را اعلام می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 145 :
                        # r45
                        if cmp(msg['text'] , 'پس از مکث و تأمل کافی، نسبت به بحث يا سؤالات مطرح شده  اظهار نظر مي کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ثبات و استحکام را دوست دارم.'], ['تغيير و انعطاف را دوست دارم.']])
                                bot.sendMessage(chat_id, " سوال چهل و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 146
                        elif cmp(msg['text'] , 'در هر لحظه که فرصت شد سؤالات را مطرح يا نظر خود را اعلام می کنم.') :
                                # q3
                                dicts[chat_id] = 146
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ثبات و استحکام را دوست دارم.'], ['تغيير و انعطاف را دوست دارم.']])
                                bot.sendMessage(chat_id, " سوال چهل و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 146 :
                        # r46
                        if cmp(msg['text'] , 'ثبات و استحکام را دوست دارم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر از نتيجه گيری های منطقی و استدلال استفاده می کنم.'], ['بيشتر بر اساس عواطف و عقايد شخصی نسبت به زندگی يا افراد عمل می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 147
                        elif cmp(msg['text'] , 'تغيير و انعطاف را دوست دارم.') :
                                # q3
                                dicts[chat_id] = 147
                                keyboard = ReplyKeyboardMarkup(keyboard=[['بيشتر از نتيجه گيری های منطقی و استدلال استفاده می کنم.'], ['بيشتر بر اساس عواطف و عقايد شخصی نسبت به زندگی يا افراد عمل می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 147 :
                        # r47
                        if cmp(msg['text'] , 'بيشتر از نتيجه گيری های منطقی و استدلال استفاده می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هر وقت که مناسب بود و فرصت دست داد نسبت به انجام کارها آزادانه و بدون فشار اقدام می کنم.'], ['اين مهم است که از قبل بدانم چه کاری يا چه چيزی از من انتظار دارند تا به انجام آنها بپردازم.']])
                                bot.sendMessage(chat_id, " سوال چهل و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 148
                        elif cmp(msg['text'] , 'بيشتر بر اساس عواطف و عقايد شخصی نسبت به زندگی يا افراد عمل می کنم.') :
                                # q3
                                dicts[chat_id] = 148
                                keyboard = ReplyKeyboardMarkup(keyboard=[['هر وقت که مناسب بود و فرصت دست داد نسبت به انجام کارها آزادانه و بدون فشار اقدام می کنم.'], ['اين مهم است که از قبل بدانم چه کاری يا چه چيزی از من انتظار دارند تا به انجام آنها بپردازم.']])
                                bot.sendMessage(chat_id, " سوال چهل و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 148 :
                        # r48
                        if cmp(msg['text'] , 'هر وقت که مناسب بود و فرصت دست داد نسبت به انجام کارها آزادانه و بدون فشار اقدام می کنم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ترجيح می دهم در جمع افراد توسط فرد ديگری معرفی شوم.'], ['معمولاً در جمع، ديگران را به يکديگر معرفی می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 149
                        elif cmp(msg['text'] , 'اين مهم است که از قبل بدانم چه کاری يا چه چيزی از من انتظار دارند تا به انجام آنها بپردازم.') :
                                # q3
                                dicts[chat_id] = 149
                                keyboard = ReplyKeyboardMarkup(keyboard=[['ترجيح می دهم در جمع افراد توسط فرد ديگری معرفی شوم.'], ['معمولاً در جمع، ديگران را به يکديگر معرفی می کنم.']])
                                bot.sendMessage(chat_id, " سوال چهل و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 149 :
                        # r49
                        if cmp(msg['text'] , 'ترجيح می دهم در جمع افراد توسط فرد ديگری معرفی شوم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['تلاش می کنم با رعايت ترتيب، مراحل پيش بينی شده کارها را انجام دهم.'], ['هنگام انجام دادن کارها از قسمت های بی اهميت آن صرف نظر می کنم.']])
                                bot.sendMessage(chat_id, " سوال پنجاهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 150
                        elif cmp(msg['text'] , 'معمولاً در جمع، ديگران را به يکديگر معرفی می کنم.') :
                                # q3
                                dicts[chat_id] = 150
                                keyboard = ReplyKeyboardMarkup(keyboard=[['تلاش می کنم با رعايت ترتيب، مراحل پيش بينی شده کارها را انجام دهم.'], ['هنگام انجام دادن کارها از قسمت های بی اهميت آن صرف نظر می کنم.']])
                                bot.sendMessage(chat_id, " سوال پنجاهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 150 :
                        # r50
                        if cmp(msg['text'] , 'تلاش می کنم با رعايت ترتيب، مراحل پيش بينی شده کارها را انجام دهم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['نسبت به افراد سازمانی که با آنها کار می کنم ، براساس تحليل دقيق اوضاع اظهار نظر می کنم '], ['نسبت به افراد سازمانی که با آنها کار می کنم براساس درک نيازهايشان خود را به جاي آنها گذاشته و اظهار نظر می کنم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 151
                        elif cmp(msg['text'] , 'هنگام انجام دادن کارها از قسمت های بی اهميت آن صرف نظر می کنم.') :
                                # q3
                                dicts[chat_id] = 151
                                keyboard = ReplyKeyboardMarkup(keyboard=[['نسبت به افراد سازمانی که با آنها کار می کنم ، براساس تحليل دقيق اوضاع اظهار نظر می کنم '], ['نسبت به افراد سازمانی که با آنها کار می کنم براساس درک نيازهايشان خود را به جاي آنها گذاشته و اظهار نظر می کنم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و یکم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 151 :
                        # r51
                        if cmp(msg['text'] , 'نسبت به افراد سازمانی که با آنها کار می کنم براساس درک نيازهايشان خود را به جاي آنها گذاشته و اظهار نظر می کنم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً بدون فوت وقت يک کار يا پروژه را شروع و به هر قسمتی از آن که ممکن باشد زودتر می پردازم.'], ['معمولاً کارها را به اجزاي مشخص تقسيم کرده وسپس به ترتيب به انجام بخش های مشخص شده می پردازم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 152
                        elif cmp(msg['text'] , 'نسبت به افراد سازمانی که با آنها کار می کنم ، براساس تحليل دقيق اوضاع اظهار نظر می کنم ') :
                                # q3
                                dicts[chat_id] = 152
                                keyboard = ReplyKeyboardMarkup(keyboard=[['معمولاً بدون فوت وقت يک کار يا پروژه را شروع و به هر قسمتی از آن که ممکن باشد زودتر می پردازم.'], ['معمولاً کارها را به اجزاي مشخص تقسيم کرده وسپس به ترتيب به انجام بخش های مشخص شده می پردازم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و دوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 152 :
                        # r52
                        if cmp(msg['text'] , 'معمولاً بدون فوت وقت يک کار يا پروژه را شروع و به هر قسمتی از آن که ممکن باشد زودتر می پردازم.' ):
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به کارهای فردی ( يا حداکثر با يکی دو نفر ديگر ) علاقمندم.'], ['به کارهای گروهی علاقمندم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 153
                        elif cmp(msg['text'] , 'معمولاً کارها را به اجزاي مشخص تقسيم کرده وسپس به ترتيب به انجام بخش های مشخص شده می پردازم.') :
                                # q3
                                dicts[chat_id] = 153
                                keyboard = ReplyKeyboardMarkup(keyboard=[['به کارهای فردی ( يا حداکثر با يکی دو نفر ديگر ) علاقمندم.'], ['به کارهای گروهی علاقمندم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و سوم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 153 :
                        # r53
                        if cmp(msg['text'] , 'به کارهای فردی ( يا حداکثر با يکی دو نفر ديگر ) علاقمندم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['يکي از اشکالات اساسی زندگی من، يکنواختی وچسبيدن به برنامه و کار مشخص بوده است.'], ['يکي از اشکالات اساسی زندگی من از شاخه ای به شاخه ای پريدن و داشتن برنامه های متعدد بوده است.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 154
                        elif cmp(msg['text'] , 'به کارهای گروهی علاقمندم.' ):
                                # q3
                                dicts[chat_id] = 154
                                keyboard = ReplyKeyboardMarkup(keyboard=[['يکي از اشکالات اساسی زندگی من، يکنواختی وچسبيدن به برنامه و کار مشخص بوده است.'], ['يکي از اشکالات اساسی زندگی من از شاخه ای به شاخه ای پريدن و داشتن برنامه های متعدد بوده است.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و چهارم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 154 :
                        # r54
                        if cmp(msg['text'] , 'يکي از اشکالات اساسی زندگی من، يکنواختی وچسبيدن به برنامه و کار مشخص بوده است.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['قاطع بودن برای من الويت است. '], ['ملايم و احساسی بودن برای من الويت است. ']])
                                bot.sendMessage(chat_id, " سوال پنجاه و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 155
                        elif cmp(msg['text'] , 'يکي از اشکالات اساسی زندگی من از شاخه ای به شاخه ای پريدن و داشتن برنامه های متعدد بوده است.') :
                                # q3
                                dicts[chat_id] = 155
                                keyboard = ReplyKeyboardMarkup(keyboard=[['قاطع بودن برای من الويت است. '], ['ملايم و احساسی بودن برای من الويت است. ']])
                                bot.sendMessage(chat_id, " سوال پنجاه و پنجم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 155 :
                        # r55
                        if cmp(msg['text'] , 'قاطع بودن برای من الويت است. ') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['علاقمندم جلسات و گردهمايی ها هنگامی شروع شود که همگی افراد حضور و آمادگی لازم را داشته و احساس راحتي کنند.'], ['علاقه‌مندم جلسات رأس ساعت مقرر شروع شود و روي وقت‌شناسی تأکيد دارم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 156
                        elif cmp(msg['text'] , 'ملايم و احساسی بودن برای من الويت است. ') :
                                # q3
                                dicts[chat_id] = 156
                                keyboard = ReplyKeyboardMarkup(keyboard=[['علاقمندم جلسات و گردهمايی ها هنگامی شروع شود که همگی افراد حضور و آمادگی لازم را داشته و احساس راحتي کنند.'], ['علاقه‌مندم جلسات رأس ساعت مقرر شروع شود و روي وقت‌شناسی تأکيد دارم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و ششم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 156 :
                        # r56
                        if cmp(msg['text'] , 'علاقمندم جلسات و گردهمايی ها هنگامی شروع شود که همگی افراد حضور و آمادگی لازم را داشته و احساس راحتي کنند.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از نظر ديگران ممکن است تا حدی گوشه گير به نظر برسم.'], ['از نظر ديگران ممکن است  فردی  خوش صحبت به نظر برسم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 157
                        elif cmp(msg['text'] , 'علاقه‌مندم جلسات رأس ساعت مقرر شروع شود و روي وقت‌شناسی تأکيد دارم.') :
                                # q3
                                dicts[chat_id] = 157
                                keyboard = ReplyKeyboardMarkup(keyboard=[['از نظر ديگران ممکن است تا حدی گوشه گير به نظر برسم.'], ['از نظر ديگران ممکن است  فردی  خوش صحبت به نظر برسم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و هفتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 157 :
                        # r57
                        if cmp(msg['text'] , 'از نظر ديگران ممکن است تا حدی گوشه گير به نظر برسم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کارها را با نظم و ترتيب و مرحله به مرحله انجام می دهم.'], ['قسمت های مهم و جالب کار را زودتر انجام می دهم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 158
                        elif cmp(msg['text'] , 'از نظر ديگران ممکن است  فردی  خوش صحبت به نظر برسم.' ):
                                # q3
                                dicts[chat_id] = 158
                                keyboard = ReplyKeyboardMarkup(keyboard=[['کارها را با نظم و ترتيب و مرحله به مرحله انجام می دهم.'], ['قسمت های مهم و جالب کار را زودتر انجام می دهم.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و هشتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 158 :
                        # r58
                        if cmp(msg['text'] , 'کارها را با نظم و ترتيب و مرحله به مرحله انجام می دهم.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['رعايت اصول و قوانين برايم بسيار مهم است.'], ['مهربانی و گذشت در زندگی برايم بسيار مهم است.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 159
                        elif cmp(msg['text'] , 'قسمت های مهم و جالب کار را زودتر انجام می دهم.') :
                                # q3
                                dicts[chat_id] = 159
                                keyboard = ReplyKeyboardMarkup(keyboard=[['رعايت اصول و قوانين برايم بسيار مهم است.'], ['مهربانی و گذشت در زندگی برايم بسيار مهم است.']])
                                bot.sendMessage(chat_id, " سوال پنجاه و نهم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 159 :
                        # r59
                        if cmp(msg['text'] , 'رعايت اصول و قوانين برايم بسيار مهم است.') :
                                # q3
                                keyboard = ReplyKeyboardMarkup(keyboard=[['مقيد بودن به برنامه ای که از قبل مشخص شده باشد براي من جالب نيست.'], ['از انجام دادن کارهايی که از قبل مشخص شده باشد احساس رضايت دارم.']])
                                bot.sendMessage(chat_id, " سوال شصتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                                # dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts[chat_id] = 160
                        elif cmp(msg['text'] , 'مهربانی و گذشت در زندگی برايم بسيار مهم است.' ):
                                # q3
                                dicts[chat_id] = 160
                                keyboard = ReplyKeyboardMarkup(keyboard=[['مقيد بودن به برنامه ای که از قبل مشخص شده باشد براي من جالب نيست.'], ['از انجام دادن کارهايی که از قبل مشخص شده باشد احساس رضايت دارم.']])
                                bot.sendMessage(chat_id, " سوال شصتم: لطفا عبارتی که بیشتر در مورد شما صدق می کند را انتخاب کنید",reply_markup = keyboard)
                        else : 
                                tmp[chat_id] = 100
                        print("end of p 102")




                if tmp[chat_id] == 160 :
                        # r160
                        if cmp(msg['text'] , 'مقيد بودن به برنامه ای که از قبل مشخص شده باشد براي من جالب نيست.') :
                                # q3
                                bot.sendMessage(chat_id, "با تشکر از وقت گذاری شما",reply_markup =ReplyKeyboardRemove(remove_keyboard=True))
                                dicts_ie[chat_id] = dicts_ie[chat_id] + 1
                                # dicts_sn[chat_id] = dicts_sn[chat_id] + 1
                                # dicts_tf[chat_id] = dicts_tf[chat_id] + 1
                                # dicts_pj[chat_id] = dicts_pj[chat_id] + 1
                                dicts_ie[chat_id] = dicts_ie[chat_id] / 15  * 100
                                dicts_sn[chat_id] = dicts_sn[chat_id] / 15  * 100
                                dicts_tf[chat_id] = dicts_tf[chat_id] / 15  * 100
                                dicts_pj[chat_id] = dicts_pj[chat_id] / 15  * 100
                                t = ""
                                if dicts_ie[chat_id]>50 : 
                                        t += "I"
                                else:
                                        t+= "E"

                                if dicts_sn[chat_id]>50 : 
                                        t += "S"
                                else:
                                        t+= "N"

                                if dicts_tf[chat_id]>50 : 
                                        t += "T"
                                else:
                                        t+= "F"

                                if dicts_pj[chat_id]>50 : 
                                        t += "P"
                                else:
                                        t+= "J"
                                dicts_tip[chat_id]=t
                                bot.sendMessage(chat_id,"تیپ شخصیتی شما : "+t)
                                dicts[chat_id] = 161
                                inserTolist(chat_id)
                                saveToCSV()
                        elif cmp(msg['text'] , 'از انجام دادن کارهايی که از قبل مشخص شده باشد احساس رضايت دارم.') :
                                # q3
                                bot.sendMessage(chat_id, "با تشکر از وقت گذاری شما",reply_markup =ReplyKeyboardRemove(remove_keyboard=True))
                                dicts_ie[chat_id] = dicts_ie[chat_id] / 15  * 100
                                dicts_sn[chat_id] = dicts_sn[chat_id] / 15  * 100
                                dicts_tf[chat_id] = dicts_tf[chat_id] / 15  * 100
                                dicts_pj[chat_id] = dicts_pj[chat_id] / 15  * 100
                                t = ""
                                if dicts_ie[chat_id]>50 : 
                                        t += "I"
                                else:
                                        t+= "E"

                                if dicts_sn[chat_id]>50 : 
                                        t += "S"
                                else:
                                        t+= "N"

                                if dicts_tf[chat_id]>50 : 
                                        t += "T"
                                else:
                                        t+= "F"

                                if dicts_pj[chat_id]>50 : 
                                        t += "P"
                                else:
                                        t+= "J"
                                dicts_tip[chat_id]=t
                                dicts_tip[chat_id]=t
                                bot.sendMessage(chat_id,"تیپ شخصیتی شما : "+t)
                                dicts[chat_id] = 161
                                inserTolist(chat_id)
                                saveToCSV()


                        else : 
                                tmp[chat_id] = 100

                        print("end of p 102")
              



                if tmp[chat_id] == 100 :
                        bot.sendMessage(chat_id,"لطفا یکی از گزینه های پیشنهادی را انتخاب کنید")
                if tmp[chat_id] == 161 :
                        bot.sendMessage(chat_id,"ثبت نام شما با موفقیت کامل شد")




        





                
                tmp[chat_id] = dicts[chat_id]
                      
        elif content_type == 'text' :
                if msg['text'] == '/start' :
                        bot.sendMessage(chat_id,'سلام و عرض ادب!')
                        bot.sendMessage(chat_id,'خوش آمدید !')
                        bot.sendMessage(chat_id,'لطفا با حروف فارسی نامتان را بنویسید.')
                        dicts[chat_id] = 1
                        tmp[chat_id] = dicts[chat_id]
                        print("end of p 1")
                        print(chat_id)
                        if chat_id in dicts:
                                print('in in in')
                        
MessageLoop(bot, handle).run_as_thread()
clear = lambda: os.system('clear')
while 1:
    time.sleep(0.5)