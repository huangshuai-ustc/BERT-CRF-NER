import json
import os

pred_output_dir = r"../outputs/nsner_output/bert/"
dataset_dir = r"../datasets/nsner/"
output_predict_file = os.path.join(pred_output_dir, "test_prediction.json")
with open(output_predict_file, "r", encoding="utf-8") as f:
    datas = f.readlines()[2000:3000]

with open(dataset_dir+'train.char', 'a', encoding='utf-8') as f:
    for i in range(len(datas)):
        # if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 8:
        if int(str(i)[-1]) != 3 and int(str(i)[-1]) != 8:
            j = json.loads(datas[i])
            tag_seq = j['tag_seq'].split(' ')
            seq = j['seq']
            print(seq)
            entities = j['entities']
            p = j['p'][1:-1]
            if len(seq) == len(tag_seq):
                tag_seq = ['O']*len(seq)
                for _ in entities:
                    start = _[1]
                    end = _[2]
                    score = sum(p[start:end + 1]) / (end - start)
                    if score < 7.0:
                        _[0] = 'O'
                    for j in entities:
                        if j[0] != 'O':
                            tag_seq[j[1]] = 'B-'+j[0]
                            tag_seq[j[1]+1:j[2]+1] = ['I-'+j[0] for i in tag_seq[j[1]+1:j[2]+1]]
                for j in range(len(seq)):
                    f.write(seq[j]+' '+tag_seq[j]+'\n')
                f.write('\n')
