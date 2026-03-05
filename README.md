# imdb_spark_project
Big Data Project (Polishchuk, Hoshovska, Pavliukh, Napadailo)

### 1. Клонування репозиторію

```bash
git clone https://github.com/polishchukmaryna/imdb_spark_project.git
cd imdb_spark_project
git checkout develop
```

### 2. Завантаження даних

Створіть папку `data/` та завантажте файли з https://datasets.imdbws.com/:

```bash
mkdir -p data && cd data
wget https://datasets.imdbws.com/name.basics.tsv.gz
wget https://datasets.imdbws.com/title.akas.tsv.gz
wget https://datasets.imdbws.com/title.basics.tsv.gz
wget https://datasets.imdbws.com/title.crew.tsv.gz
wget https://datasets.imdbws.com/title.episode.tsv.gz
wget https://datasets.imdbws.com/title.principals.tsv.gz
wget https://datasets.imdbws.com/title.ratings.tsv.gz
gunzip *.gz
cd ..
```

### 3. Запуск через Docker

```bash
docker compose up --build
```

