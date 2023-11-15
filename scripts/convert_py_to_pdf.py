import sys
import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from xhtml2pdf import pisa

def convert_python_to_pdf(input_file, output_file):
    try:
        # Read the Python code from the input file
        with open(input_file, 'r') as file:
            python_code = file.read()

        # Create HTML content with syntax highlighting
        formatter = HtmlFormatter(style='vs')  # or use 'colorful'
        highlighted_code = highlight(python_code, PythonLexer(), formatter)

        # Prepare HTML content
        html_content = f"""
        <html>
        <head>
            <style>{formatter.get_style_defs()}</style>
        </head>
        <body>
            {highlighted_code}
        </body>
        </html>
        """

        # Generate PDF from HTML content
        with open(output_file, 'w+b') as pdf_file:
            pisa.pisaDocument(html_content, pdf_file)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_py_to_pdf.py input_file.py")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".pdf"

    convert_python_to_pdf(input_file, output_file)

    print(f"Conversion completed. PDF file saved as {output_file}")

