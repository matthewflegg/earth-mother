import pandas as pd


async def choose_fact(filepath: str):
    """
    Loads the facts spreadsheet into memory.
    """
    facts = pd.read_excel(filepath)

