import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--path', type=str, default='test.txt')
args = parse.parse_args()
file = open(args.path, 'r', encoding='utf-8')
with open('datasets/nsner/test.char', 'w', encoding='utf-8') as f:
    for line in file.readlines():
        line = line.replace('\xa0', ' ').replace('\u3000', ' ').replace('\x20', ' ').replace('\u202f', ' ').replace('\u200b', ' ')
        line = line.strip().replace(' ', '，')
        for _ in line:
            f.write(_ + ' O\n')
        f.write('\n')
