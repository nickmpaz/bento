import sys
import argparse

from . import settings
from .link import link


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description=settings.cli_description)
    subparsers = parser.add_subparsers(dest="action")
    subparsers.required = True

    parser_link = subparsers.add_parser(
        'link', help="Symlink configuration files to their desired locations.")
    parser_link.set_defaults(func=link.link)

    args = parser.parse_args(args)
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
