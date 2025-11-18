#  QR Code Generator

This project is a simple Python program that generates a **QR code** based on user input. The user can enter any text, message, or URL, and the program will convert it into a scannable QR code image.

---

##  Features

* Accepts **any user input** (text, message, URL, etc.)
* Generates a QR code using the `qrcode` Python library
* Saves the QR code as an **image file (.png)**
* Can be scanned by any smartphone QR reader
* Easy to use and beginner-friendly

---

## Requirements

Make sure you have the following Python packages installed:

```bash
pip install qrcode
pip install pillow
```

These libraries allow Python to create QR codes and save them as images.

---

##  How It Works

1. The program prompts the user for text or a URL.
2. The user enters a **file name** for saving the QR code.
3. The program generates the QR code.
4. The QR code is saved as an image in the project folder.

Example output file:

```
my_qr_code.png
```

---

## How to Run the Program

Run the script with Python:

```bash
python main.py
```

When prompted, enter:

1. The text or URL you want to encode
2. The desired file name

The QR code image will be saved automatically.

---

##  Example Usage

**Input:**

```
Enter text or URL: https://github.com
File name to save as: github_qr
```

**Output:**

```
QR code saved as github_qr.png
```

---

##  Output Example

A QR code image like this will be generated:

```
[github_qr.png]
```

(Scan it with your phone to open the URL.)


