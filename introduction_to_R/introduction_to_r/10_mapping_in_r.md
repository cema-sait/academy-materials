---
name: Mapping in R
dependsOn: [introduction_to_R.introduction_to_r.09_data_visualisation]
learningOutcomes:
  - Work with spatial data using sf objects.
  - Build choropleth maps by joining geographic and tabular data.
  - Interpret common ggplot2 geometries for analysis communication.
---

## Maps in R — `sf` and `ggplot2`

Spatial analysis in R centres on the **`sf`** package — *simple features* — which stores geographic shapes as ordinary data frames with a special **geometry column** attached. Every dplyr verb works on `sf` objects: `filter()`, `mutate()`, `left_join()`, and so on.

Two key ideas to remember:

- `st_read()` reads a GeoPackage (or shapefile) into a data frame with geometry — exactly like `read_csv()` reads a CSV
- `geom_sf()` renders the geometry column automatically inside ggplot2 — no coordinate wrangling needed


```r
kenya
```

## `geom_sf()` — Kenya Boundaries

```r
ggplot(data = kenya) +
  geom_sf(fill = "white", colour = "black", linewidth = 0.4) +
  theme_void() +
  labs(title = "Kenya — County Boundaries (47 Counties)")
```


## `geom_sf()` — Result

```r
ggplot(data = kenya) +
  geom_sf(fill = "white", colour = "black", linewidth = 0.4) +
  theme_void() +
  labs(title = "Kenya — County Boundaries (47 Counties)")
```
`geom_sf()` is the spatial equivalent of `geom_col()` — you supply a data frame and ggplot2 handles all coordinate projection and border drawing.

**What you get**

- All 47 county borders from a single function call
- The `geometry` column is detected automatically — no `x =` or `y =` needed

> **Try it:** change `fill = "#f0f4f8"` to `fill = "#185FA5"` and re-run to colour every county blue.
## Preparing the Choropleth — Cattle Population

Filter the population data to one species and build the joined spatial table.

```r
# filter to a single species
cattle <- population |>
  filter(Species == "Cattle(Total)")

# county names in the shapefile don't always match the CSV exactly —
# case_when() fixes four known mismatches before the join
cattle_map <- kenya |>
  rename(county = ADM1_EN) |>
  mutate(county = case_when(
    county == "Murang'a" ~ "Muranga",
    county == "Elgeyo-Marakwet" ~ "Elgeyo Marakwet",
    county == "Tharaka-Nithi" ~ "Tharaka Nithi",
    county == "Trans Nzoia" ~ "Trans-Nzoia",
    TRUE ~ county
  )) |>
  left_join(cattle, by = "county")

cattle_map |> select(county, value)
```

> The `case_when()` step is a real-world data quality step — spelling mismatches between datasets are extremely common. Always check with `setdiff(table_a$key, table_b$key)` before any join.

## Choropleth — Cattle Population

```r
ggplot(data = cattle_map) +
  geom_sf(aes(fill = value), colour = "black", linewidth = 0.3) +
  scale_fill_gradient(low = 'lightyellow', 
                      high = 'darkred', 
                      labels = scales::comma,
                      name = "Cattle") +
  theme_void() +
  labs(title = "Cattle Population by County — Kenya")
```


## Choropleth — Result

```r
cattle <- population |>
  filter(Species == "Cattle(Total)")
cattle_map <- kenya |>
  rename(county = ADM1_EN) |>
  mutate(county = case_when(
    county == "Murang'a" ~ "Muranga",
    county == "Elgeyo-Marakwet" ~ "Elgeyo Marakwet",
    county == "Tharaka-Nithi" ~ "Tharaka Nithi",
    county == "Trans Nzoia" ~ "Trans-Nzoia",
    TRUE ~ county
  )) |>
  left_join(cattle, by = "county")
ggplot(data = cattle_map) +
  geom_sf(aes(fill = value), colour = "black", linewidth = 0.3) +
  scale_fill_gradient(low = 'lightyellow', 
                      high = 'darkred', 
                      labels = scales::comma,
                      name = "Cattle") +
  theme_void() +
  labs(title = "Cattle Population by County — Kenya")
```
`left_join()` connects the spatial data frame to the CSV table on the shared `county` key — ggplot2 maps `value` to `fill` exactly as it would for a bar chart.

**Reading the map**

- Darker red = larger cattle population
- Turkana county typically show the highest density

> **Try it:** go back, change `"Cattle(Total)"` to `"Goats"` in the `filter()`, re-run both slides, then advance — observe how the spatial pattern shifts between species.
## ggplot2 Reference — Common Geometries

| Geometry | Best for | Key aesthetics |
|----------|----------|----------------|
| `geom_bar()` | Counts from raw data | `x`, `fill` |
| `geom_col()` | Pre-summarised counts / values | `x`, `y`, `fill` |
| `geom_point()` | Scatter — two continuous variables | `x`, `y`, `colour`, `size` |
| `geom_line()` | Trends over time | `x`, `y`, `group`, `colour` |
| `geom_boxplot()` | Distribution by group | `x`, `y`, `fill` |
| `geom_histogram()` | Distribution of one variable | `x`, `fill` |
| `geom_sf()` | Spatial features / maps | `fill`, `colour` |

> Every geometry inherits aesthetics from `ggplot(aes(...))`. You override them inside the `geom_*()` call when one layer needs different mappings.
