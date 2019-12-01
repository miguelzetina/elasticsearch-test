from elasticsearch import Elasticsearch


es = Elasticsearch("http://localhost:9200")

doc1 = {"sentence" : "Today is a sunny day."}
doc2 = {"sentence" : "Today is a bright-sunny day"}

res = es.search(
    index="english",
    body={
        "from": 0,
        "size": 0,
        "query": {
            "bool": {
                "must_not": { "match": { "sentence": "bright" } },
                "should": { "match": { "sentence": "sunny" } }
            }
        }
    }
)

print(res)

res = es.search(
    index="english",
    body={
        "from": 0,
        "size": 1,
        "query": {
            "bool": {
                "must_not": { "match": { "sentence": "bright" } },
                "should": { "match": { "sentence": "sunny" } }
            }
        }
    }
)

print(res)

