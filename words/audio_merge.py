from pydub import AudioSegment  # 先导入这个模块
import os
import re

work_path = os.getcwd()
work_path = work_path[::-1]
work_path = work_path[6:]
work_path = work_path[::-1]
os.chdir(work_path)

eng = './words/word_sound/english/'
jp = './words/word_sound/japanese/'
sec = './words/word_sound/'

choice = input ('eng or jp ? :')

def mergeFunc(path, word_type):

    questions_voice = []
    wordf = ''
    if word_type == 0:
        wordf = 'english.txt'
    else:
        wordf = 'japanese.txt'
    f = open(sec + wordf, 'r')
    for fp in f.readlines():
        # questions.append(fp[re.search('  ', fp).span()[1]:-1])
        questions_voice.append(fp[:re.search('  ', fp).span()[0]])
    print (questions_voice)
    output_music = AudioSegment.from_mp3(sec + '1s.mp3') 
    for name in questions_voice:
        print (name)
        # 加载需要合并的两个mp3音频
        try:
            input_music_0 = AudioSegment.from_mp3(path + name + '.mp3') 
        except:
            input_music_0 = AudioSegment.from_mp3(path + name + '_cn.mp3') 

        input_music_1 = AudioSegment.from_mp3(sec + '1s.mp3') 

        try:
            input_music_2 = AudioSegment.from_mp3(path + name + '_cn.mp3') 
        except:
            input_music_2 = AudioSegment.from_mp3(path + name + '.mp3') 
        input_music_3 = AudioSegment.from_mp3(sec + '2s.mp3') 

        output_music += input_music_0 + input_music_1 + input_music_2 + input_music_3
        # 简单输入合并之后的音频
    output_music.export('./' + choice + ".mp3", format="mp3")# 前面是保存路径，后面是保存格式

if choice == 'eng':
    mergeFunc(eng, 0)
elif choice == 'jp':
    mergeFunc(jp, 1)