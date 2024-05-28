import json

with open("outputs/nsner_output/bert/test_prediction.json", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for i in datas:
        j = json.loads(i)
        tag_seq = j['tag_seq'].split(' ')
        seq = j['seq']
        entities = j['entities']
        p = j['p'][1:-1]
        for _ in entities:
            start = _[1]
            end = _[2]
            print(_[0]+": "+seq[start:end+1].replace('，', ' '))
