# pip install Pillow reportlab
from PIL import Image
from reportlab.pdfgen import canvas

def jpg_to_pdf(input_img_path, output_pdf_path):
    img = Image.open(input_img_path)
    pdf = canvas.Canvas(output_pdf_path, pagesize=img.size)
    pdf.drawInlineImage(input_img_path, 0, 0, width=img.width, height=img.height)
    pdf.save()

if __name__ == "__main__":
    input_image = "c:/Users/Teodor/Desktop/Coding/PythonScripts/ImageToPDF/dockerfile.jpg"  # Make sure to give your exact path where you placed your image
    output_pdf = "c:/Users/Teodor/Desktop/Coding/PythonScripts/ImageToPDF/dockerfile.pdf"

    jpg_to_pdf(input_image, output_pdf)
    print(f"Conversion completed! PDF saves as {output_pdf}")    
    