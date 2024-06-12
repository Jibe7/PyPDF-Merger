from pypdf import PdfMerger

# pdfs = ["fileOne.pdf", "fileTwo.pdf"]

merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

merger.append(r"C:\Users\JB_sansdroits\Documents\ENSEA Diploma.pdf")
merger.append("C://Users//JB_sansdroits//Documents//Archives//Project Archives//2024 PC MH//PC Marc.pdf")

# merge.append("one.pdf", pages=(0, 4, 2)) # means we consider the pages in the range from 0 to 4 with a step of 2.


merger.write("ExampleFolder/DiplomaAndPC.pdf")
merger.close()