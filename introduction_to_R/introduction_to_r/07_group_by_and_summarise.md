---
name: Group By and Summarise
dependsOn: [introduction_to_R.introduction_to_r.06_mutate_and_case_when]
learningOutcomes:
  - Aggregate datasets with grouped and ungrouped summaries.
  - Use summary functions to compute counts and descriptive statistics.
---

##  `group_by()` & `summarise()`

Most research questions are comparisons: **Does this outcome differ across groups?** `group_by()` and `summarise()` are how tidyverse answers them

## `summarise()` — The Baseline

Without a grouping, `summarise()` collapses the entire dataset to a single summary row. This is your reference point.

```r
ideal |>
  summarise(
    n_visits = n(),
    n_calves = n_distinct(CalfID),
    mean_weight = round(mean(Weight, na.rm = TRUE), 1),
    mean_pcv = round(mean(ManualPCV, na.rm = TRUE), 1),
    theileria_pos = sum(`Theileria.spp.` == 1, na.rm = TRUE)
  )
```

> `na.rm = TRUE` tells R to ignore missing values when computing the mean. Without it, any column containing a single `NA` returns `NA` as the summary.

## `group_by()` + `summarise()`

- Add `group_by()` and every summary is computed independently for each group. The result is one row per unique combination of grouping variables.
- Call `ungroup()` afterwards to release the grouping structure.

```r
result <- ideal |>
  group_by(sublocation, ReasonsLoss1) |>
  summarise(
    n_calves = n_distinct(CalfID),
    mean_weight = round(mean(Weight,    na.rm = TRUE), 1),
    mean_pcv = round(mean(ManualPCV, na.rm = TRUE), 1)
  ) |>
  ungroup() |>
  arrange(sublocation, ReasonsLoss1)
result
```

## Disease Burden by Outcome

```r
ideal |>
  group_by(ReasonsLoss1) |>
  summarise(
    n_calves = n_distinct(CalfID),
    theileria_pos = sum(`Theileria.spp.` == 1, na.rm = TRUE),
    theileria_pct = round(mean(`Theileria.spp.` == 1, na.rm = TRUE) * 100, 1),
    mean_pcv = round(mean(ManualPCV, na.rm = TRUE), 1),
    mean_adwg = round(mean(ADWG,      na.rm = TRUE), 3)
  ) |>
  ungroup()
```

## Common Summary Functions

| Function | Computes |
|----------|----------|
| `n()` | Number of rows in the group |
| `n_distinct(x)` | Number of unique values |
| `sum(x, na.rm = TRUE)` | Total — events, counts, doses |
| `mean(x, na.rm = TRUE)` | Average |
| `median(x, na.rm = TRUE)` | Median — robust to outliers |
| `sd(x, na.rm = TRUE)` | Standard deviation |
| `min(x)` / `max(x)` | Minimum and maximum |
| `sum(is.na(x))` | Count of missing values |
| `mean(condition)` | Proportion satisfying a condition |

> Every numeric summary on real data should carry `na.rm = TRUE`. Missing values will otherwise silently propagate as `NA` in your output.

