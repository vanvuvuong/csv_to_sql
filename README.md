CSV TO SQL VERSION 1.1 (USING PANDAS FOR BETTER PERFORMANCE)
===
## SETUP THE ENVIRONMENT (GUIDE FOR LINUX ONLY)

```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## GUIDE TO USE THE SCRIPT

### NOTE (THIS TOOL USE FOR MySQL SERVER ONLY):

1. Run this script to see command and option:

```
python3 main_cli.py --help
```

2. Create the `config/config.yaml` based on `config/config.sample.yaml` to connect to MySQL server


3. Copy the csv file to folder `files`

4. Example of running:
```
python3 main_cli.py files/sample.csv
```
After run the scrip, the terminal will ask you to type the `encoding`, `delimiter` and `quotechar`  of the csv files. The default values of them have been set.
