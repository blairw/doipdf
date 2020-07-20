# DOI to PDF resolver

## What is this?

A simple DOI to PDF resolver for your personal use, written in Python. So you can, for example, go to ...

```bash
http://localhost:5000/doipdf/10.1177/2053168016653424
```

... and immediately see the PDF file of the article, assuming you have:

1. Downloaded the PDF, and
2. Placed it in `doi_resolver_files`, and
3. Set up a mySQL database with table `papers` and fields `doi` and `pdf`, and
4. Registered said PDF in said mySQL table, and
5. Configured mySQL connection in `secrets.txt`.

This is for your personal use because you will need to collect PDF files during your research and save them into `doi_resolver_files`. The only benefit over dx.doi.org is that you will have your files with you on the go (e.g. working without an internet connection).

## secrets.txt expected format

```python
host = localhost
user = blair
password = secretpassword
database = doitopdfresolver
```

## Running the server real quick

```bash
python3 -m flask run --host=0.0.0.0
```

## Virtualenv (venv) configuration

Load requirements from file:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt 
```

Save requirements to file:
```bash
pip freeze > requirements.txt
deactivate
```