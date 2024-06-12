from pypdf import PdfMerger
from typing import List

pdfsPath = []


def mergePDFs(pdfs : List[str], mergedPDFName : str) -> None:
    """ Merges input PDFs into one and choose the name for the merged pdf. 
    
    Parameters
    ----------------
    pdfs
        Represents the filenames of the PDFs we want to merge.
        Can be in one of the following format :
        r"C:\Path\To The File\File.pdf"
        "C://Path//To The File//File.pdf"
    mergedPDFName
        The name of the output file.
        In the form : "mergedPdf.pdf" to create in the current folder (where the code is running)
        Or : "C://Path//To Output//mergedPdf.pdf"
    """
    merger = PdfMerger()
    for pdf in pdfs:
      merger.append(pdf)

    merger.write(mergedPDFName)
    merger.close()

def mergePDFsOutPut(pdfs : List[str], outPutPath : str, mergedPDFName : str):
   mergePDFs(pdfs, outPutPath + mergedPDFName)

# merge.append("one.pdf", pages=(0, 4, 2)) # means we consider the pages in the range from 0 to 4 with a step of 2.
def mergePDFsWithPageSelection(pdfs : List[str], pages : List[tuple], outPutPath : str, mergedPDFName : str) -> None:
   """ Merge PDFs and allow the possibility to select only certain pages by specifying a range (start, end, step). You choose the folder where the merged file will be output as well as the name of the file.

    Parameters
    -------------
    pdfs
        Represents the filenames of the PDFs we want to merge.
        Can be in one of the following format :
        r"C:\Path\To The File\File.pdf"
        "C://Path//To The File//File.pdf"
    pages
        Contain list of tuples of the form (start_page, end_page, step) to select the pages for each PDF listed in pdfs.
        Example : [(0, 10, 2), (0, 5, 1)] # select one page on two from 0 to 10 for the first pdf and from 0 to 5 for the second pdf.
    mergedPDFName
        The name of the output file.
        In the form : "mergedPdf.pdf" to create in the current folder
   """
   merger = PdfMerger()
   for p in range(len(pdfs)):
      merger.append(pdfs[p], pages=pages[p])
   
   merger.writer(outPutPath + mergedPDFName)
   merger.close()