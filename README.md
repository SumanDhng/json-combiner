# JSON File Combiner

This script processes JSON files within a specified directory and its subdirectories. It reads the JSON data from provided files, combines the data into a list, and then exports the combined data into both a sinlge JSON and an Excel file.

## Requirements

Install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the script.

2. Run the script by executing the following command:

    ```
    py main.py
    ```

3. When prompted, enter the path of the folder containing the JSON files.

4. The script will process the JSON files, create an `json_combined.json` file containing the combined JSON data, and generate an `combined_output.xlsx` file with the data in an Excel format.