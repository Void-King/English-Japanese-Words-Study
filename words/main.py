import tkinter as tk
from tkinter import *
import re
from pydub import AudioSegment
from pydub.playback import play
import random
import time

import get_sound
import get_trans

global questions_num
questions_num = 0
def voice_word(word_type, origin_word):
    audio_add = ''
    if word_type == 0:
        audio_add += './words/word_sound/english/'
    else:
        audio_add += './words/word_sound/japanese/'
    audio_name = audio_add + origin_word + '.mp3'
    audio_name = audio_name.encode('utf-8').decode('utf-8')
    sound = AudioSegment.from_mp3(audio_add + origin_word + '.mp3')
    play(sound)

def mem_test(word_type):
    global questions_num
    questions = []
    questions_voice = []
    wordf = ''
    if word_type == 0:
        wordf = 'english.txt'
    else:
        wordf = 'japanese.txt'
    f = open('./words/word_sound/' + wordf, 'r')
    for fp in f.readlines():
        questions.append(fp[re.search('  ', fp).span()[1]:-1])
        questions_voice.append(fp[:re.search('  ', fp).span()[0]])
    maxlength = len(questions)
    length = maxlength
    if questions_num == 0:
        while (questions_num == 0):
            inputnum = input ('输入题目基数数量，不超过' + str(maxlength * 2 // 3) + '个:')
            try:
                questions_num = int(inputnum)
            except:
                pass
    if questions_num % 2 != 0:
        questions_num -= 1

    # print (length)
    a = maxlength - questions_num
    b = questions_num
    x = a + int(random.random() * b)
    length -= 1
    b -= 1
    quescon = questions[x]
    quescon_com = questions_voice[x]
    questions.pop(x)
    questions_voice.pop(x)
    
    root = tk.Tk()
    root.geometry('820x310+300+300')
    root.resizable(0, 0)
    root.title('Words Study')
    frame1 = tk.Frame(root, background='#3f3f3f')
    frame1.grid(padx = 0, pady = 0)
    frame = tk.Frame(frame1, background='#3f3f3f')
    frame.grid(padx = 10, pady = 8)

    answer = []
    answer_com = []
    answer_com.append(quescon_com)
    
    label1 = tk.Text(frame, width = 22, height = 6, font = '微软雅黑 20')
    label1.grid(row = 0, column = 0, sticky = tk.NW, padx = 22, pady = 40)
    label2 = tk.Text(frame, width = 22, height = 6, font = '微软雅黑 20')
    label2.grid(row = 0, column = 1, sticky = tk.NW, padx = 22, pady = 40)
    label1.insert(INSERT, quescon)

    def next_ques_re(event):
        next_ques()
    def next_ques():
        nonlocal length, maxlength, answer, answer_com, a, b, questions, word_type, quescon_com
        # def showresult():
        #     print (answer)
        #     print (answer_com)
        if length == maxlength - questions_num:
            a = 0
            b = maxlength - questions_num
        x = a + int(random.random() * b)
        length -= 1
        b -= 1
        # print (questions)
        if length >= 0:
            quescon = questions[x]
            quescon_com = questions_voice[x]
            questions.pop(x)
            questions_voice.pop(x)
        
        if label2.get('1.0','end')[:-2] == '':
            answer.append('NULL')
        else:
            answer.append(label2.get('1.0','end')[:-2])
        label1.delete('1.0','end')
        label2.delete('1.0','end')
        if length + 1 == maxlength - questions_num - (questions_num // 2):
            # showresult()
            root.destroy()
            root1 = tk.Tk()
            root1.title('Words Study')

            canvas=Canvas(root1,width=500,height=500,scrollregion=(0,0,0,1540)) #创建canvas
            canvas.pack() #放置canvas的位置
            frame11=Frame(canvas) #把frame放在canvas里
            frame11.pack() #frame的长宽，和canvas差不多的

            vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
            vbar.place(x = 480,width=20,height=500)
            vbar.configure(command=canvas.yview)
            # frame11 = Frame(root1)
            # frame11.pack()
            text11 = Text(frame11, width = 19, height = 60, font = '微软雅黑 14')
            text12 = Text(frame11, width = 19, height = 60, font = '微软雅黑 14')
            text11.grid(row = 0, column = 0, sticky = tk.NW, padx = 10, pady = 10)
            text12.grid(row = 0, column = 1, sticky = tk.NW, padx = 10, pady = 10)
            for i in range(0,len(answer)):
                text11.insert(INSERT, answer_com[i]+'\n')
                text12.insert(INSERT, answer[i]+'\n')
                if answer[i] != answer_com[i]:
                    text12.tag_add('redtag', str(i+1)+'.0', str(i+1)+'.end')
                    text12.tag_config('redtag', foreground = 'red')
            canvas.config(yscrollcommand=vbar.set) #设置  
            canvas.create_window((240,770), window=frame11)  #create_window
            root1.mainloop()
        else:
            answer_com.append(quescon_com)
            label1.insert(INSERT, quescon)
            voice_word(word_type, quescon_com + '_cn')
        
    root.bind('<Return>', next_ques_re)
    voice_word(word_type, quescon_com + '_cn')
    root.mainloop()


def display_word():
    global questions_num
    root = tk.Tk()
    root.geometry('1140x490+200+200')
    root.resizable(0, 0)
    root.title('Words Study')
    frame1 = tk.Frame(root, background='#3f3f3f')
    frame1.grid(padx = 0, pady = 0)
    frame = tk.Frame(frame1, background='#3f3f3f')
    frame.grid(padx = 10, pady = 8)
    owEt = tk.Entry(frame, width = 43, font = "微软雅黑 16")
    owEt.grid(row = 0, column = 0, sticky = tk.NW, padx = 15, pady = 25)
    label1 = tk.Text(frame, width = 43, height = 12, font = '微软雅黑 16')
    label1.grid(row = 1, column = 0, sticky = tk.NW, padx = 15)
    label2 = tk.Text(frame, width = 60, height = 16, font = '微软雅黑 12')
    label2.grid(row = 1, column = 1, sticky = tk.NW, padx = 15)
    def confirm_word_re(event):
        confirm_word()
    def confirm_word():
        global questions_num
        questions_num += 1

        word_type = 0
        origin_word = owEt.get()
        if re.search('[A-z]+', origin_word) is None:
            word_type = 1
        if origin_word != '':
            cn_word = get_trans.get_t(word_type, origin_word)
            label1.delete('1.0','end')
            label2.delete('1.0','end')
            label1.insert(INSERT, cn_word)
            cn_word_all = ''
            try:
                cn_word_all = get_trans.get_allt(word_type, origin_word)
            except:
                pass
            label2.insert(INSERT, cn_word_all)
            get_sound.get_s(word_type, origin_word, cn_word)
            voice_word(word_type, origin_word)
            owEt.delete('0','end')

    owBt = tk.Button(frame, text = '查询',command = confirm_word, width = 66, font = "微软雅黑 10")
    owBt.grid(row = 0, column = 1, padx = 15, pady = 25)


    def engt():
        mem_test(0)
    def jpt():
        mem_test(1)
    egBt = tk.Button(frame, text = '英语训练',command = engt, width = 50, font = "微软雅黑 10")
    egBt.grid(row = 2, column = 0, padx = 15, pady = 10)
    jpBt = tk.Button(frame, text = '日语训练',command = jpt, width = 50, font = "微软雅黑 10")
    jpBt.grid(row = 2, column = 1, padx = 15, pady = 10)
    
    # cn_word = get_trans.get_t(0, 'state')
    # cn_word_all = get_trans.get_allt(0, 'state')
    # print (cn_word_all)
    # get_sound.get_s(0, 'state', cn_word)
    root.bind('<Return>', confirm_word_re)
    root.mainloop()

    
# mem_test(0)
display_word()