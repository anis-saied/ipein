def convert_python_to_pdf(input_file, output_file):
    # Read the Python code from the input file
    with open(input_file, 'r') as file:
        python_code = file.read()

    # Create HTML content with syntax highlighting
    formatter = HtmlFormatter(style='vs', fontsize=12)  # Set font size to 12
    highlighted_code = highlight(python_code, PythonLexer(), formatter)

    # Prepare HTML content with custom header and footer
    custom_header = """
    <div style="text-align: center; font-size: 16px; font-weight: bold;">
        Custom Header
    </div>
    """
    
    custom_footer = """
    <div style="text-align: center; font-size: 12px;">
        Page <span class="page"></span> of <span class="topage"></span>
    </div>
    """

    html_content = f"""
    <html>
    <head>
        <style>{formatter.get_style_defs()}</style>
    </head>
    <body>
        {custom_header}
        <h1>IPIEN</h1>
        <hr>
        {highlighted_code}
        {custom_footer}
    </body>
    </html>
    """

    # Generate PDF from HTML content
    with open(output_file, 'w+b') as pdf_file:
        pisa.pisaDocument(html_content, pdf_file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_py_to_pdf.py input_file.py output_file.pdf")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".pdf"

    convert_python_to_pdf(input_file, output_file)

    print(f"Conversion completed. PDF file saved as {output_file}")

