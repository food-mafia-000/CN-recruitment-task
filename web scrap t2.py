from bs4 import BeautifulSoup
import requests
from csv import writer


url=str(input("Enter the URL of the Product : "))
page=requests.get(url)
#print(page)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup)
reviewlist=soup.findAll('div',class_="col _2wzgFH K0kLPL")
#print (reviewlist)


with open('review.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['User', 'Rating','Location','Heding','Status','Text']
    thewriter.writerow(header)
    for rew in reviewlist:
        heading=rew.find('p',class_="_2-N8zT").text

        rateing=rew.find('div',class_="_3LWZlK _1BLPMq").text
        text=rew.find('div',class_="t-ZTKy").text
        user=rew.find('p',class_="_2sc7ZR _2V5EHH").text
        #    rew.replace("_2sc7ZR _2V5EHH"," aaa")
        #    date=rew.find('p',class_="_2sc7ZR").text
        #    print(date)
        stat=rew.find('p',class_="_2mcZGG").text
        st=stat.split(", ")
        sta=st[0]
        location=st[-1]
        #    all=rew.find('div',class_='row').text
        #    print(all)
        #    print(user,"\n",rateing,"\n",location,"\n",text,"\n",sta)
        data = [user,rateing, location, heading, sta,text]
        thewriter.writerow(data)
print("The data has been stored in a csv file !")
print("Thank you for using our service")