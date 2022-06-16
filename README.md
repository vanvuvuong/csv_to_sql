CSV, XML TO SQL VERSION 0.1.1
===
## SETUP THE ENVIRONMENT (GUIDE FOR LINUX ONLY)
Requirement:
---
 - Docker & docker-compose. Please view the official documentations to install it: https://docs.docker.com/get-docker/
 - Create the `.env` & `to_sql/config/config.yaml` files
---
### 1. Start the stack:
---
```
docker-compose up -d
```
### 2. Start the stack & rebuild the image:
---
```
docker-compose up --build -d
```
### 3. Stop the stack:
---
```
docker-compose down
```

## GUIDE TO USE THE SCRIPT
---
1. Let get into the container:
```
docker container exec -it app /bin/bash
```
2. Move to the script folders:
```
cd to_sql
```
3. Run this script to see command and option:
```
py main.py --help
```
4. Copy the files to folder `files` to get them ready to run

5. Example of running:

- Importing 1 csv file sample
```
py main.py csv files/sample.csv
```

- Importing 2 csv files sample
```
py main.py csv files/sample.csv files/customers.csv
```
After run the scrip, the terminal will ask you to type the `encoding`, `delimiter` and `quotechar`  of the csv files. The default values of them have been set.

- Importing 1 xml file sample
```
py main.py xml files/sample.xml
```

- Importing 2 xml files sample
```
py main.py xml files/sample.xml files/products.xml
```
After run the scrip, the terminal will ask you to type the `encoding`, `parse_type` of the xml files. The default values of them have been set.