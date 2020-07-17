from whoosh.index import create_in
from whoosh import fields, analysis
from whoosh.qparser import QueryParser


myanalyzer = analysis.StandardAnalyzer(expression=r'[ㄱ-힣]+', minsize=1)
schema = fields.Schema(analysis=fields.TEXT(analyzer=myanalyzer, stored=True))
ix = create_in("indexdir", schema)
writer = ix.writer()

n_words = 0
for line in open('wiki/wiki.ko.analyzed', 'r', encoding='utf8'):
    line = line.strip()
    sent, analysis = line.split("\t")
    n_words += len(sent.split())
    if n_words > 10000000: break
    writer.add_document(analysis=analysis)
writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("analysis", ix.schema).parse("지미")
    print(query)
    results = searcher.search(query)
    print(results[0]["analysis"])