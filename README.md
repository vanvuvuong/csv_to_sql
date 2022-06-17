CSV, XML TO SQL VERSION 0.1.1
===
## SETUP THE ENVIRONMENT (GUIDE FOR LINUX ONLY)
Requirement:
---
 - Docker & docker-compose. Please view the official documentations to install it: https://docs.docker.com/get-docker/
 - Create the `.env` & `to_sql/config/config.yaml` files
 - Know how to use `docker` & `docker-composer`
---
### Start the docker-compose:
---
```
docker-compose up -d
```
### Start the docker-compose & rebuild the image:
---
```
docker-compose up --build -d
```
### Stop the docker-compose:
---
```
docker-compose down
```

## GUIDE TO USE THE SCRIPT (Keep the `container` alive to run the script)
---
1. Let get into the container:
```
docker container exec -it app /bin/bash
```
2. Run this script to see command and option:
```
py main.py --help
```
3. Copy the files to folder `files` to get them ready to run

4. Example of running:

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