


import os
import fitz
from pypdf import PdfWriter, PdfReader

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    print("""
        ====================
        PDF Utility Toolkit
        ====================

    Merge PDF              enter ---> 1
    Split PDF              enter ---> 2
    PDF to Image           enter ---> 3
    Password Protect       enter ---> 4
    Exit                   enter ---> 5
    """)

    option = input("Choose: ")

    if option == "1":
        try:
            file1 = input("First PDF name : ")
            file2 = input("Second PDF name : ")
            output = input("Save as : ")
            writer = PdfWriter()
            reader1 = PdfReader(file1)
            reader2 = PdfReader(file2)
            for page in reader1.pages:
                writer.add_page(page)
            for page in reader2.pages:
                writer.add_page(page)
            with open(output, "wb") as f:
                writer.write(f)
            print("✅ PDFs Merged!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error :", e)

    elif option == "2":
        try:
            file = input("PDF name : ")
            start = int(input("From page? : "))
            end = int(input("To page? : "))
            output = input("Save as : ")
            reader = PdfReader(file)
            if start < 1 or end > len(reader.pages) or start > end:
                print("❌ Invalid page range!")
                continue
            writer = PdfWriter()
            for i in range(start - 1, end):
                writer.add_page(reader.pages[i])
            with open(output, "wb") as f:
                writer.write(f)
            print("✅ PDF Split!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error :", e)

    elif option == "3":
        try:
            file = input("PDF name : ")
            start = int(input("From page? : "))
            end = int(input("To page? : "))
            pdf = fitz.open(file)
            if start < 1 or end > len(pdf) or start > end:
                print("❌ Invalid page range!")
                continue
            for i in range(start - 1, end):
                page = pdf[i]
                image = page.get_pixmap()
                image.save(f"page_{i+1}.png")
            pdf.close()
            print("✅ PDF to Image Done!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error :", e)

    elif option == "4":
        try:
            file = input("PDF name : ")
            password = input("Set password : ")
            output = input("Save as : ")
            reader = PdfReader(file)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            with open(output, "wb") as f:
                writer.write(f)
            print("✅ PDF Password Protected!")
        except FileNotFoundError:
            print("❌ File not found!")
        except Exception as e:
            print("❌ Error :", e)

    elif option == "5":
        print("Bye!")
        break

    else:
        print("❌ Invalid Option!")
