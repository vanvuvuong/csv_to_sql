from to_sql.libs.process_data import *

def test_process_data():
    file_name = 'to_sql/files/samples.csv'
    _table_name = re.sub('[^a-zA-Z0-9-_]', '', file_name.replace('to_sql/files/', '').split('.csv')[0])