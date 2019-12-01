# Elasticsearch with Python

## Prerequisites

- [pipenv](https://github.com/pypa/pipenv)
- [Elasticsearh 7.4.2](https://www.elastic.co/)

### Run Jupyter environment

```bash
pipenv run jupyter notebook
```


#### Extra - Install Elasticsearch with Docker

[Install Docker](https://docs.docker.com/install/)

```bash
docker pull elasticsearch:7.4.2
```

```bash
docker network create elasticsearch-net
```

```bash
docker run -d --name elasticsearch --net elasticsearch-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.4.2
```

