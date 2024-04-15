import pandas as pd

# Adapted from https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file
secrets = {}
with open("secrets_csvmode.txt") as myfile:
    for line in myfile:
        key, value = line.partition("=")[::2]
        secrets[key.strip()] = value.strip()
        
def get_pdf_from_doi(given_doi):
  given_doi = given_doi.lower()
  df_mappingfile = pd.read_csv(secrets["doipdf_mappingfile_csv"])
  df_results = df_mappingfile[df_mappingfile['doi'].str.lower() == given_doi][['pdf']]
  
  prepared_output = {"folder": secrets["doipdf_pdfs_folder"], "filepath": df_results.iloc[0, 0]}

  return prepared_output
