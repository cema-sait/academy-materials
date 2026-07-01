---
name: Select and Rename
dependsOn: [introduction_to_R.introduction_to_r.04_pipe_and_filter]
tags: [r, dplyr, select, rename, arrange]
learningOutcomes:
  - Select, drop, and pattern-match columns efficiently.
  - Rename fields for cleaner and more readable analysis.
  - Sort rows using arrange and descending order.
---

# ️ `select()` & `rename()`

- A well-structured analysis uses only the columns it needs, named in a way that makes code self-explanatory.
- `select()` shapes the column space;
- `rename()` removes the friction of working with raw source names.

## `select()` — Choosing Your Columns

Pass column names directly. `select()` returns a tibble with exactly those columns in the order you listed them. Rows are untouched.

```{webr-r}
#| label: select-basic
ideal |>
  dplyr::select(CalfID, sublocation, CalfSex, Weight, ManualPCV, `Theileria.spp.`, ReasonsLoss1)
```

> Columns with `.` in their names still require backticks inside `select()`. One of many reasons to `rename()` early.

## `select()` — Dropping Columns

Prefix any name with `-` to drop it instead of keeping it. When you want most columns but not a few, dropping is more concise than listing every keeper.

```{webr-r}
#| label: select-drop
# removing columns
ideal |>
  select(-CADOB, -VisitID, -VisitWeek, -WeightMax, -WeightMin)
```

## `select()` — Helper Functions

When a dataset has dozens of columns, selecting by pattern is more robust than listing names.

```{webr-r}
#| label: select-helpers
# select both ELISA columns without naming them explicitly
ideal |>
  select(CalfID, starts_with("ELISA")) |>
  head(n = 1)
```

| Helper | Selects columns whose names… |
|--------|------------------------------|
| `starts_with("x")` | Begin with "x" |
| `ends_with("x")` | End with "x" |
| `contains("x")` | Contain "x" anywhere |
| `where(is.numeric)` | Pass a type test |
| `everything()` | Are not already selected |

## `rename()`

- You have now seen the friction that raw source names create — backticks for `Theileria.spp.`, uppercase everywhere, cryptic codes like `ReasonsLoss1`. `rename()` removes that friction permanently. Do it once, and every line that follows is cleaner.

```{webr-r}
#| label: rename-basic
# syntax: rename(new_name = old_name)
ideal |>
  rename(
    sex = CalfSex,
    theileria = `Theileria.spp.`,
    outcome = ReasonsLoss1
  ) |>
  select(CalfID, sex, theileria, outcome) |>
  head(2)
```

## `arrange()` — Sorting Rows

- `arrange()` reorders rows by one or more columns. Unlike `filter()`, it never removes rows it only changes their order.

```{webr-r}
#| label: arrange
# which calves were heaviest at the time of their visit?
ideal |>
  filter(!is.na(Weight)) |>
  select(CalfID, sublocation, Age, Weight, ReasonsLoss1) |>
  arrange(desc(Weight)) |> # from largest to smallest.
  head(5)
```

