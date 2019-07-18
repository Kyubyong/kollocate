from whoosh.qparser import QueryParser
import whoosh.index as index
from collections import Counter
import re


class Collocate(object):
    def __init__(self):
        ix = index.open_dir("indexdir")
        self.searcher = ix.searcher()
        self.query = QueryParser("analysis", ix.schema)


    def adjust(self, analysis):
        tokens = re.split("[ +]", analysis)
        words, poses = [], []
        for token in tokens:
            try:
                word, pos = token.split("/")
            except:
                continue
            if pos[0]=="N":
                pos = "noun"
            elif pos in ("VV", "VXV"):
                pos = "verb"
            elif pos in ("VA", "VXA", "VCN"):
                pos = "adjective"
            elif pos[:2] == "MD":
                pos = "determiner"
            elif pos[:2] == "MA":
                pos = "adverb"
            else:
                continue
            words.append(word)
            poses.append(pos)
        return words, poses


    def parse_results(self, query, results):
        # print(len(results))
        entry = dict()
        for result in results:
            sent = result["analysis"]
            words, poses = self.adjust(sent)
            for i, (w, p) in enumerate(zip(words, poses)):
                if w == query:
                    if i != 0:
                        w_col = words[i-1]
                        p_col = poses[i-1]
                        if p in entry:
                            if p_col in entry[p]:
                                entry[p][p_col].append(w_col)
                            else:
                                entry[p][p_col] = [w_col]
                        else:
                            entry[p] = dict()
                            entry[p][p_col] = [w_col]

                    if i != len(words)-1:
                        w_col = words[i+1]
                        p_col = poses[i+1]
                        if p in entry:
                            if p_col in entry[p]:
                                entry[p][p_col].append(w_col)
                            else:
                                entry[p][p_col] = [w_col]
                        else:
                            entry[p] = dict()
                            entry[p][p_col] = [w_col]
        _entry = dict()
        for pos, cols in entry.items():
            _entry[pos] = dict()
            for col_pos, collocates in cols.items():
                collocate2cnt = Counter(collocates)
                _collocates = []
                for collocate, cnt in collocate2cnt.most_common(len(collocate2cnt)):
                    _collocates.append((collocate, cnt))
                _entry[pos][col_pos] = _collocates

        return _entry


    def __call__(self, word):
        query = self.query.parse(word)
        results = self.searcher.search(query, limit=None)
        print(query, results)
        entry = self.parse_results(word, results)

        return entry

if __name__ == "__main__":
    c = Collocate()
    q = "먹"
    collocates = c(q)
    for pos, cols in collocates.items():
        print(q + " as " + pos)
        for pos2, cols2 in cols.items():
            print(pos2, ", ".join(word + "(" + str(cnt) + ")" for word, cnt in cols2))

