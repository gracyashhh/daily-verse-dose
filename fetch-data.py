import requests
from bs4 import BeautifulSoup
import csv

URL = "https://holyword.church/miscellaneous-resources/how-many-words-in-each-book-of-the-bible/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="tablepress-1")
job_elements = results.find("tbody", class_="row-hover")
reference={
    1:"SI",
    2:"BOOK",
    3:"CHAPTERS",
    4:"VERSES",
    5:"WORDS",
    6:"AUTHOR",
    7:"GENRE",
    8:"OT/NT",
}
bible_backup={}
si=1
for j in range(2,68):
    rows=job_elements.find("tr",class_=f"row-{j}")
    bible_backup[si] = {}
    for i in range(1,9):
        content=rows.find("td",class_= f"column-{i}")
        # print(i,content.text)
        bible_backup[si][reference[i]]=content.text
    si+=1
my_file = open("bible.csv", "w",newline='')
writer = csv.writer(my_file)
for key, value in bible_backup.items():
    writer.writerow([key,value])
my_file.close()