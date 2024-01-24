from PyPDF2 import PdfReader, PdfWriter
import os

def export_first_page(input_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_filepath = os.path.join(input_folder, filename)
            file_base_name = input_filepath.replace('.pdf', '')
            print(input_filepath)

            pdf_reader = PdfReader(input_filepath)

            pdf_writer_first_page = PdfWriter()
            pdf_writer_first_page.add_page(pdf_reader.pages[0])

            with open('{0}_KQ.pdf'.format(file_base_name), 'wb') as f:
                pdf_writer_first_page.write(f)

            pdf_writer_remaining = PdfWriter()
            for page_num in range(1, len(pdf_reader.pages)):
                pdf_writer_remaining.add_page(pdf_reader.pages[page_num])

            with open('{0}_HSKT.pdf'.format(file_base_name), 'wb') as g:
                pdf_writer_remaining.write(g)

if __name__ == "__main__":
    input_folder_path = r'D:\My Document\Code\PDFTools\Input'
    export_first_page(input_folder_path)
