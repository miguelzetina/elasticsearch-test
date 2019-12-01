from elasticsearch import Elasticsearch


es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

es.indices.create(index='first_index', ignore=400)

es.indices.exists(index='first_index')

es.indices.delete(index='first_index')
