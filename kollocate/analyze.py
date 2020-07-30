from konlpy.tag import Kkma


kkma = Kkma()

with open('wiki/wiki.ko.analyzed', 'w', encoding='utf8') as fout:
    for line in open('wiki/wiki.ko', 'r', encoding='utf8'):
        line = line.strip()
        try:
            li = kkma.pos(line, flatten=False, join=True)
            analyzed = " ".join("+".join(each) for each in li)
            fout.write(f"{line}\t{analyzed}\n")
        except:
            continue

