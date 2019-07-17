import js2py
import sys
import os
import requests
import json
# https://blog.csdn.net/qq_42306041/article/details/93183327

def get_t(language_type, single_word):
    
    sign = js2py.EvalJs()
    with open('./words/sign.js', 'r', encoding='utf-8') as f:
        sign.execute(f.read())
    sign_con = str(sign.e(single_word))

    word_url = "https://fanyi.baidu.com/v2transapi"
    from_type = ''
    if language_type == 0:# english
        from_type = 'en'
    elif language_type == 1:# japanese
        from_type = 'jp'
        
    data = {
        'from': from_type,
        'to': 'zh',
        'query': single_word,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign_con,
        'token': '0acb460908f02ba69bd0979aedab298a'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'cookie': 'BIDUPSID=5A47EC51C61EBD14FA107A2E5469DC3F; PSTM=1556338557; BAIDUID=5A47EC51C61EBD14FA107A2E5469DC3F:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=1421_21104_29522_29521_29237_28519_29099_28830_29220; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%5D; delPer=0; ZD_ENTRY=baidu; locale=zh; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563151766,1563153427,1563153433,1563156570; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563156584; yjs_js_security_passport=c68a1065c904837b6895234acb1964967c65737c_1563156583_js'
    }
    res = requests.post(url = word_url, data = data, headers = headers)
    trans_result = json.loads(res.text)['trans_result']['data'][0]['dst']
    # print (trans_result)
    return res
    # return trans_result
    # print (trans_result)
    # res = requests.get(sound_url)
    # sound_file = open('test.mp3', 'wb')
    # sound_file.write(res.content)
    # sound_file.close()
    # print (res['tgt'])
def get_allt(res):
    # word_url = "https://fanyi.baidu.com/transapi"
    # from_type = ''
    # if language_type == 0:# english
    #     from_type = 'en'
    # elif language_type == 1:# japanese
    #     from_type = 'jp'
    # data = {
    #     'from': from_type,
    #     'to': 'zh',
    #     'query': single_word,
    #     'source': 'txt'
    # }
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    #     'cookie': 'BIDUPSID=5A47EC51C61EBD14FA107A2E5469DC3F; PSTM=1556338557; BAIDUID=5A47EC51C61EBD14FA107A2E5469DC3F:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=1421_21104_29522_29521_29237_28519_29099_28830_29220; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; ZD_ENTRY=baidu; locale=zh; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563151766,1563153427,1563153433,1563156570; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563156584; yjs_js_security_passport=c68a1065c904837b6895234acb1964967c65737c_1563156583_js; DOUBLE_LANG_SWITCH=1; CHINA_PINYIN_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
    # }
    # res = requests.post(url = word_url, data = data, headers = headers)
    # res_text = str(json.loads(res.text)['result']).encode('utf-8').decode('unicode_escape')
    # # print (res.text.encode('utf-8').decode('unicode_escape'))
    # # print (json.loads(res_text)['content'][0]['mean'])
    # show_text = ''
    # for word_type in json.loads(res_text)['content'][0]['mean']:
    #     show_text += str(word_type['pre']) + '\n'
    #     for single_mean in list(word_type['cont'].keys()):
    #         show_text += str(single_mean) + ', '
    #     show_text = show_text[:-2]
    #     show_text +='\n'
    trans_result = json.loads(res.text)['dict_result']['simple_means']['symbols'][0]['parts']
    show_text = ''
    for i in trans_result:
        # print (i['part'])
        show_text += i['part'] + '\n'
        all_t = ''
        for j in i['means']:
            all_t += j + ', '
        all_t = all_t[:-2] + '\n'
        # print (all_t)
        show_text += all_t
    # print (show_text)
    return show_text
# res = get_t(0, 'state')
# get_allt(res)
# get_t(1, 'ありがとう')
# get_t(0, 'hello')
