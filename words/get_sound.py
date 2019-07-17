import sys
import os
import requests
import json
import re

import get_trans

def get_s(language_type, single_word, single_cn_word):
    sound_url = ""
    sound_cn_url = ''
    record_txt = ''
    word_adress = ''
    save_flag = 1
    if language_type == 0:# english
        sound_url = 'https://fanyi.baidu.com/gettts?lan=en&text=' + single_word + '&spd=3&source=web'
        sound_cn_url = 'https://fanyi.baidu.com/gettts?lan=zh&text=' + single_cn_word + '&spd=4&source=web'
        record_txt = './words/word_sound/english.txt'
        word_adress = './words/word_sound/english/'
        f = open('./words/word_sound/english.txt','r')
        for ft in f.readlines():
            ftn = re.search('  ', ft)
            if single_word == ft[:ftn.span()[0]]:
                # print ('exist!')
                save_flag = 0
    elif language_type == 1:# japanese
        sound_url = 'https://fanyi.baidu.com/gettts?lan=jp&text=' + single_word + '&spd=3&source=web'
        sound_cn_url = 'https://fanyi.baidu.com/gettts?lan=zh&text=' + single_cn_word + '&spd=4&source=web'
        record_txt = './words/word_sound/japanese.txt'
        word_adress = './words/word_sound/japanese/'
        f = open('./words/word_sound/japanese.txt','r')
        for ft in f.readlines():
            ftn = re.search('  ', ft)
            if single_word == ft[:ftn.span()[0]]:
                # print ('exist!')
                save_flag = 0
    
    if save_flag == 1:
        res = requests.get(sound_url)
        sound_file = open(word_adress + single_word + '.mp3', 'wb')
        sound_file.write(res.content)
        sound_file.close()
        res = requests.get(sound_cn_url)
        sound_file = open(word_adress + single_word + '_cn.mp3', 'wb')
        sound_file.write(res.content)
        sound_file.close()

        record_txt_stream = open(record_txt, 'a')
        record_txt_stream.write(single_word + '  ' + single_cn_word + '\n')
        record_txt_stream.close()
    else:
        pass
    return save_flag
# get_s(1, 'ねこ', '寻找')

