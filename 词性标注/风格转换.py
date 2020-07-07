from fastHan import FastHan
import random
import re
word_label = ['NN', 'JJ', 'VA', 'NT']
find = {'NN':'', 'VV':'', 'JJ':'', 'VA':'', 'NT':''}
with open('NN_new.txt', "r", encoding='UTF8') as f_NN, open('VV_new.txt', "r", encoding='UTF8') as f_VV, open('JJ_new.txt', "r", encoding='UTF8') as f_JJ, open('VA_new.txt', "r", encoding='UTF8') as f_VA, open('NT_new.txt', "r", encoding='UTF8') as f_NT:
    find['NN'] = f_NN.read().split("\n")
    find['VV'] = f_VV.read().split("\n")
    find['JJ'] = f_JJ.read().split("\n")
    find['VA'] = f_VA.read().split("\n")
    find['NT'] = f_NT.read().split("\n")
model = FastHan(model_type = 'large')
while 1:
    text = input("请输入转换语句：")
    answer=model(text,target="Parsing")
    for _ in range(10):
        final = []
        for i in range(len(answer[0])):
            if str(answer[0][i].pos) in word_label:
                final.append(''.join(re.findall('[\u4e00-\u9fa5]', find[str(answer[0][i].pos)][random.randint(0, len(find[str(answer[0][i].pos)]))])))
            else:
                final.append(str(answer[0][i]))
        print("--------------------")
        print(''.join(final))
        print("--------------------")
