import os
import jieba
import jieba.posseg as psg
import re
import pandas as pd
def get_stop_dict(file):
    content = open(file,encoding="utf-8")
    word_list = []
    for c in content:
        c = re.sub('\n|\r','',c)
        word_list.append(c)
    return word_list

file_path = input("请输入当前文件夹路径:")
os.chdir(file_path)
stop_file = input("请输入停用词文件名字:")
user_file = input("请输入用户词典文件名字:")
##stop_file = "stopwordlist.txt"
##user_file = "add_word_list.txt"

stop_words = get_stop_dict(stop_file)
file_name = input("请输入文件名字:")
text = open(file_name,encoding="utf-8").read()
jieba.load_userdict(user_file)
text_lines  = text.split('\n')

flag_list = ['n','nz','vn']
counts={}

for line in text_lines:
    line_seg = psg.cut(line)
    for word_flag in line_seg:
        word = re.sub("[^\u4e00-\u9fa5]","",word_flag.word)
        if word_flag.flag in flag_list and len(word)>1 and word not in stop_words:
            counts[word]=counts.get(word,0)+1

word_freq = pd.DataFrame({'word':list(counts.keys()),'freq':list(counts.values())})
word_freq = word_freq.sort_values(by='freq',ascending=False)
word_freq.to_excel("word_freq.xlsx",index=False)

input("Press <enter>")
