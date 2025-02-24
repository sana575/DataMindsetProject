

# 🚀 DataMaster Pro - The Ultimate Data Sweeper 🧹

**DataMaster Pro** is a powerful data transformation and cleaning tool that helps you upload, clean, visualize, and convert CSV and Excel files effortlessly. Built on Streamlit, this app is designed for users who want to streamline their data processing workflow.

---

## 🌟 Features

1. **File Upload Support**:
   - Upload multiple CSV and Excel files simultaneously.
   - Supports `.csv` and `.xlsx` formats.

2. **Data Cleaning**:
   - Remove duplicates.
   - Fill missing values with column means.
   - Rename columns dynamically.

3. **Data Visualization**:
   - Interactive bar charts, line charts, and scatter plots.
   - Visualize numeric data columns.

4. **Data Conversion**:
   - Convert files to CSV or Excel format.
   - Customize output file names.

5. **User-Friendly Interface**:
   - Clean and intuitive design.
   - Real-time preview of data.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/datamaster-pro.git
   cd datamaster-pro
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. **Access the App**:
   Open your browser and go to `http://localhost:8501`.

---

## 📂 File Structure

```
datamaster-pro/
├── app.py                # Main Streamlit application
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── assets/               # Optional: Folder for images or resources
```

---

## 🚀 Usage

1. **Upload Files**:
   - Click on the "Upload your files here" button to upload CSV or Excel files.

2. **Clean Data**:
   - Use the data cleaning options to remove duplicates, fill missing values, or rename columns.

3. **Visualize Data**:
   - Select columns and choose a chart type (bar, line, or scatter plot) to visualize your data.

4. **Convert Files**:
   - Convert your cleaned data to CSV or Excel format and download it with a custom file name.

---

## 📝 Requirements

The following Python packages are required to run the app:

- `streamlit>=1.0.0`
- `pandas>=2.0.0`
- `openpyxl>=3.0.0`
- `xlrd>=2.0.1` (for older Excel `.xls` format support)

---

## 🐛 Troubleshooting

1. **ImportError: Missing `openpyxl`**:
   - Install `openpyxl` using:
     ```bash
     pip install openpyxl
     ```

2. **File Upload Issues**:
   - Ensure the file size is within Streamlit's limits.
   - Check the file format (only `.csv` and `.xlsx` are supported).

3. **App Crashes**:
   - Make sure all dependencies are installed correctly.
   - Check the logs for detailed error messages.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- Built with ❤️ using [Streamlit](https://streamlit.io/).
- Powered by [Pandas](https://pandas.pydata.org/) for data manipulation.

---

## 📬 Contact

For questions or feedback, feel free to reach out:

- **GitHub**:[https://github.com/sana575/DataMindsetProject]

---

Enjoy using **DataMaster Pro**! 🎉
