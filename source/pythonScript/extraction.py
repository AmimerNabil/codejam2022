from pdf2image import convert_from_path
from trp import Document
import tables
import csv
import csvExtraction
import sys

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def main(filePath):
    print("this happened")
    outputCSV = []
    images = convert_from_path(filePath)

    dates = {}

    for page, image in enumerate(images):
        imagePath = "pythonScript/pdf_image/image_" + str(page) + ".png" 
        image.save(imagePath)
        csv = tables.main(imagePath , page)
        outputCSV.append(csv)
        output = (csvExtraction.getDates("output" + str(page)))
        if len(output) != 0:
            dates.update(output)

    return dates


if __name__ == "__main__":
    file_name = sys.argv[1]
    print(main(file_name))






