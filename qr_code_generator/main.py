import qrcode
from PIL import Image, ImageDraw

def main():

    url = input("Input the text or url your would like to be converted into a QR code: ")

    filename = input("Please enter the file name to save as: ")
    filename = filename + ".png"

    print("Generating QR code...")

    img = qrcode.make(url)

    
    img.save(filename)

    print(f"QR code generated and saved as {filename}")


if __name__ == "__main__":
    main()