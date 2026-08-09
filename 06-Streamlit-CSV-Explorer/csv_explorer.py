import streamlit as st
import pandas as pd

st.title("CSV Explorer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Function to load demo data
def load_demo_data():
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "signup_date": ["2023-01-01", "2023-02-15", "2023-03-20", "2023-04-10", "2023-05-05"],
        "score": [88, 92, 85, 90, 95],
    }
    df = pd.DataFrame(data)
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    return df

# Initialize variables
df = None
date_columns = []

if uploaded_file is not None:
    # Read CSV first without date parsing to detect columns
    try:
        df_sample = pd.read_csv(uploaded_file, nrows=5)
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        st.stop()

    # Detect likely date columns by name
    possible_date_cols = [col for col in df_sample.columns if "date" in col.lower()]

    st.write(f"Detected date columns: {possible_date_cols}")

    # Let user select which columns to parse as dates
    to_parse_dates = st.multiselect("Select columns to parse as dates", possible_date_cols)

    try:
        # Reload CSV with date parsing
        df = pd.read_csv(uploaded_file, parse_dates=to_parse_dates)
    except Exception as e:
        st.error(f"Error reading CSV with date parsing: {e}")
        st.stop()

else:
    st.info("No file uploaded. Using demo data.")
    df = load_demo_data()

# Show basic info
if df is not None:
    st.write(f"Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    st.write("Sample data:")
    st.dataframe(df.head())

else:
    st.warning("No data available to display.")
