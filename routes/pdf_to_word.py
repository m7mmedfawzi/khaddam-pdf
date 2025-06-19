from flask import Blueprint, request, send_file
from pdf2docx import Converter
import uuid, os

pdf_to_word_route = Blueprint('pdf_to_word_route', __name__)

@pdf_to_word_route.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    if 'file' not in request.files:
        return 'مفيش ملف PDF', 400

    pdf = request.files['file']
    pdf_path = f'/tmp/{uuid.uuid4()}.pdf'
    docx_path = pdf_path.replace('.pdf', '.docx')

    pdf.save(pdf_path)
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        return send_file(docx_path, as_attachment=True, download_name="converted.docx")
    except Exception as e:
        return f'حصل خطأ: {str(e)}', 500
    finally:
        if os.path.exists(pdf_path): os.remove(pdf_path)
        if os.path.exists(docx_path): os.remove(docx_path)
