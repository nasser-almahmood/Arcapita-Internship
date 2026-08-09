# Arcapita Internship Projects

## Overview

This repository contains Python exercises and small projects completed as part of my learning and technical development during my Technology internship at Arcapita. The work progresses from basic Python syntax through conditionals and user input, general problem solving, small interactive applications, working with Python libraries, file handling and CSV analysis, basic data analysis, and a simple Streamlit application.

The projects were written incrementally while learning, so code style and structure vary between the earlier and later folders.

## Repository Structure

- **01-Python-Fundamentals** — Introductory exercises covering input handling, conditionals, and simple decision logic (e.g. age classification, day-of-week lookup, grade conversion, leap year check, password strength check).
- **02-Python-Mini-Projects** — Small interactive console applications built with loops, functions, and dictionaries/lists (e.g. a to-do list, a contact book manager, a student gradebook, a budget/expense analyzer, a number-guessing game, and a simplified survival-prediction exercise inspired by the Titanic dataset).
- **03-Problem-Solving** — Standalone algorithmic exercises (e.g. FizzBuzz, palindrome check, anagram check, word frequency counter, matrix diagonal sum).
- **04-Python-Libraries** — Practice using external libraries (`pandas`, `re`, `datetime`) to load and validate tabular data.
- **05-File-Handling-and-Data** — Reading and parsing CSV files with Python's built-in `csv` module, including a small retail analytics console that computes basic KPIs and a simplified RFM (Recency, Frequency, Monetary) customer segmentation.
- **06-Streamlit-CSV-Explorer** — A small Streamlit app for uploading and previewing a CSV file, plus a short notebook/script used to practice loading CSV data with `pandas`.

All sample CSV files in this repository (e.g. `retail.csv`, `sample_sale.csv`, `sample_emp.csv`, `transactions.csv`) contain generic, made-up placeholder data created for practice purposes.

**Note on intentionally imperfect data:** A few sample datasets contain deliberately malformed rows, used to test input validation and error-handling logic in the accompanying scripts:
- `04-Python-Libraries/transactions.csv` includes rows with an invalid price, an invalid quantity, and an incomplete date, exercised by the validation logic in `transaction_data_cleaning.py`.
- `05-File-Handling-and-Data/retail.csv` includes blank lines and one incomplete trailing row, used to exercise the row-skipping/error-handling logic in `retail_analytics_console.py` and `retail_analytics_v2.py`.

These were left unchanged intentionally and are not data errors.

## Skills Practiced

- Python
- Problem solving
- Control flow (conditionals, loops)
- Functions
- Data structures (lists, dictionaries)
- File handling
- CSV processing
- Input validation / basic error handling
- Basic data analysis
- Python libraries (`pandas`, `csv`, `re`, `datetime`)
- Streamlit

## About the Internship

These exercises were completed during my Technology internship at Arcapita as part of developing my programming and data-handling skills. They represent personal learning and practice work rather than production software.

## Disclaimer

This repository contains personal learning exercises and practice projects completed during my internship. It does not contain proprietary Arcapita source code, confidential company information, or production systems.
