from pdf2image import convert_from_path
from trp import Document
import tables
import csv
import csvExtraction
import sys
import insert

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

    
mappings = {
    ('january' , 'jan') : '01',
    ('february', 'feb') : '02',
    ('march', 'mar') : '03',
    ('april', 'apr') : '04',
    ('may', 'may') : '05',
    ('june', 'jun') : '06',
    ('july', 'jul') : '07',
    ('august', 'aug') : '08',
    ('september', 'sep') : '09',
    ('october','oct') : '10',
    ('november','nov') : '11',
    ('december','dec') : '12'
}


def main(filePath , filename):
    print("this happened")
    outputCSV = []
    images = convert_from_path(filePath)

    dates = {}

    for page, image in enumerate(images):
        imagePath = "pdf_image/image_" + str(page) + ".jpeg" 
        image.save(imagePath)
        csv = tables.main(imagePath , page)
        outputCSV.append(csv)
        output = (csvExtraction.getDates("output" + str(page)))
        if len(output) != 0:
            dates.update(output)

    
    for item,date in dates.items():
        words = date.split()
        month = words[0]
        day = words[1]
        monthnum = -1

        for idx, months in enumerate(mappings):
            if month.lower() in months:
                monthnum = idx + 1
                break
        
        insert.main(filename + str("-")+item, day,monthnum)

    return dates


if __name__ == "__main__":
    file_path = sys.argv[1]
    file_name = sys.argv[2]
    main(file_path, file_name)






