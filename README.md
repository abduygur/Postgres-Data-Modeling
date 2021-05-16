# Postgres Data Modeling

Sparkify is a startup company which is providing music streaming to their customers in sparkify music app. The Marketing Analytics team wants to understand their customers behaviour. Currently the team can not get the customers logs easily. 

The log data and metadata are storing in JSON files. In this case data modeled in Postgres and ETL pipeline created with Python and dimension and fact tables created based on **star** schema.


## Dimension Tables
- users: customers using sparkify app
- songs: Song related data. (Song Name, Artist, Album etc.)
- artist: Artist data (Artist Name, location etc.)
- time: time of customers logs. The timestamp divided into units (hour, week, time etc.)

## Fact Table
- songplays: song plays logs

## ETL Pipeline
 - Process Data in both song_data and log_data directories using **Python** and **SQL**

## Files
    .
    |-- create_tables.py ====> Create Dimension and Fact Tables with Postgre SQL
    |-- data ================> Songs and Log Data in JSON Format
    |-- etl.ipynb ===========> ETL Scripts Notebook for test
    |-- etl.py ==============> ETL Scripts
    |-- sql_queries.py ======> All CREATE, INSERT and SELECT queries
    |-- test.ipynb ==========> Notebook for testing the ETL Scripts run correctly or not

## Libraries
    os
    glob
    psycopg2
    pandas


## How to Run

- install necessary libraries.
- run ``create_tables.py`` for creating database with SQL queries in .``sql_queries.py`` file.
- run ``etl.py`` for process log and song data and transfer to the dimension and fact tables.

