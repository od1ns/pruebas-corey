import csv
import sys

def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

#def print_start():
#    html_out +="<table border='1'>"

#def print_end():
#    html_out +="</table>"

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields

#def print_line(line, color, maxwidth):


html_out = ''
names = []
maxwidth = 100
#print_start()
count = 0

with open('data\co2-sample.csv','r') as data_file:
    #csv_data = csv.reader(data_file)
    csv_data = (data_file)
    #next(csv_data)
    
    html_out += "<table border='1'>"
    for line in csv_data:
        #names.append(f"{line[0]} {line[1]} {line[2]} {line[3]} {line[4]} {line[5]}")
        if count == 0:
                color = "lightgreen"
        elif count % 2:
            color = "white"
        else:
            color = "lightyellow"
#        print_line(line, color, maxwidth)
       
        html_out += "<tr bgcolor='{0}'>".format(color)
        
        fields = extract_fields(line)
        for field in fields:
            if not field:
                html_out +="<td></td>"
            else:
                number = field.replace(",", "")
                try:
                    x = float(number)
                    html_out +="<td align='right'>{0:d}</td>".format(round(x))
                except ValueError:
                    field = field.title()
                    field = field.replace(" And ", " and ")
            
                    if len(field) <= maxwidth:
                        field = escape_html(field)
                    else:
                        field = "{0} ...".format(
                                escape_html(field[:maxwidth]))
                    html_out +="<td>{0}</td>".format(field)
        html_out +="</tr>"
        count += 1
#html_out += f"<p> Hay en el momento' {len(names)} nombres. Gracias! </p>"

#print_end()
#count = 0
#while True:
#    try:
#        line = csv_data()
#        if count == 0:
#                color = "lightgreen"
#        elif count % 2:
#            color = "white"
#        else:
#           color = "lightyellow"
#        print_line(line, color, maxwidth)
#        count += 1
#    except EOFError:
#        break

html_out += "</table>"

print(html_out)