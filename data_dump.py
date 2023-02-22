import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://arunangshudas:kumkumdi@cluster0.2mavmls.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME="aps"
COLLECTION_NAME="sensor"
DATA_FILE_PATH='/Users/arunangshu/Desktop/aps-fault/dataset.csv'


if __name__=='__main__':
    df=pd.read_csv(DATA_FILE_PATH)
    print(df.shape)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted record
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)