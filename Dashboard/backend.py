import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    
    conn = mysql.connect(host='localhost', user='root', password="",
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    
    conn, cur = DBConnect(dbName)
    sqlFile = 'schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
            res = cur.execute(command)
    conn.commit()
    cur.close()


def insert_to_tweet_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    
    conn, cur = DBConnect(dbName)

    df = preprocess_df(df)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (created_at, source, clean_text, sentiment, polarity, subjectivity, language,
                    favorite_count, retweet_count, original_author, followers_count, friends_count, possibly_sensitive, hashtags, user_mentions, place)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14], row[15])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)


if __name__ == "__main__":
    createDB(dbName='tweets')
    createTables(dbName='tweets')

    df = pd.read_csv('../processed_tweet_data.csv')

    insert_to_tweet_table(dbName='tweets', df=df, table_name='TweetInformation')