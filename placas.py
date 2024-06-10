import cv2
import pytesseract
import numpy as np
import imutils 

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def preprocess_image(image):
    """Applies preprocessing steps to enhance license plate detection."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17) # Noise reduction
    edged = cv2.Canny(gray, 30, 200)  # Edge detection
    return edged

def find_contours(edged_image):
    """Finds potential license plate contours."""
    contours = cv2.findContours(edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10] # Get top 10 contours
    return contours

def detect_plate(image):
    """Detects and extracts the license plate region."""
    edged = preprocess_image(image)
    contours = find_contours(edged)

    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * peri, True)

        if len(approx) == 4: # License plates are usually rectangular
            screenCnt = approx
            x, y, w, h = cv2.boundingRect(contour)
            license_plate = image[y:y + h, x:x + w]
            return license_plate
    return None

# Read the image
image = cv2.imread('car2.JPG')
image = imutils.resize(image, width=500)

# Detect the plate region
license_plate = detect_plate(image)

if license_plate is not None:
    # Preprocess for OCR
    license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
    license_plate = cv2.threshold(license_plate, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Perform OCR
    text = pytesseract.image_to_string(license_plate, config='--psm 11')  # Use psm 11 for single line text
    print("License Plate:", text)

    # Draw and display
    cv2.imshow("License Plate", license_plate)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
