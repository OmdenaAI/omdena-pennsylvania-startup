
from requests_html import HTMLSession
import time
import csv
import os
import pandas as pd


def scrapper():
    company_details = []
    counter=0
    urls = [f"https://startuptracker.io/discover?filters%5B0%5D%5Bcc%5D%5Bq%5D=US&page={number}" for number in range(16)]
    for url in urls:
        session = HTMLSession()
        r = session.get(url)
        startups = r.html.xpath('//*[@class="_8vwxjw"]//a/@href')
        startups = [f"https://startuptracker.io{start}" for start in startups]
        time.sleep(10)
        session.close()
        
        for startup in startups:
            details={}
            try:
                session = HTMLSession()
                r = session.get(startup)
                r.html.render(500)
                description = r.html.xpath('//*[@class="_qgzmqh"]/text()')
                description = str(description)
                details['description'] = description[1:-1]
                website = r.html.xpath('//*[@class="_e4x16a"]/a/@href')
                details['website']  = website[0]
                details['crunchbase_link'] = website[1]
                name = r.html.xpath('//*[@class="_1vj0t0j"]/text()')
                name = str(name)
                details['name'] = name[1:-1]
                print(name)
                activity = r.html.xpath('//*[@class="_1vmw3q2"]/text()')
                details['activity_level'] = activity[-3]
                #activity_verified = str(activity[-1])
                first = r.html.xpath('//*[@class="_mm5zvh"]/text()')
                second =  r.html.xpath('//*[@class="_1jivuxq"]/text()')
                market = r.html.xpath('//*[@class="_16gr0n0l"]/text()')
                market = str(market)
                details['market'] = market[1:-1]
                products = r.html.xpath('//*[@class="_c4ithgh"]/text()')
                products = str(products)
                details['products'] = products[1:-1]
                revenue_through =  r.html.xpath('//*[@class="_11tz2hsj"]/text()')
                revenue_through = str(revenue_through)
                details['revenue_through'] = revenue_through[1:-1]            
                founded_by = r.html.xpath('//*[@class="_1gebkr1"]/text()')
                founded_by = str(founded_by)
                details['founded_by'] = founded_by[1:-1]
                details['founded']  = str(f"{second[0]} {first[0]}")
                details['place'] =  f"{second[1]} {first[1]}"
                details['team_members'] = str(first[2])
                details['launch_stage'] = first[3]
                details['revenue_stage'] = first[4]
                details['amount_raised'] = first[5]
                details['twitter_followers'] = first[6]
                details['percentile'] = first[-1]
                if len(second[-2]) > 5:
                    details['pageviews'] = first[-2]
                else:
                    details['pageviews'] = 0 
                if second[-3] == 'global rank':
                    details['ranking'] = first[-3]
                else:
                    details['ranking'] = 0

                print(details)
                company_details.append(details)
                session.close()
                print(counter, "count")
                counter+=1
                time.sleep(30)
            except:
                pass 
    return company_details    



if __name__ == "__main__":
    print('started working')
    data= scrapper()
    df = pd.DataFrame.from_dict(data)
    df.to_csv('startup_tracker_io.csv', index=False)

