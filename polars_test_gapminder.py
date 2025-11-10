# %% Import librarys ==============================================================
import polars as pl
import plotly.express as px
import pyarrow

# %% Import data ==============================================================
gapminder = pl.read_parquet("gapminder_data.parquet")

# %% See data structure ==============================================================
gapminder.dtypes
gapminder.schema

# %% Fix column types ==============================================================
gapminder_ft = gapminder.with_columns(
    [
        # from caegorical to utf8 (string)
        pl.col("country").cast(pl.Utf8),
        pl.col("continent").cast(pl.Utf8),
        pl.col("region").cast(pl.Utf8),
    ]
)

# %% Check structure and see first rows ===============================================
gapminder_ft.schema
gapminder_ft.head(10)
