
# import librarys
import polars as pl
import plotly.express as px
import pyarrow

# import data
gapminder = pl.read_parquet("gapminder_data.parquet")

# see data structure
gapminder.dtypes
gapminder.schema

# fix types of columns
gapminder_ft = (
  gapminder
  .with_columns([
    # from caegorical to utf8 (string)
    pl.col('country').cast(pl.Utf8),
    pl.col('continent').cast(pl.Utf8),
    pl.col('region').cast(pl.Utf8)
  ])
)

# check structure
gapminder_ft.schema

# see first 10 rows
gapminder_ft.head(10)

