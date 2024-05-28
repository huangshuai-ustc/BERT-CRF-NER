import re

space_regex = re.compile(r'[\u2000-\u200a\u202f\u205f\u3000\u180e\xa0\u200b]')
str1 = 'x    x  x'
str1 = space_regex.sub(' ', str1)
with open('test.char', 'w', encoding='utf-8') as f:   
    str1 = str1.strip().replace(' ', '，')
    for _ in str1:
        f.write(_ + ' O\n')
