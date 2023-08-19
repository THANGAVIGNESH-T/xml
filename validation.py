import xml.etree.ElementTree as ET
from lxml import etree

# Load the XML document and XML schema
xml_document = 'employees.xml'
xml_schema = 'employee_schema.xsd'

# Create an XML schema object
schema = etree.XMLSchema(file=xml_schema)

# Parse the XML document
try:
    xml_tree = ET.parse(xml_document)
    root = xml_tree.getroot()
    print("XML document loaded successfully.")
except ET.ParseError as e:
    print("Error parsing XML document:", e)
    exit(1)

# Validate the XML document against the schema
if schema.validate(xml_tree):
    print("XML document is valid.")
else:
    print("XML document is not valid. Validation errors:")
    for error in schema.error_log:
        print(f"Line {error.line}, Column {error.column}: {error.message}")