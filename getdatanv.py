import requests
x = requests.get("https://hocpython.org/data/")
html = x.text
first_place = html.find("<table>")
second_place = html.find("</table>")
html = html[first_place + 7: second_place]
html = html.replace("<tbody>", "")
html = html.replace("</tbody>", "")
html = html.replace("<tbody>", "")
html = html.replace("<td>", "")
html = html.replace("</td>", ",")
html = html.replace("<tr>","")
html = html.replace("</tr>", "\n")
html = html.replace(",\n","\n")
print(html)

f = open("Datanv.csv", "w", encoding = "utf8")
f.write(html)
f.close()



