# install packcage
# devtools::install_github('https://github.com/rafalab/dslabs')

# get data
gapminder_data <- dslabs::gapminder |> tibble::as_tibble()


# export data
gapminder_data |>
  arrow::write_parquet(
    sink = "gapminder_data.parquet"
  )
