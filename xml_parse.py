import xml.etree.ElementTree as ET

tree = ET.parse('20FEV22H00V1.xml')
root = tree.getroot()
print(root.tag)
print(root[0].tag)
# print(root[0].text)

print(root.attrib)


for elem in tree.iter():
    print(elem.tag, elem.text)


# for PMSetup in root.iter('PMSetup'):
#     print(PMSetup.attrib)

# for MO in root.iter('MO'):
#     print(MO.attrib)


# for NEWBTS in root.iter('NE-WBTS_1.0'):
#     print(NEWBTS.attrib)

# for ltetload in root.findall('PMMOResult'):
#     print(ltetload.text)