# excel-gen
- Requires python 3.11+

## How it works
- It picks the files from the specified input path in settings file
- Reads those files and remove any blank lines and duplicates
- Finally, it saves the results to the output path specified in settings file

## Usage
- Open the command prompt
- Navigate to the project folder on command prompt
- If running for the first time, install dependencies using:
    
    ```pip install requirements.txt```

- Use the configuration file in settings to give the input and output paths
- Run the script using the command:

    ```python main.py```