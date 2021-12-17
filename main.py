from pandas.core.frame import DataFrame
import streamlit as st
import pymongo
from pandas import DataFrame

def set_dataframe(data):
    
    mask = data["Price"].str.contains("<NA>")
    st.write(mask)
    mask1 = data["Flat_price"].str.contains("<NA>")
    print(mask1)
    return data[(~mask) & (~mask1)]

def main():
    cluster = pymongo.MongoClient("mongodb+srv://simplon:simplon@cluster0.4i0sl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Scraping"]
    game_instant = DataFrame(list(db["Instant"].find({}, {"_id" : 0})))
    game_g2a = DataFrame(list(db["G2a"].find({}, {"_id" : 0})))
    game_instant = set_dataframe(game_instant)
    game_g2a = set_dataframe(set_dataframe(game_g2a))
    
    
    container_instant = st.container()
    container_g2a = st.container()
    with container_instant:
        container_instant.title("Jeux Instant gaming info :")
        container_instant.dataframe(game_instant)
    with container_g2a:
        container_instant.title("Jeux G2a info :")
        container_instant.dataframe(game_g2a)
    
    
main()