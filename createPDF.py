from reportlab.pdfgen import canvas

pdf_file = canvas.Canvas("clcodingpdff.pdf")

pdf_file.drawString(100, 750, "Hello, this is a PDF file created using ReportLab.")
pdf_file.drawString(100, 730, "This is a new line in the PDF.")
pdf_file.drawString(100, 710, "You can add more text and customize it as needed.")
pdf_file.drawString(100, 690, "This is another line.")
pdf_file.drawString(100, 670, "You can also add images, tables, and more.")
pdf_file.drawString(100, 650, "This is a simple example of creating a PDF.")
pdf_file.drawString(100, 630, "You can use different fonts and styles.")
pdf_file.drawString(100, 610, "This is a demonstration of the ReportLab library.")
pdf_file.drawString(100, 590, "You can create complex layouts and designs.")
pdf_file.drawString(100, 570, "This is the end of the example.")
pdf_file.drawString(100, 550, "Thank you for using ReportLab!")
pdf_file.save()