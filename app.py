from flask import Flask, request, send_file
from pdf2docx import Converter
import os, uuid

app = Flask(__name__)

@app.route('/')
def home():
    return 'خدّام شغال 💪'

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    if 'file' not in request.files:
        return 'مفيش ملف PDF', 400

    pdf = request.files['file']
    pdf_path = f'/tmp/{uuid.uuid4()}.pdf'
    docx_path = pdf_path.replace('.pdf', '.docx')

    pdf.save(pdf_path)

    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    return send_file(docx_path, as_attachment=True, download_name='converted.docx')
