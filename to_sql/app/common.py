from to_sql.libs.process_data import create_table_name, csv_to_frame, xml_to_frame
from to_sql.libs.db_utils import init_engine
from to_sql.libs.process_data import pd
import to_sql.libs.logger as Logger
from alive_progress.core.progress import alive_bar
from time import sleep

logger = Logger.get_instance()

def chunker(data_frame: pd.DataFrame, size: int):
    return (data_frame[pos:pos + size] for pos in range(0, len(data_frame), size))

def finish_notify():
    sleep(0.25)
    logger.info("---------------------------------------")
    sleep(0.5)
    logger.info("Finish import the data")
    sleep(0.25)
    logger.info("---------------------------------------")

def multiple_file(**kwargs):
    assert type(kwargs['files']) == tuple
    for file in kwargs['files']:
        new_kwargs = kwargs.copy()
        new_kwargs['files'] = file
        core_app(**new_kwargs)

def core_app(**kwargs):
    table_name, file_extension = create_table_name(kwargs['files'])
    engine = init_engine(kwargs['config_file'])
    logger.info(f"-----------Created table: {table_name}-----------")
    if file_extension == 'csv':
        data_frame = globals()[f"{file_extension}_to_frame"](kwargs['files'], kwargs['encoding'], kwargs['delimiter'], kwargs['quotechar'])
    elif file_extension == 'xml':
        data_frame = globals()[f"{file_extension}_to_frame"](kwargs['files'], kwargs['encoding'], kwargs['parser'])

    chunksize = int(len(data_frame)/100) or 10
    with alive_bar(int(len(data_frame)/chunksize)) as bar:
        for index, cdf in enumerate(chunker(data_frame, chunksize)):
            replace = "replace" if index == 0 else "append"
            cdf.to_sql(table_name, con=engine, if_exists=replace, index_label="index")
            bar()
    finish_notify()