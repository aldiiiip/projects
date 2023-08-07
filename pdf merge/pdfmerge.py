from PyPDF2 import PdfMerger, PdfWriter
import os

def merge_pdfs_in_directory(directory):
    merger = PdfMerger()

    #list all the pdf in the directory
    for root, dirs, files in os.walk(directory):
        pdf_files = [pdf for pdf in files if pdf.lower().endswith('.pdf')]

        print("Available PDF files:")
        for idx, pdf in enumerate(pdf_files):
            print(f"{idx + 1}. {pdf}")

        selected_order = input("Enter the order of PDF files (comma-separated numbers): ")
        selected_indices = [int(i.strip()) - 1 for i in selected_order.split(',')]

        for index in selected_indices:
            if 0 <= index < len(pdf_files):
                pdf_path = os.path.join(root, pdf_files[index])
                merger.append(pdf_path)
            else:
                print(f"Invalid index: {index + 1}")
    
    # Get user's home directory
    home_directory = os.path.expanduser("~")

    # Set the output path in the "Downloads" directory
    output = os.path.join(home_directory, "Downloads", input("Enter output PDF file: "))
    merger.write(output)
    merger.close()

    print(f"Merged PDF saved as '{output}'")

if __name__ == "__main__":
    directory = input("Enter directory containing PDF files: ")
    merge_pdfs_in_directory(directory)






