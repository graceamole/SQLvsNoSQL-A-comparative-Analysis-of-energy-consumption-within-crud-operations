#  SQL vs NoSQL: A Comparative Analysis of Energy Consumption in CRUD Operations

> A university research project investigating the environmental cost of database operations across SQL and NoSQL systems, using real energy measurement tooling to produce empirical, data-driven findings.

---

##  Overview

As cloud infrastructure scales globally, the energy footprint of database systems has become an increasingly important consideration for sustainable software engineering. This research project conducts a rigorous, empirical comparison of energy consumption across four widely-used database systems — two relational (SQL) and two document-based (NoSQL) — measuring the carbon emissions produced during standard Create, Read, Update, and Delete (CRUD) operations across three data types: **text**, **images**, and **audio**.

The goal is to provide data-driven insights into which database paradigm is more energy-efficient for different workload types, helping developers and architects make environmentally informed technology choices.

---

##  Databases Compared

| Type   | Database       |
|--------|----------------|
| SQL    | MySQL          |
| SQL    | PostgreSQL     |
| NoSQL  | MongoDB        |
| NoSQL  | CouchDB        |

---

##  Repository Structure

```
.
├── mysqlcreatetext.py          # MySQL CRUD - text data
├── mysqlinsertmedia.py         # MySQL CRUD - image/audio data
├── mysqlretrieve.py
├── mysqldelete.py
├── postgrescreatetext.py       # PostgreSQL CRUD - text data
├── postgreinsertmedia.py       # PostgreSQL CRUD - image data
├── postgresinsertaudio.py      # PostgreSQL CRUD - audio data
├── postgretrive.py
├── postgresdelete.py
├── mongodbcreatetext.py        # MongoDB CRUD - text data
├── mongodbinsertimages.py      # MongoDB CRUD - image data
├── mongodbretrieverecord.py
├── mongodbdeletemedia.py
├── mongoupdate.py
├── couchcreatetext.py          # CouchDB CRUD - text data
├── couchdbcreateimage.py       # CouchDB CRUD - image data
├── couchdbcreateaudio.py       # CouchDB CRUD - audio data
├── couchdbretrive.py
├── couchupdate.py
├── couchdbdelete.py
└── emissions.csv               # Raw energy & emissions measurements
```

---

##  Methodology

Each database was subjected to identical CRUD operations across three data types to ensure a fair and consistent comparison:

- **Create** — inserting text records, images, and audio files
- **Read** — retrieving stored records
- **Update** — modifying existing records
- **Delete** — removing records from the database

Energy consumption and CO₂ equivalent emissions were tracked using the **CodeCarbon** library, which measures CPU and memory power draw during each operation. Results were logged to `emissions.csv` for analysis.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **SQL Databases:** MySQL, PostgreSQL
- **NoSQL Databases:** MongoDB, CouchDB
- **Energy Measurement:** CodeCarbon (`emissions.csv`)
- **Data Types Tested:** Text, Images, Audio

---

##  Prerequisites

Ensure you have the following installed:

```bash
pip install pymongo couchdb mysql-connector-python psycopg2 codecarbon
```

You will also need running instances of all four databases. You can use Docker for convenience:

```bash
# MySQL
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql

# PostgreSQL
docker run --name postgres-db -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres

# MongoDB
docker run --name mongo-db -p 27017:27017 -d mongo

# CouchDB
docker run --name couch-db -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin -p 5984:5984 -d couchdb
```

---

##  Running the Experiments

Each script is self-contained. Run any script to execute the corresponding CRUD operation and log emissions data:

```bash
# Example: Run MySQL text creation test
python mysqlcreatetext.py

# Example: Run MongoDB image insertion test
python mongodbinsertimages.py
```

Emissions data will be appended to `emissions.csv` automatically by CodeCarbon.

---

## Results

Raw energy and emissions measurements are stored in `emissions.csv`. Each row corresponds to a single experiment run and includes fields such as:

- `timestamp` — when the experiment ran
- `duration` — time taken (seconds)
- `emissions` — CO₂ equivalent (kg)
- `energy_consumed` — total energy used (kWh)
- `project_name` — identifies the database and operation

---

##  Key Research Questions

1. Do SQL databases consume more or less energy than NoSQL databases for equivalent CRUD operations?
2. How does data type (text vs image vs audio) affect energy consumption across database systems?
3. Which database system offers the best performance-per-watt for each operation type?

---

##  Why This Matters

Data centres account for roughly 1–2% of global electricity consumption. As developers, the database systems we choose have a real environmental impact at scale. This research contributes to the growing field of **Green Software Engineering** by providing empirical evidence to guide more sustainable architectural decisions.

---

##  Authors

- Grace Olapeju Amole
