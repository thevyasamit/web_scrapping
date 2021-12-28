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







# # string  = "nnas/ajs?adkkkada#adkjda"
# # st1 = string.split("/")
# # st2 = string.split("?")
# # st3 = string.split("#")
# # print(st1,'\n',st2,'\n',st3)




# -------------------- Ramp Capital Internship Decoder -----------------------

# import codecs
# import string
# import sys
# import time

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.hashes import SHA1
# from cryptography.hazmat.primitives.twofactor.totp import TOTP


# ONE_WEEK_IN_SECONDS = 604_800


# def generate_secret():
#     totp = TOTP(
#         key=codecs.encode(string.ascii_letters, encoding="utf-8"),
#         length=8,
#         algorithm=SHA1(),
#         time_step=ONE_WEEK_IN_SECONDS,
#         backend=default_backend(),
#     )
#     seed = int(time.time())
#     token = codecs.decode(totp.generate(seed), encoding="utf-8")
#     return f"{token}-{seed}"


# if __name__ == "__main__":
#     sys.stdout.write(
#         f"Please head to https://ramp.com/careers and use this secret when "
#         f"you apply: {generate_secret()}\n"
#     )