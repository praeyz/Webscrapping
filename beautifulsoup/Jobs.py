import requests
from bs4 import BeautifulSoup

#Make a Url link for the request method
url = "https://pythonjobs.github.io/"

#User-Agent
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"}

#Make a get request to the Url 
response = requests.get(url, headers = headers)
webpage = response.content

print(f"your status code is :{response.status_code}")

#Make a beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#Logic to extract relevant imformation including - Title, Location, company and description
for jobs in soup.find_all('section', class_ = 'job_list'):
    title = [i for i in jobs.find_all('h1')]

    for n, tags in enumerate(jobs.find_all('div', class_ = 'job')):
        company_info = [i for i in tags.find_all('span', class_ = 'info')]
        for description in tags.find_all('p', class_= 'detail'):
            print(f"Title : {title[n].text.strip()}")
            print(f"Location : {company_info[0].text.strip()}")
            print(f"Company : {company_info[3].text.strip()}")
            print(f"description : {description.text.strip()}")




 

    