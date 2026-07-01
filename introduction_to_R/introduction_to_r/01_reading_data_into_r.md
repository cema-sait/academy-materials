---
name: Reading Data into R
dependsOn: [introduction_to_R.introduction_to_r.00_getting_started_with_r]
learningOutcomes:
  - Load data from CSV and Excel files into tibbles.
  - Choose appropriate import functions for common file formats.
---

Before you can analyse data, you must load it into R. Two tidyverse packages handle virtually every file format you will encounter in practice.

## Key Packages

- `readr` reads rectangular text files.
- `readxl` reads Excel workbooks.
- Both produce a **tibble** — R's modern, opinionated data frame.

| Package | Function | Use when… |
|---------|----------|-----------|
| `readr` | `read_csv()` | Your file is `.csv` — the universal format |
| `readr` | `read_tsv()` | Columns are separated by tabs |
| `readxl` | `read_excel()` | Your file is `.xlsx` or `.xls` |

```r
library(tidyverse)
library(readxl)
```

> `readxl` is not part of the tidyverse core. Always call `library(readxl)` explicitly.

## Reading a CSV File

- `read_csv()` is the workhorse for flat files. It reads faster than base R's `read.csv()`, it never silently converts strings to factors, and prints a column-type summary on load so you always know what was parsed.

```r
# reading the data
# this should work when the file is in your working directory
ideal <- read_csv("ideal.csv")
```

## Reading an Excel File

Excel workbooks carry hidden complexity including multiple sheets, merged header rows, dates stored as serial numbers.

- `read_excel()` exposes each of these as an explicit argument, making your assumptions visible and reproducible.

```r
# this reads the first sheet by default
ideal <- read_excel("ideal.xlsx")

# precise reading, when sheets have merged titles or extra header rows
ideal <- read_excel(
  "ideal.xlsx", # excel file
  sheet = "Calf Data", # specified sheet name
  skip = 2, # skip merged title rows before the header
  col_names = TRUE # use the first row as column names
)
```

