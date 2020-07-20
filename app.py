from doi_lookup import get_pdf_from_doi
from flask import Flask, send_file, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/doipdf/', defaults={'path': ''})
@app.route('/doipdf/<path:path>')
def catch_all(path):
    try:
        pdf_filename = get_pdf_from_doi(path) + '.pdf'
    except:
        return 'DOI not found: %s' % path
    else:
        response = send_from_directory(directory='doi_resolver_files',
                        filename=pdf_filename,
                        mimetype='application/pdf',
                        attachment_filename=pdf_filename)
        # https://stackoverflow.com/questions/41543951/how-to-change-downloading-name-in-flask
        # https://stackoverflow.com/questions/38564525/chrome-embedded-pdf-download-filename
        response.headers["x-filename"] = pdf_filename
        response.headers["x-suggested-filename"] = pdf_filename
        response.headers["Content-Disposition"] = 'inline; filename="' + pdf_filename + '"'
        response.headers["Access-Control-Expose-Headers"] = 'x-filename'
        response.headers["Access-Control-Expose-Headers"] = 'x-suggested-filename'
        return response