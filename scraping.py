from bs4 import BeautifulSoup
import requests


source = requests.get('https://engineering.csuohio.edu/eecs/computer-science-faculty').text
soup = BeautifulSoup(source,'lxml')
i = 0
for tr in soup.find_all('tr'):
#tr = soup.find('tr')
    i+=1
    if(i == 4 or i == 13 ): #these 2 people have formatting issues so need to do manually or figure out later
        pass
    else:
        facultyName = tr.td.a.text.split(",")[0]
        print("Name is : ", facultyName)

        designation = tr.p.text.split(" ")[2].split("\n")[1]+ " "+tr.p.text.split(" ")[3].split("\n")[0]
        designation = designation.split("\t")[5]
        print("Position is: ", designation)

        officeLocation = tr.td.text.split("\n")[4].split(":")[1]
        print("Office is: ", officeLocation)

        facultyEmail = tr.td.text.split("\n")[5].split(":")[1]
        print("Email is: ", facultyEmail)
        #print(tr.prettify())
        print("-----------------------------")
