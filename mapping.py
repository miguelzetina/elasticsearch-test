from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"Bangalore", "country":"India","datetime":"2018,01,01,10,20,00"} #format: yyyy,MM,dd,hh,mm,ss
doc2 = {"city":"London", "country":"England","datetime":"2018,01,02,03,12,00"}
doc3 = {"city":"Los Angeles", "country":"USA","datetime":"2018,04,19,21,02,00"}

es.indices.get_mapping(index='travel', doc_type='cities') #POSTMAN: http://127.0.0.1:9200/travel/_mapping/cities

es.index(index="travel", doc_type="cities", id=1, body=doc1)

#http://127.0.0.1:9200/travel/_mapping/places
es.indices.put_mapping(
    index="travel",
    doc_type="cities",
    body={
        "properties": {
            "city": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "country": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "datetime": {
                "type": "date",
                "format":"yyyy,MM,dd,hh,mm,ss"
            }
        }
    }
)
"""
es.indices.delete(index="travel")

es.indices.create(index="travel")
"""
