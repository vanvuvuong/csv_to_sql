from to_sql.app.common import core_app, multiple_file
import to_sql.libs.logger as Logger
from typing import Tuple, Union
import click

logger = Logger.get_instance()
CONFIG_FILE_PATH = "to_sql/config/config.yaml"
@click.group()
@click.option("--log-level", default="info", show_default=True)
def main(log_level: str = "info"):
    logger.setLevel(Logger.LOG_LEVEL_BY_NAME[log_level])

@main.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option("--encoding", default="utf-8") #, prompt="Encoding:")
@click.option("--delimiter", default=",") #, prompt="Delimiter:")
@click.option("--quotechar", default="\"") #, prompt="Quote character:")
def csv(files: Union[str, Tuple[str]], encoding: str, delimiter: str, quotechar: str, config_file: str = CONFIG_FILE_PATH):
    kwargs = {
        "files": files,
        "encoding": encoding,
        "delimiter": delimiter,
        "quotechar": quotechar,
        "config_file": config_file,
    }
    if isinstance(kwargs['files'], tuple):
        multiple_file(**kwargs)
    else:
        core_app(**kwargs)

@main.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option("--encoding", default="utf-8", prompt="Encoding:")
@click.option("--parser", default="lxml", prompt="Parser mode:")
def xml(files: Union[str, Tuple[str]], encoding: str, parser: str = "lxml", config_file: str = CONFIG_FILE_PATH):
    kwargs = {
        "files": files,
        "encoding": encoding,
        "parser": parser,
        "config_file": config_file,
    }
    if isinstance(kwargs['files'], tuple):
        multiple_file(**kwargs)
    else:
        core_app(**kwargs)

main()