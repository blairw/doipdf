# from doi_lookup_sql import get_pdf_from_doi
from doi_lookup_csv import get_pdf_from_doi
from flask import Flask, send_file, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/doipdf/', defaults={'path': ''})
@app.route('/doipdf/<path:path>')
def catch_all(path):
    try:
        pdf_details = get_pdf_from_doi(path)
    except:
        return 'DOI not found: %s' % path
    else:
        response = send_from_directory(directory = pdf_details["folder"],
                        path = pdf_details["filepath"],
                        mimetype = 'application/pdf',
                        as_attachment = True)
        # https://stackoverflow.com/questions/41543951/how-to-change-downloading-name-in-flask
        # https://stackoverflow.com/questions/38564525/chrome-embedded-pdf-download-filename
        response.headers["x-filename"] = pdf_details["filepath"]
        response.headers["x-suggested-filename"] = pdf_details["filepath"]
        response.headers["Content-Disposition"] = 'inline; filename="' + pdf_details["filepath"] + '"'
        response.headers["Access-Control-Expose-Headers"] = 'x-filename'
        response.headers["Access-Control-Expose-Headers"] = 'x-suggested-filename'
        return response
