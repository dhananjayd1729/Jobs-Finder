from bs4 import BeautifulSoup
import requests
import time

print('Tell us the skills you are unfamiliar with')
unfamiliar_skills=input('>')
print(f"filtering out:{unfamiliar_skills}")


def find_jobs () :
    html_text = requests.get (
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=' ).text
    soup = BeautifulSoup ( html_text , 'lxml' )
    jobs = soup.find ( 'li' , class_ = 'clearfix job-bx wht-shd-bx' )
    for index , job in enumerate ( jobs ) :
        published_date = jobs.find ( 'span' , class_ = 'sim-posted' ).span.text
        if 'few' in published_date :
            company_name = jobs.find ( 'h3' , class_ = 'joblist-comp-name' ).text.replace ( ' ' , '' )
            skills = jobs.find ( 'span' , class_ = 'srp-skills' ).text.replace ( ' ' , '' )
            more_info = jobs.header.h2.a [ 'href' ]
            if unfamiliar_skills not in skills :
                with open ( f'posts/{index}.txt' , 'w' ) as f :
                    f.write ( f"Company name: {company_name.strip ( )} \n" )
                    f.write ( f"Skills required: {skills.strip ( )} \n" )
                    f.write ( f"More info: {more_info} \n" )
                print ( f'File saved: {index}' )


if __name__ == '__main__' :
    while True :
         find_jobs()
         time_wait=10
         print(f'Waiting {time_wait} minutes...')
         time.sleep(time_wait*10)
