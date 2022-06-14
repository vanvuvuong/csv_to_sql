CSV, XML TO SQL VERSION 0.1.0
===
## SETUP THE ENVIRONMENT (GUIDE FOR LINUX ONLY)

---
### 0. Install poetry:
---
1. Official Documents:
https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions

- Or running this command:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
2. Update poetry virtual environment to in project command:
```
poetry config virtualenvs.in-project true
```
---
### 1. Install virtual environment:
---
1. Install with poetry:
```
poetry install
```

2. Active the virtual environment:
```
source .venv/bin/activate
```
---
## GUIDE TO USE THE SCRIPT
---
### NOTE (THIS TOOL WAS TESTED FOR MySQL SERVER ONLY):
Move to the script folders
```
cd to_sql
```
1. Run this script to see command and option:

```
python3 main.py --help
```

2. Create the `config/config.yaml` based on `config/config.sample.yaml` to connect to MySQL server


3. Copy the files to folder `files`

4. Example of running:

- Importing 1 csv file sample
```
python3 main.py csv files/sample.csv
```

- Importing 2 csv files sample
```
python3 main.py csv files/sample.csv files/customers.csv
```
After run the scrip, the terminal will ask you to type the `encoding`, `delimiter` and `quotechar`  of the csv files. The default values of them have been set.

- Importing 1 xml file sample
```
python3 main.py csv files/sample.xml
```

- Importing 2 xml files sample
```
python3 main.py xml files/sample.xml files/products.xml
```
After run the scrip, the terminal will ask you to type the `encoding`, `parse_type` of the xml files. The default values of them have been set.