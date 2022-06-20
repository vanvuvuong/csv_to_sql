from to_sql.libs.process_data import create_table_name

def test_create_table_name(benchmark):
    file_name = 'to_sql/files/samples.csv'
    expected_result = 'samples', 'csv'
    result = create_table_name(file_name)
    benchmark(create_table_name, file_name)
    assert expected_result[0] == result[0].split('_')[0]
    assert expected_result[1] == result[1]