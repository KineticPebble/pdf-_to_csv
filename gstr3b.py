from pypdf import PdfReader
import csv
import os

foldername = 'GST'
ls = os.listdir(foldername)
filename = ls[0]

reader = PdfReader(foldername+'/'+filename)
page_count = len(reader.pages)

pages_text = []
for i in range(page_count):
    page = reader.pages[i]
    a = page.extract_text()
    b = a.split('\n')
    pages_text += b

gst31_header = ['Nature of Supplies', 'Total taxable value', 'Integrated tax', 'Central tax', 'State/UT tax', 'Cess']

def text_to_list(ls, c):
    return [' '.join(ls.split(' ')[:c])] + ls.split(' ')[c:]

gst31 = [
    ['3.1 Details of Outward supplies and inward supplies liable to reverse charge (other than those covered by Table 3.1.1)'],
gst31_header,
[pages_text[20] + pages_text[21]] + pages_text[22].split(' '),
text_to_list(pages_text[23], -5),
text_to_list(pages_text[24], -5),
text_to_list(pages_text[25], -5),
text_to_list(pages_text[26], -5),
['']
 ]

gst311 = [
['3.1.1 Details of Supplies notified under section 9(5) of the CGST Act, 2017 and corresponding provisions in IGST/UTGST/SGST Acts'],
gst31_header,
[pages_text[39]+ pages_text[40]] + pages_text[41].split(' '),
[pages_text[42]+ pages_text[43]+ pages_text[44]+ pages_text[45]] + pages_text[46].split(' '),
['']
]

gst32 = [
[pages_text[47]],
['Nature of Supplies', 'Total taxable value', 'Integrated tax'],
text_to_list(pages_text[49], -2),
[pages_text[50] + pages_text[51]] + pages_text[52].split(' '),
text_to_list(pages_text[53], -2),
['']
]

gst4 = [
[pages_text[54]],
['Details', 'Integrated tax', 'Central tax', 'State/UT tax', 'Cess'],
[pages_text[56]],
text_to_list(pages_text[57], -4),
text_to_list(pages_text[58], -4),
text_to_list(pages_text[59], -4),
text_to_list(pages_text[61], -4),
text_to_list(pages_text[62], -4),
[pages_text[63]],
text_to_list(pages_text[64], -4),
text_to_list(pages_text[65], -4),
text_to_list(pages_text[66], -4),
text_to_list(pages_text[67], -4),
[pages_text[68] + pages_text[69]] + pages_text[52].split(' '),
text_to_list(pages_text[71], -4),
['']
]

gst5 = [
[pages_text[72]],
['Nature of Supplies', 'Inter- State supplies', 'Intra- State supplies'],
text_to_list(pages_text[74], -2),
text_to_list(pages_text[75], -2),
['']
]

gst51 = [
[pages_text[76]],
['Details', 'Integrated tax', 'Central tax', 'State/UT tax', 'Cess'],
[pages_text[78] + pages_text[79]] + pages_text[80].split(' '),
text_to_list(pages_text[81], -4),
text_to_list(pages_text[82], -4),
['']
]

gst61 = [
[pages_text[83]],
['Description', 'Total tax Payable', '(ITC) Integrated tax', '(ITC) Integrated tax', '(ITC) Central tax', '(ITC) State/UT tax', '(ITC) Cess', 'Tax paid in cash',
 'Interest paid in cash', 'Late fee paid in cash'],
[pages_text[92]],
[pages_text[93] + pages_text[94]] + pages_text[95].split(' '),
text_to_list(pages_text[96], -8),
text_to_list(pages_text[97], -8),
text_to_list(pages_text[98], -8),
[pages_text[99]],
[pages_text[100] + pages_text[101]] + pages_text[102].split(' '),
text_to_list(pages_text[103], -8),
text_to_list(pages_text[104], -8),
text_to_list(pages_text[105], -8),
['']
]

gst_liability =[
[pages_text[106]],
['Period', 'Integrated tax', 'Central tax', 'State/UT tax', 'Cess'],
text_to_list(pages_text[108], -4),
['']
]


fh = open('gst3b.csv', 'w', newline='')
csvwriter = csv.writer(fh)
csvwriter.writerows(gst31)
csvwriter.writerows(gst311)
csvwriter.writerows(gst32)
csvwriter.writerows(gst4)
csvwriter.writerows(gst5)
csvwriter.writerows(gst51)
csvwriter.writerows(gst61)
csvwriter.writerows(gst_liability)
fh.flush()
fh.close()
