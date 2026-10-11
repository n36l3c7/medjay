from importlib.metadata import version

from click.testing import CliRunner

from medjay import __version__
from medjay.cli import main


def test_version_option_prints_package_version() -> None:
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert result.output.strip() == f"medjay, version {__version__}"


def test_installed_metadata_matches_dunder_version() -> None:
    assert version("medjay") == __version__


def test_help_option_prints_usage() -> None:
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert result.output.startswith("Usage:")
    assert "Indicators of Compromise" in result.output
