---
name: Joins
dependsOn: [introduction_to_R.introduction_to_r.07_group_by_and_summarise]
tags: [r, dplyr, joins, data-integration]
learningOutcomes:
  - Distinguish common join types and when to use each.
  - Join analytical and reference datasets using shared keys.
  - Diagnose unmatched keys with anti_join.
---

#  Joins

Real datasets live across multiple tables. Joins are how you reunite them, matching rows from two sources on a shared key, without manually copying values between files.

## Why Joins?

The IDEAL dataset records one row per calf visit. A separate table holds sub-location metadata — division, altitude, administrative boundaries. Joining enriches every visit row without duplicating the metadata by hand.

:::: {.columns}
::: {.column width="50%"}
**`ideal`** — Visit records

```{r}
#| label: join-left-preview
#| echo: false
ideal |> distinct(sublocation) |> arrange(sublocation)
```
:::
::: {.column width="50%"}
**`sublocation_info`** — Area metadata

```{r}
#| label: join-right-preview
#| echo: false
sublocation_info
```
:::
::::

## The Four Join Types

| Join | Result |
|------|--------|
| `left_join(x, y)` | All rows from `x`; matched columns from `y`; unmatched rows get `NA` |
| `right_join(x, y)` | All rows from `y`; matched columns from `x` |
| `inner_join(x, y)` | Only rows with a match in both tables |
| `full_join(x, y)` | All rows from both; unmatched cells get `NA` |

> `left_join()` is the workhorse of data analysis. It preserves your primary dataset intact and attaches reference information wherever a match exists. Unmatched rows are retained with `NA`, not silently lost.

## `left_join()` — Attach Without Losing Rows

```{webr-r}
#| label: left-join
# summarise to sublocation level, then attach geographic metadata
calf_summary <- ideal |>
  group_by(sublocation) |>
  summarise(
    n_calves = n_distinct(CalfID),
    mean_pcv = round(mean(ManualPCV, na.rm = TRUE), 1)
  ) |>
  ungroup()

calf_join <- calf_summary |>
  left_join(sublocation_info, by = "sublocation")

calf_join
```

> **Yiro West** has no entry in `sublocation_info`, so it receives `NA` for `division` and `altitude_m`. It is still present in the result — `left_join()` never drops a row from the left table.

## `inner_join()` — Only Complete Matches

```{webr-r}
#| label: inner-join
# only sub-locations present in both tables survive
calf_summary |>
  inner_join(sublocation_info, by = "sublocation")
```

> **Yiro West** is now absent. It had no match on the right. Use `inner_join()` when your analysis requires complete information for every row, and you are prepared to lose unmatched records.

## `anti_join()` — Diagnosing the Gaps

```{webr-r}
#| label: anti-join
# which sub-locations in the data have no metadata entry?
calf_summary |>
  anti_join(sublocation_info, by = "sublocation")
```

> `anti_join()` returns only the rows that *failed* to match. It is a data quality diagnostic. Run it before any analysis that depends on a join to catch missing reference records.

## Joining on the Full Dataset

```{webr-r}
#| label: join-raw
ideal |>
  left_join(sublocation_info, by = "sublocation") |>
  filter(!is.na(Weight)) |>
  select(CalfID, sublocation, division, altitude_m, Weight, ReasonsLoss1) |>
  head(8)
```

> When you join on the full visit-level dataset, each metadata value repeats for every row belonging to that sub-location. 

