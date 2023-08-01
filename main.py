import os
import configparser
from datetime import date

import pandas as pd

from utils import Logger

logger = Logger("Excel Generator")

logger.info("Excel generator started")

CONFIG = configparser.ConfigParser()

with open("./settings/settings.ini", "r") as file:
    CONFIG.read_file(file)

OUTPUT_PATH = CONFIG.get("paths", "output")

INPUT_PATH = CONFIG.get("paths", "input")

def read_file(path: str) -> pd.DataFrame:
    """Reads an excel file and returns a dataframe"""
    logger.info("Reading file >> {}".format(path))

    df = pd.read_excel(path)

    df = df.dropna()

    df = df.drop_duplicates()

    logger.info("Products found: {}".format(len(df)))

    return df

def generate_df(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    """Takes a list of dataframes and returns a combined df"""
    logger.info("Generating unique products...")

    df = pd.concat(dfs)

    products = []

    df_list = df.drop_duplicates().to_dict("records")

    for product in df_list:
        products.append({
            "Title": product["Title"],
            "Title_link": product["Title_link"],
            "Thumbnail": product["Thumbnail"],
            "Price": product["Price"]
        })
    
    logger.info("Unique products found: {}".format(len(products)))

    return pd.DataFrame(products)

def run() -> None:
    """Entry point to the excel generator"""
    logger.info("Finding excel files in >> {}".format(INPUT_PATH))

    dataframes = []
    files = []

    for file in os.listdir(INPUT_PATH):
        if file.endswith("xlsx"):
            files.append(file)
    
    logger.info("Files found: {}".format(len(files)))

    for file in files:
        dataframes.append(read_file(INPUT_PATH + file))
    
    final_df = generate_df(dataframes)

    logger.info("Saving data retrieved to excel...")

    name = "results_{}.xlsx".format(date.today())

    final_df.to_excel(OUTPUT_PATH + name, index=False)

    logger.info("Results saved to >> {}".format(name))


if __name__ == "__main__":
    run()