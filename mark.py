# Created by Selva
# Made with ❤ in Selvasoft

from bs4 import BeautifulSoup
import requests

csv_file = open("selvasoft.csv","w")
reg_start = 952817104001 #Enter starting number
reg_end = 952817104060 #Ending number
url = "http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl?regno="

def write_csv(list1):
    for word in list1:
        csv_file.write(word+",")
    csv_file.write("\n")

write_csv(['Name','Phy Lab','Chemistry','Python','EG','Py Lab','English','Maths','Physics'])

for i in range(reg_start,reg_end+1):
    data_list = []
    soup = requests.get(url+str(i))
    selva = BeautifulSoup(soup.text,"html.parser")
    td = selva.find_all("td")

    tables = td[1].find_all("table")
    strongs = tables[0].find_all("strong")
    table_2 = tables[1].find_all("strong")
    #print(table_2)
    no = 4
    name = strongs[1].string
    data_list.append(name)
    print("Completed for "+name)
    while no < len(table_2):
        print(table_2[no].string)
        data_list.append(table_2[no].string)
        no = no + 3
    write_csv(data_list)
csv_file.close()
