




import os
from pypdf import PdfWriter, PdfReader

try:
    import fitz  
    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def ensure_pdf_extension(name):
    return name if name.lower().endswith(".pdf") else name + ".pdf"


def confirm_overwrite(path):
    if os.path.exists(path):
        choice = input(f"⚠️  '{path}' already exists. Overwrite? (yes/no): ").strip().lower()
        return choice == "yes"
    return True


while True:
    print("""
           ╔══════════════════════════════════╗
           ║       PDF UTILITY TOOLKIT        ║
           ╚══════════════════════════════════╝

**********************************************************

        Merge PDF                        Enter  →  1
        Split PDF                        Enter  →  2
        PDF to Image                     Enter  →  3
        Password Protect                 Enter  →  4
        Exit                             Enter  →  5

***********************************************************
    """)

    option = input("Choose: ")

    if option == "1":
        try:
            file1 = input("First PDF name: ").strip()
            file2 = input("Second PDF name: ").strip()
            output = ensure_pdf_extension(input("Save as: ").strip())

            if not confirm_overwrite(output):
                print("❌ Cancelled.")
                continue

            writer = PdfWriter()
            reader1 = PdfReader(file1)
            reader2 = PdfReader(file2)
            for page in reader1.pages:
                writer.add_page(page)
            for page in reader2.pages:
                writer.add_page(page)
            with open(output, "wb") as f:
                writer.write(f)
            print(f"✅ PDFs Merged into {output}!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error:", e)

    elif option == "2":
        try:
            file = input("PDF name: ").strip()
            reader = PdfReader(file)
            total_pages = len(reader.pages)
            print(f"ℹ️  This PDF has {total_pages} page(s).")
            start = int(input("From page? : "))
            end = int(input("To page? : "))
            if start < 1 or end > total_pages or start > end:
                print("❌ Invalid page range!")
                continue
            output = ensure_pdf_extension(input("Save as: ").strip())
            if not confirm_overwrite(output):
                print("❌ Cancelled.")
                continue
            writer = PdfWriter()
            for i in range(start - 1, end):
                writer.add_page(reader.pages[i])
            with open(output, "wb") as f:
                writer.write(f)
            print(f"✅ PDF Split into {output}!")
        except FileNotFoundError:
            print("❌ File not found!")
        except ValueError:
            print("❌ Page numbers must be numeric!")
        except Exception as e:
            print("❌ Error:", e)

    elif option == "3":
        if not FITZ_AVAILABLE:
            print("❌ This feature needs PyMuPDF. Install it with: pip install PyMuPDF")
            continue
        try:
            file = input("PDF name: ").strip()
            pdf = fitz.open(file)
            total_pages = len(pdf)
            print(f"ℹ️  This PDF has {total_pages} page(s).")
            start = int(input("From page? : "))
            end = int(input("To page? : "))
            if start < 1 or end > total_pages or start > end:
                print("❌ Invalid page range!")
                pdf.close()
                continue
            for i in range(start - 1, end):
                page = pdf[i]
                image = page.get_pixmap()
                image.save(f"page_{i+1}.png")
            pdf.close()
            print(f"✅ Saved pages {start}-{end} as images!")
        except FileNotFoundError:
            print("❌ File not found!")
        except ValueError:
            print("❌ Page numbers must be numeric!")
        except Exception as e:
            print("❌ Error:", e)

    elif option == "4":
        try:
            file = input("PDF name: ").strip()
            password = input("Set password: ")
            if not password:
                print("❌ Password cannot be empty!")
                continue
            output = ensure_pdf_extension(input("Save as: ").strip())
            if not confirm_overwrite(output):
                print("❌ Cancelled.")
                continue
            reader = PdfReader(file)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            with open(output, "wb") as f:
                writer.write(f)
            print(f"✅ PDF Password Protected as {output}!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error:", e)

    elif option == "5":
        print("👋 Bye!")
        break

    else:
        print("❌ Invalid Option!")






