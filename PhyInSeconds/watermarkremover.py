import fitz 
 # PyMuPDF

def remove_email_watermark(input_pdf_path, output_pdf_path, email_address):
    doc = fitz.open(input_pdf_path)

    for page in doc:
        # Example: Coordinates of the watermark to cover
        watermark_area = fitz.Rect(100, 200, 300, 220)  # You need to adjust this
        # Cover the watermark area with a rectangle that matches the background
        page.insert_rectangle(watermark_area, color=(1, 1, 1), fill=(1, 1, 1))
        
        # Attempt to redraw text that was supposed to be in the area
        # NOTE: Highly manual, you need to adjust position, font, size, and the text itself
        text_to_redraw = email_address
        page.insert_text((105, 210), text_to_redraw, fontsize=11, fontname="helv", color=(0, 0, 0))

    doc.save(output_pdf_path)
    doc.close()

# Usagepdf
input_pdf_path = 'PhyInSeconds/1-Day-1 Nervous System Lecture Notes.pdf'
output_pdf_path = 'output.pdf'
email_address = 'mailto:hannanujjan39@gmail.com'  # The email link to look for
remove_email_watermark(input_pdf_path, output_pdf_path, email_address)
