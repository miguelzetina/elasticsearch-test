from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

doc1 = {"sentence" : "Today is a sunny day."}
doc2 = {"sentence" : "Today is a bright-sunny day"}

es.index(index="english", doc_type="sentences", id=1, body=doc1)

es.index(index="english", doc_type="sentences", id=2, body=doc2)

res = es.search(index="english", body={"from":0,"size":0,"query":{"match":{"sentence":"SUNNY"}}})
print(res)

res = es.search(index="english", body={"from":0,"size":2,"query":{"match":{"sentence":"SUNNY"}}})
print(res)

res = es.search(index="english", body={"from":0,"size":0,"query":{"match_phrase":{"sentence":"SUNNY"}}})
print(res)

res = es.search(index="english", body={"from":0,"size":0,"query":{"match_phrase":{"sentence":"bright SUNNY"}}})
print(res)

res = es.search(index="english", body={"from":0,"size":0,"query":{"term":{"sentence":"bright SUNNY"}}})
print(res)

