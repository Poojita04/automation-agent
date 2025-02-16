import pytesseract
from PIL import Image

# Set Tesseract path (only needed for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
image_path = r"D:\TDS\automation-agent\data\credit-card.png"

image = Image.open(image_path)

# Extract text using OCR
extracted_text = pytesseract.image_to_string(image, config="--psm 6 digits")

# Remove spaces and non-numeric characters
card_number = "".join(filter(str.isdigit, extracted_text))

# Save the result
output_path = "/data/credit-card.txt"
with open(output_path, "w") as f:
    f.write(card_number)

print(f"Extracted credit card number saved to {output_path}")
