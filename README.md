# Medjay

IoC analysis tool that queries OSINT sources and presents readable, actionable results.

[![CI](https://github.com/n36l3c7/medjay/actions/workflows/ci.yml/badge.svg)](https://github.com/n36l3c7/medjay/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Licence: MIT](https://img.shields.io/badge/licence-MIT-green)](LICENSE)

> **Status: pre-alpha.** The project is under active development and nothing is
> released yet. The roadmap below describes what is coming; only the scaffolding
> exists today.

## What it does

Medjay takes one or many Indicators of Compromise (IPv4/IPv6 addresses, domains,
URLs, file hashes, email addresses), looks them up against OSINT sources through
their public APIs, enriches them with passive data that costs no API quota, and
shows one aggregated verdict per indicator together with the evidence from each
source. The same core powers a CLI for pipelines and a local web UI for
interactive triage.

It is built for analysts, incident responders and SOC teams who want to triage
indicators quickly without burning through free-tier API quotas.

## Roadmap

| Milestone | Scope |
|---|---|
| Core and CLI | IoC auto-detection and refanging, bulk input, concurrent rate-limited lookups, VirusTotal, table/JSON output |
| Cache | Local cache with per-source TTL, offline mode, daily quota budgets |
| Sources | AbuseIPDB, AlienVault OTX, GreyNoise, Shodan, urlscan.io |
| Enrichment | rDNS, RDAP, GeoIP/ASN from a local database, TLS certificate data |
| Allowlist | Mark your own assets as known-good without spending API calls |
| History | Record every verdict and highlight changes between checks |
| Export | JSON, JSON Lines, CSV, TSV, Markdown, HTML, STIX 2.1, MISP, Splunk lookup, plain blocklist |
| Web UI | Local server-side rendered interface with filters, detail view and export |
| Docker | Multi-stage image and Compose file for the web UI |

## Requirements

- Python 3.11 or newer.

## Installation

Medjay is not published on PyPI yet. Install from source:

```sh
git clone https://github.com/n36l3c7/medjay.git
cd medjay
python -m pip install .
```

## Quickstart

```sh
medjay --version
medjay --help
```

Lookup commands arrive with the first functional release.

## Configuration

Not applicable yet. Configuration will live in a TOML file in the platform's
standard configuration directory, with API keys read from environment variables.

## Development

```sh
git clone https://github.com/n36l3c7/medjay.git
cd medjay
python -m venv .venv
# Linux / macOS
. .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Run the checks that CI runs:

```sh
ruff check .
ruff format --check .
mypy
pytest
```

## Contributing

Issues and pull requests are welcome. Please open an issue first for anything
larger than a small fix so the approach can be agreed before you invest time in
it. All contributions must keep the test suite green and pass `ruff` and `mypy`.

## Documentation

The documentation site is published at <https://n36l3c7.github.io/medjay/>.

## Licence

[MIT](LICENSE)
