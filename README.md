# DOI to PDF resolver

## What is this?

A simple DOI to PDF resolver for your personal use, written in Python. So you can, for example, go to ...

```bash
http://localhost:5001/10.1111/isj.12343
```

... and immediately see the PDF file of the article, assuming you have completed the appropriate setup:

### Setup for SQL mode

Assuming you have:

1. Downloaded the PDF, and
2. Placed it in `doi_resolver_files`, and
3. Set up a mySQL database with table `papers` and fields `doi` and `pdf`, and
4. Registered said PDF in said mySQL table, and
5. Configured mySQL connection in `secrets_sqlmode.txt`.

### Setup for CSV mode

Assuming you have:

1. Downloaded the PDF, and
2. Placed it in a folder somewhere, and
3. Set up a CSV file with fields `doi` and `path_to_file` and `filename`, and
4. Registered said PDF in said mySQL table, and
5. Configured mySQL connection in `secrets_csvmode.txt`.


### Note

This is for your personal use because you will need to collect PDF files during your research and save them into `doi_resolver_files`. The only benefit over dx.doi.org is that you will have your files with you on the go (e.g. working without an internet connection).

## secrets_csvmode.txt expected format

```python
doipdf_mappingfile_csv = ~/00blair/path/to/mappingfile.csv
doipdf_pdfs_folder = ~/00blair/path/to/pdfs
```

## secrets_sqlmode.txt expected format

```python
host = localhost
user = blair
password = secretpassword
database = doipdf
```

## Running the server real quick

```bash
python3 -m flask run -h 0.0.0.0 -p 5001
```

## Virtualenv (venv) configuration

Load requirements from file:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements_sqlmode.txt 
```

Save requirements to file:
```bash
pip freeze > requirements_sqlmode.txt
deactivate
```