import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db
import cgi
from lxml import etree as ET

galleries = db.get_galleries()

root = ET.Element('galleries')
for gallery in galleries:
    gallery_element = ET.SubElement(root, 'gallery')
    gallery_name = ET.SubElement(gallery_element, 'name')
    gallery_name.text = gallery[1]
    gallery_city = ET.SubElement(gallery_element, 'city')
    gallery_city.text = str(gallery[2])
    gallery_country = ET.SubElement(gallery_element, 'country')
    gallery_country.text = str(gallery[3])


print(f'Content-Type: application/octet-stream; name="galleries.xml"\n')
ET.dump(root)