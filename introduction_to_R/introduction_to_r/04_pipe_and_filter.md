---
name: Pipe and Filter
dependsOn: [introduction_to_R.introduction_to_r.03_inspecting_your_data]
learningOutcomes:
  - Use the base R pipe for readable transformation pipelines.
  - Apply filter with logical operators, NA handling, and set membership.
---

##  The Pipe Operator & `filter()`

The pipe turns nested, inside-out function calls into a left-to-right sentence.

## The Pipe Operator `|>`

- Without the pipe, reading R code means parsing from the innermost call outward which is the opposite of how you reason about a problem.
- The pipe lets you write steps in the order they happen.

### Without the pipe

```r
# read from the inside out — unnatural
select(
  filter(ideal, ReasonsLoss1 == "survived"),
  CalfID, sublocation, Weight
)
```
### With the pipe

```r
# read left to right — matches how you think
ideal |>
  dplyr::filter(ReasonsLoss1 == "survived") |>
  dplyr::select(CalfID, sublocation, Weight)
```
> Read `|>` as **"and then"** — *take the data, **and then** filter, **and then** select.* Keyboard shortcut: **Ctrl + Shift + M** in RStudio.

## `%>%` vs `|>` — Which Pipe?

| | `%>%` (base R) | `\|>` (magrittr)|
|--|------------------|----------------|
| **Requires a package?** | Yes — loaded with tidyverse | No — built into R ≥ 4.1 |
| **Speed** | Slightly slower | Marginally faster |
| **Where you'll see it** | Most existing tidyverse tutorials | Modern R code, including this session |

```r
# these two lines produce identical output
ideal %>% filter(ReasonsLoss1 == "survived")
ideal |>  filter(ReasonsLoss1 == "survived")
```

## `filter()` — Keeping the Rows You Need

`filter()` evaluates a condition row by row and returns only the rows where the condition is `TRUE`. Every other row is silently discarded leaving the column structure is unchanged.

```r
# keep only calves that did not survive
ideal |>
  filter(ReasonsLoss1 == "died")
```

## `filter()` — Combining Conditions

- Separate conditions with a `&` for AND logic, or `|` for OR logic.
- R tests each row independently — only rows that satisfy every condition are kept.

```r
# Theileria-positive calves that survived — AND logic
ideal |>
  dplyr::filter(`Theileria.spp.` == 1 & ReasonsLoss1 == "survived") |>
  head()
```

```r
# visits from either Kidera or Igero — OR logic
ideal |>
  dplyr::filter(sublocation == "Kidera" | sublocation == "Igero") |>
  head()
```

> Column names containing `.` require backticks: `` `Theileria.spp.` ``. This friction is precisely why `rename()` matters — which we cover shortly.

## `filter()` — Handling Missing Values

Missing values are R's most common source of silent, hard-to-detect errors. The rule is simple: `NA == NA` returns `NA`, not `TRUE`. That means `filter(Weight == NA)` always returns zero rows — even when missing values exist.

```r
# use is.na() to test for missingness
ideal |>
  filter(!is.na(Weight))
```

```r
# count how many visits are missing a weight measurement
ideal |>
  filter(is.na(Weight)) |>
  nrow()
```

> `is.na()` is the only reliable way to test for missing values in R.

## `filter()` — Reference: Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `ReasonsLoss1 == "survived"` |
| `!=` | Not equal to | `sublocation != "Igero"` |
| `>` / `<` | Greater / less than | `Weight > 30` |
| `>=` / `<=` | Greater / less or equal | `ManualPCV >= 24` |
| `&` | AND — both conditions true | `` `Theileria.spp.` == 1 & ReasonsLoss1 == "died"`` |
| `\|` | OR — either condition true | `sublocation == "Kidera" \| sublocation == "Igero"` |
| `%in%` | Belongs to a set | `sublocation %in% c("Kidera", "Igero", "Bukati")` |
| `is.na()` | Is missing | `filter(is.na(Weight))` |
| `between()` | Falls within a range | `between(Age, 100, 200)` |

## `filter()` — The `%in%` Operator

- `%in%` tests membership in a set — far more readable than chaining multiple `==` conditions with `|`.
- It scales naturally: adding a fourth location is one comma, not a new line of logic.

```r
# select three specific sub-locations
ideal |>
  dplyr::filter(sublocation %in% c("Kidera", "Igero", "Luanda")) |>
  dplyr::select(CalfID, sublocation, Weight, ReasonsLoss1) |>
  head()
```

