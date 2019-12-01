from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

es.get(index="english", doc_type="sentences", id=1)

es.get(index="english", doc_type="sentences", id=2)

es.get(index="english", doc_type="sentences", id=3)

es.search(index="english", body={"from":0, "size":0,"query":{"regexp":{"sentence":".*"}}})

es.search(index="english", body={"from":0, "size":3,"query":{"regexp":{"sentence":".*"}}})

es.search(index="english", body={"from":0, "size":0,"query":{"regexp":{"sentence":"sun.*"}}})

es.search(index="english", body={"from":0, "size":2,"query":{"regexp":{"sentence":".*"}}})

