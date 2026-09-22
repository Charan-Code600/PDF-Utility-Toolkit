




# 📄 PDF Utility Toolkit

A Python command-line tool for common PDF operations — merge, split, convert pages to images, and password-protect — all from a single menu-driven interface.

## Features

- 🔗 **Merge PDF** — combine two PDFs into one
- ✂️ **Split PDF** — extract a page range into a new PDF
- 🖼️ **PDF to Image** — save a page range as PNG images (requires PyMuPDF)
- 🔒 **Password Protect** — encrypt a PDF with a password of your choice
- 📁 Automatically adds a `.pdf` extension to output filenames if you forget it
- ⚠️ Asks before overwriting a file that already exists
- ✅ Validates page ranges and numeric input — invalid ranges or non-numeric input are rejected with a clear message instead of crashing
- 🔁 Menu loops after every operation — run as many operations as you like without restarting
- ❌ Handles missing files and invalid menu options gracefully

## Requirements

```bash
pip install pypdf
```

- **Optional:** For the "PDF to Image" feature, also install:
  ```bash
  pip install PyMuPDF
  ```
  Without it, every other feature still works — you'll just get a clear message if you try Option 3.

## How to Run

```bash
python pdf_toolkit.py
```

## How to Use

1. Run the program — a menu with 5 options appears.
2. **Merge PDF (1)** — enter the names of two existing PDFs and a name to save the merged file as.
3. **Split PDF (2)** — enter a PDF name; the tool shows how many pages it has, then asks for a page range to extract.
4. **PDF to Image (3)** — enter a PDF name and page range; each page is saved as `page_N.png` in the same folder.
5. **Password Protect (4)** — enter a PDF name and the password you want to set, then a filename to save the protected copy as.
6. **Exit (5)** — closes the program.
7. If the output filename you choose already exists, you'll be asked to confirm before it's overwritten.
8. All file paths (input and output) are relative to the folder the script is run from, unless you give a full path.

## Technologies Used

- Python
- pypdf
- PyMuPDF (fitz) — optional, for PDF-to-image conversion

## Author

**Charan Aade | Python Developer**


🔗 [GitHub](https://github.com/Charan-Code600)


