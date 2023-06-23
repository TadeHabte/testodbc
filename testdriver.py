import pyodbc
import streamlit as st
import pandas as pd

drivers = [driver for driver in pyodbc.drivers()]

df = pd.DataFrame(drivers)
df

for driver in drivers:
    print(driver)

