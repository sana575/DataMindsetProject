
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# App configuration
st.set_page_config(page_title="🚀 DataMaster Pro", layout="wide")
st.title("🚀 Data MasterPro: The Ultimate Data Sweeper 🧹")
st.write("**Your Ultimate Data Transformation and Cleaning Tool!** Upload CSV or Excel files, clean and visualize your data, and convert it to your desired format effortlessly.")

# File uploader (multiple files support)
uploaded_files = st.file_uploader("📂 Upload your files here", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error("Unsupported file type!")
            continue  # Move to next file if type is unsupported

        # Display file information
        st.write(f"*File Name:* {file.name}")
        st.write(f"*File Size:* {round(file.size/1024, 2)} KB")

        # Preview the DataFrame
        st.write("Preview of the DataFrame:")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")
                    st.dataframe(df.head())
            with col2:
                if st.button(f"Remove Missing Values from {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values Filled!")
                    st.dataframe(df.head())
            with col3:
                if st.button(f"Rename Columns for {file.name}"):
                    new_names = st.text_input("Enter new column names (comma-separated):")
                    if new_names:
                        new_names = new_names.split(',')
                        if len(new_names) == len(df.columns):
                            df.columns = new_names
                            st.write("Columns Renamed!")
                            st.dataframe(df.head())
                        else:
                            st.error("Number of new names must match the number of columns.")

        # Column Selection
        st.subheader("📌 Select Columns to Keep")
        selected_columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("🚀 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            chart_type = st.selectbox(f"Select chart type for {file.name}", ["Bar Chart", "Line Chart", "Scatter Plot"])
            if chart_type == "Bar Chart":
                st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :2])
            elif chart_type == "Line Chart":
                st.line_chart(df.select_dtypes(include=['number']).iloc[:, :2])
            elif chart_type == "Scatter Plot":
                st.write("Select two columns for the scatter plot:")
                x_axis = st.selectbox("X-axis", df.select_dtypes(include=['number']).columns)
                y_axis = st.selectbox("Y-axis", df.select_dtypes(include=['number']).columns)
                st.scatter_chart(df[[x_axis, y_axis]])

        # Conversion Options
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        custom_name = st.text_input(f"Custom output file name for {file.name} (without extension):", value=file.name.split('.')[0])

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = f"{custom_name}.csv"
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = f"{custom_name}.xlsx"
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"Download {file_name}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All files processed successfully!")