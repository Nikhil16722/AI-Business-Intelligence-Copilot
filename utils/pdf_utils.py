import pdfplumber
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)


# -----------------------------------
# Extract Text From PDF
# -----------------------------------

def extract_pdf_text(pdf_file):

    text = ""

    try:

        with pdfplumber.open(
            pdf_file
        ) as pdf:

            for page in pdf.pages:

                page_text = (
                    page.extract_text()
                )

                if page_text:

                    text += (
                        page_text
                        + "\n"
                    )

    except Exception as e:

        text = f"""
Error reading PDF:

{str(e)}
"""

    return text


# -----------------------------------
# Generate PDF Report
# -----------------------------------

def generate_pdf_report(
    insights,
    output_path="report.pdf"
):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AI Business Intelligence Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    body = Paragraph(
        insights.replace(
            "\n",
            "<br/>"
        ),
        styles["BodyText"]
    )

    content.append(body)

    doc.build(content)

    return output_path


# -----------------------------------
# Document Stats
# -----------------------------------

def pdf_statistics(text):

    words = len(
        text.split()
    )

    chars = len(text)

    lines = len(
        text.splitlines()
    )

    return {

        "words": words,

        "characters": chars,

        "lines": lines
    }


# -----------------------------------
# Short Preview
# -----------------------------------

def preview_text(
    text,
    limit=1500
):

    if len(text) <= limit:

        return text

    return text[:limit] + "..."