"""
本文件将预测的结果中置信度较高的数据重新加入训练集
"""
import json

with open("test_prediction.json", "r", encoding="utf-8") as f:
    datas = f.readlines()
with open('train.char', 'a', encoding='utf-8') as f:
    for i in datas:
        j = json.loads(i)
        tag_seq = j['tag_seq'].split(' ')
        print(tag_seq)
        seq = j['seq']
        entities = j['entities']
        p = j['p'][1:-1]
        for _ in entities:
            print(_)
            start = _[1]
            end = _[2]
            score = sum(p[start:end]) / (end - start + 1)
            if score < 8.0:
                _[0] = 'O'
                tag_seq[start:end+1] = ['O' for i in tag_seq[start:end+1]]
            #     tag_seq[start:end + 1] = [_[0] + ' 0' for i in tag_seq[start:end + 1]]
            # else:
            #     tag_seq[start:end + 1] = [_[0] + ' 1' for i in tag_seq[start:end + 1]]
        for _ in range(len(seq)):
            if tag_seq[_] == 'O':
                f.write(seq[_]+' '+tag_seq[_]+' 0\n')
            else:
                f.write(seq[_]+' '+tag_seq[_]+' 1\n')
            # f.write(seq[_] + ' ' + tag_seq[_] + '\n')
        f.write('\n')

