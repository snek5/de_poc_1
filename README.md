# Data Engineering POC - 1
This is my repository to learn data engineering tools. I have access to Linode's Spark Cluster, Object Storage and PostgreSQL instance so I will be utilizing these resources to learn how to ingest data from CSV to an object storage and then to PostgreSQL.

```mermaid
flowchart TD
    subgraph Source_Layer["Source Layer"]
        CSV["CSV Files"]
    end

    subgraph Bronze_Layer["Bronze Layer"]
        BronzeStorage["Object Storage<br>(Bronze - Raw)"]
        Engine1["Spark / DuckDB<br><small>Ingest + Parse</small>"]
    end

    subgraph Silver_Layer["Silver Layer"]
        SilverStorage["Object Storage<br>(Silver - Cleansed)"]
        Engine2["Spark / DuckDB<br><small>Clean + Enrich</small>"]
    end

    subgraph Gold_Layer["Gold Layer"]
        GoldStorage["Object Storage<br>(Gold - Aggregated)"]
        Engine3["Spark / DuckDB<br><small>Aggregate + Serve</small>"]
    end

    subgraph Serving_Layer["Serving Layer"]
        PostgreSQL[("PostgreSQL<br>Analytics / BI Tool Access")]
    end

    CSV --> Spark
    Spark --> BronzeStorage
    BronzeStorage --> Spark
    Spark --> SilverStorage
    SilverStorage --> Spark
    Spark --> GoldStorage
    GoldStorage --> PostgreSQL
```
