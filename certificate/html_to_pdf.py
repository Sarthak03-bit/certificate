import pdfkit


def generate_certificate(name, course, date):

    with open('your_file.html', 'r') as file:
        # Read the entire content of the file into a string
        html_content = file.read()

    options = {
        'orientation': 'Landscape'
    }
    # Replace the placeholders
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{course}}", course)
    html_content = html_content.replace("{{date}}", date)
    try:
        # Generate the certificate as a PDF file
        pdf = pdfkit.from_string(html_content, False)
        return pdf
    except Exception as e:
        # Handle the exception (failed to generate the PDF)

        return "failed"
