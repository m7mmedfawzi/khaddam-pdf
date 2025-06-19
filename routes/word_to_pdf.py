from flask import Blueprint, request, send_file
import uuid, os

word_to_pdf_route = Blueprint('word_to_pdf_route', __name__)

@word_to_pdf_route.route('/convert-docx', methods=['POST'])
def convert_word_to_pdf():
    if 'file' not in request.files:
        return 'مفيش ملف Word', 400

    docx = request.files['file']
    docx_path = f'/tmp/{uuid.uuid4()}.docx'
    pdf_path = docx_path.replace('.docx', '.pdf')

    docx.save(docx_path)

    try:
        print("💡 DOCX Path:", docx_path)
        print("💡 Converting to PDF...")
        os.system(f'libreoffice --headless --convert-to pdf --outdir /tmp {docx_path}')
        
        if not os.path.exists(pdf_path):
            return '⚠️ التحويل فشل. PDF مش موجود', 500

        return send_file(pdf_path, as_attachment=True, download_name='converted.pdf')
    except Exception as e:
        return f'حصل خطأ: {str(e)}', 500
    finally:
        if os.path.exists(docx_path): os.remove(docx_path)
        if os.path.exists(pdf_path): os.remove(pdf_path)

