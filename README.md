# Duka Electronics Sales Exploration

## Project Summary

This project analyses Duka Electronics' 1,000 order records from January–June 2026 for the half-year sales review. Using pandas and NumPy, it investigates branch and product performance, weekend versus weekday sales, monthly revenue, and Premium Online orders from Nairobi and Mombasa. An Excel workbook complements the notebook with a SUMIFS branch ranking, an XLOOKUP region field, and a revenue-by-branch-and-channel PivotTable.

## Questions Answered

1. What do the dataset's shape, types, missing values, date range, and key categories tell us before analysis?
2. How do branches rank by total revenue and order count, and are those rankings the same?
3. Which three products lead by revenue and by units sold, and why do the lists differ?
4. How do weekday and weekend orders compare by count, total revenue, and average order revenue?
5. Which months had the highest and lowest revenue, and what is the percentage difference?
6. How many Premium Online orders came from Nairobi and Mombasa, and what revenue did they generate?
7. Can a spreadsheet reproduce the branch revenue rankings and match the pandas grand total?

## Executive Summary

- Nairobi was the top-performing branch, generating KES 26,106,100 from 376 orders.
- Laptops generated the highest product revenue at KES 41,535,000, while Tablets led unit sales with 691 units.
- Weekdays generated KES 51,856,200 from 723 orders, while weekends generated KES 19,936,300 from 277 orders and had a slightly higher average order revenue of KES 71,972.20.
- April was the strongest revenue month at KES 13,518,300, which was 23.98% higher than June, the weakest month at KES 10,903,400.
- The Premium Online segment from Nairobi and Mombasa contained 83 orders and generated KES 10,218,000 in total revenue.

## Files

- `generate_data.py` — deterministic 1,000-order generator (seed 2026).
- `duka_sales.csv` — generated data; it can be regenerated and is not required to be committed.
- `duka_sales_exploration.ipynb` — documented analysis, answers, and visible results.
- `outputs/premium_online_coast_capital.csv` — Premium Online orders from Nairobi and Mombasa, exported without the DataFrame index.
- `excel/duka_branch_summary.xlsx` — branch revenue analysis and branch/channel PivotTable.
- `requirements.txt` — Python dependencies, one per line.

## Regenerate the Data and Run the Notebook

From the repository root, install the dependencies and regenerate the CSV:

```bash
python -m pip install -r requirements.txt
python generate_data.py
```

Then open `duka_sales_exploration.ipynb` in Jupyter or VS Code and run all cells from top to bottom. The notebook reads `duka_sales.csv` from the repository root and recreates the filtered CSV under `outputs/`.
