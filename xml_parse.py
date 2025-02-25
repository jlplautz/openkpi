import xml.etree.ElementTree as ET

tree = ET.parse('20FEV22H00V1.xml')
root = tree.getroot()
print(root.tag)
# print(root[0].tag)
# print(root[0].text)
# for child in root:
#     print(child.tag, child.attrib)

for movie in root.findall("./OMeS/PMSetup/PMMOResult/NE-WBTS_1.0/[measurementType='SBTS_Energy_Consumption']"):
    print(movie.attrib)


# print(root.attrib)

# for elem in tree.iter():
#     print(elem.tag, elem.text)


# for PMSetup in root.iter('PMSetup'):
#     print(PMSetup.attrib)

# for MO in root.iter('MO'):
#     print(MO.attrib)


for NEWBTS in root.iter('NE-WBTS_1.0'):
    print(NEWBTS.attrib)

# for ltetload in root.findall('PMMOResult'):
#     print(ltetload.text)


# import xml.etree.ElementTree as ET

# root = ET.fromstring(countrydata)

# # Top-level elements
# root.findall(".")

# # All 'neighbor' grand-children of 'country' children of the top-level
# # elements
# root.findall("./country/neighbor")

# # Nodes with name='Singapore' that have a 'year' child
# root.findall(".//year/..[@name='Singapore']")

# # 'year' nodes that are children of nodes with name='Singapore'
# root.findall(".//*[@name='Singapore']/year")

# # All 'neighbor' nodes that are the second child of their parent
# root.findall(".//neighbor[2]")

