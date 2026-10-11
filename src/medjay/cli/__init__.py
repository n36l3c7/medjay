"""Command-line interface for Medjay."""

import click

from medjay import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, prog_name="medjay")
def main() -> None:
    """Look up Indicators of Compromise against OSINT sources."""
