
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import os 
import psycopg2


def get_equities():
  
    print("GETTING EQUITIES")
    """Get the url link for the Investing.com US 30 company from https://www.investing.com/equities/ and store it in a list"""
    # go to the general url for the top 30 US companies
    url = "https://www.investing.com/equities/"
    # get the URL Webpage using beautiful soup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    equities = []
    
    # Find the table in the html code with all the 30 stocks (I read the html code and found the table class)
    for link in soup.find_all("td", class_="bold left noWrap elp plusIconTd"):
        # Find the link to the company's historical data. You will need this to parse that specific page later.
        href = link.find("a").get("href")
        equity = link.find("a").get("title")
        equity_url = "https://www.investing.com" + href
        equities.append((equity, equity_url))
        
    return equities 

def get_historical_data(num_companies):
    if num_companies > 29:
        num_companies = 29
    print("GETTING HISTORICAL DATA")
    # add the historical-data link to the end of each of the urls in the list of equities
    equities_href = [(title, equities + '-historical-data') for title, equities in get_equities()]


    equities_list = []
    # loop through each of the equities and get the historical data
    for equity, url in equities_href[:num_companies]:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            # get the table with historical data 
            table = soup.find("table", class_="datatable_table__2Qbdw datatable_table--border__1hROx datatable_table--mobile-basic__2Up9u datatable_table--freeze-column__2e8u1")
            # extract the headers from the table
            headers = ["equity", "date", "price", "open", "high", "low", "olume", "change"]
           
            data = []
            # get all the historical data from the table 
            for tr in table.find_all("tr", class_="datatable_row__2vgJl"):
                row = [equity.replace(" ","")]
                print(row[0])
                for td in tr.find_all("td"):
                   
                    row.append(td.text)
                if len(row) == 8:
                    data.append(row)
            # create a dataframe for the equity and append it to the list of dataframes
            df = pd.DataFrame(data, columns=headers)
            equities_list.append(df)
        except Exception as e:
            print(e)
            continue
    return equities_list 


# def write_to_database():
df = pd.concat(get_historical_data(9))

df["date"] = pd.to_datetime(df["date"], format='%m/%d/%Y')
print(df)

DATABASE_URL = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql://')
engine = create_engine(DATABASE_URL)
# TODO: Clean right before and
df.to_sql('historical_data', engine, if_exists='replace')

"""
# def write_to_database():
#LOCAL equity_data database
engine = create_engine('postgresql://postgres@localhost:5432/equity_data')
df.to_sql('historical_data', engine, if_exists='replace')
"""
