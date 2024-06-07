from pypdf import PdfMerger

pdfs = ["fileOne.pdf", "fileTwo.pdf"]

merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

merger.append("TA1+Form - Completed no signature.pdf", pages=(0, 1))
merger.append("TA1+Form - Completed signed.pdf")
merger.append("last page to merge.pdf")

# merge.append("one.pdf", pages=(0, 4, 2)) # means we consider the pages in the range from 0 to 4 with a step of 2.


merger.write("merged.pdf")
merger.close()