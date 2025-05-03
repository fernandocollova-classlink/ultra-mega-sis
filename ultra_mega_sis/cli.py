import argparse

from ultra_mega_sis.main import main


def cli():
    parser = argparse.ArgumentParser(description="Ultra Mega SIS CLI")
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        dest="host",
        help="The host to bind the server to",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        dest="port",
        help="The port to run the server on",
    )
    return main(**vars(parser.parse_args()))


if __name__ == "__main__":
    cli()
