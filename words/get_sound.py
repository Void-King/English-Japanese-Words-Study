import sys
import os
import requests
import json
import re

import get_trans

def get_s(language_type, single_word, single_cn_word, single_cn_detail):
    sound_url = ""
    sound_cn_url = ''
    record_json = ''
    word_adress = ''
    save_flag = 1
    cur_json = json.loads("{}")
    cur_words = {}
    if language_type == 0:# english
        sound_url = 'https://fanyi.baidu.com/gettts?lan=en&text=' + single_word + '&spd=3&source=web'
        sound_cn_url = 'https://fanyi.baidu.com/gettts?lan=zh&text=' + single_cn_word + '&spd=4&source=web'
        record_json = './words/word_sound/english.json'
        word_adress = './words/word_sound/english/'
        f = open('./words/word_sound/english.json','r', encoding='utf-8')
        cur_json = json.loads(f.read())
        f.close()
        cur_words = cur_json["words"]
        for exist in cur_words:
            if single_word == exist["word"]:
                # print ('exist!')
                save_flag = 0
                break
    elif language_type == 1:# japanese
        sound_url = 'https://fanyi.baidu.com/gettts?lan=jp&text=' + single_word + '&spd=3&source=web'
        sound_cn_url = 'https://fanyi.baidu.com/gettts?lan=zh&text=' + single_cn_word + '&spd=4&source=web'
        record_json = './words/word_sound/japanese.json'
        word_adress = './words/word_sound/japanese/'
        f = open('./words/word_sound/japanese.json','r', encoding='utf-8')
        cur_json = json.loads(f.read())
        f.close()
        cur_words = cur_json["words"]
        for exist in cur_words:
            if single_word == exist["word"]:
                # print ('exist!')
                save_flag = 0
                break
    
    if save_flag == 1:
        res = requests.get(sound_url)
        sound_file = open(word_adress + single_word + '.mp3', 'wb')
        sound_file.write(res.content)
        sound_file.close()
        res = requests.get(sound_cn_url)
        sound_file = open(word_adress + single_word + '_cn.mp3', 'wb')
        sound_file.write(res.content)
        sound_file.close()

        newWordDict = {}
        newWordDict["word"] = single_word
        newWordDict["cnword"] = single_cn_word
        newWordDict["cndetail"] = single_cn_detail
        cur_words.append(newWordDict)

        outStr = json.dumps(cur_json, ensure_ascii=False)
        record_txt_stream = open(record_json, 'w', encoding='utf-8')
        record_txt_stream.write(outStr)
        record_txt_stream.close()
    else:
        pass
    return save_flag
# get_s(1, 'ねこ', '寻找')

