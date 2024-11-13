# from pdf2docx import Converter

# def pdf_to_word_exact(pdf_file, word_file):
#     cv = Converter(pdf_file)
#     cv.convert(word_file, start=0, end=None, layout='exact')  # Use layout='exact' for better accuracy
#     cv.close()
#     print(f"PDF file '{pdf_file}' has been successfully converted to Word document '{word_file}' with exact formatting.")


# pdf_file = 'Original.pdf'
# word_file = 'Original.docx'

# pdf_to_word_exact(pdf_file, word_file)
# def pdf_to_word_exact(pdf_file, word_file):
#     cv = Converter(pdf_file)
#     cv.convert(word_file, start=0, end=None, layout='exact')  # Use layout='exact' for better accuracy
#     cv.close()
#     print(f"PDF file '{pdf_file}' has been successfully converted to Word document '{word_file}' with exact formatting.")


# pdf_file = 'Original.pdf'
# word_file = 'Original.docx'

# pdf_to_word_exact(pdf_file, word_file)
# def pdf_to_word_exact(pdf_file, word_file):
#     cv = Converter(pdf_file)
#     cv.convert(word_file, start=0, end=None, layout='exact')  # Use layout='exact' for better accuracy
#     cv.close()
#     print(f"PDF file '{pdf_file}' has been successfully converted to Word document '{word_file}' with exact formatting.")


# pdf_file = 'Original.pdf'
# word_file = 'Original.docx'

# pdf_to_word_exact(pdf_file, word_file)
# def pdf_to_word_exact(pdf_file, word_file):
#     cv = Converter(pdf_file)
#     cv.convert(word_file, start=0, end=None, layout='exact')  # Use layout='exact' for better accuracy
#     cv.close()
#     print(f"PDF file '{pdf_file}' has been successfully converted to Word document '{word_file}' with exact formatting.")


# pdf_file = 'Original.pdf'
# word_file = 'Original.docx'

# pdf_to_word_exact(pdf_file, word_file)



from pdf2docx import Converter

def pdf_to_word_exact():
    # Take input from the user for the PDF file name
    pdf_file = input("Enter the name of the PDF file (with extension): ")
    
    # Automatically generate the Word file name by replacing .pdf with .docx
    if pdf_file.endswith('.pdf'):
        word_file = pdf_file.replace('.pdf', '.docx')
    else:
        print("Invalid file format. Please provide a file with .pdf extension.")
        return

    # Convert the PDF to Word with exact formatting
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None, layout='exact')  # Use layout='exact' for better accuracy
    cv.close()
    
    print(f"PDF file '{pdf_file}' has been successfully converted to Word document '{word_file}' with exact formatting.")

# Call the function
pdf_to_word_exact()
