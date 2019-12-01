from elasticsearch import Elasticsearch


es = Elasticsearch("http://localhost:9200")

doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

es.index(index="cities", doc_type="places", id=1, body=doc1)

es.index(index="cities", doc_type="places", id=2, body=doc2)

es.index(index="cities", doc_type="places", id=3, body=doc3)

res = es.get(index="cities", doc_type="places", id=2)

print(res)

print(res['_source'])
