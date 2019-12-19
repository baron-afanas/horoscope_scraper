from scraper import SimpleScraper
from multiprocessing import Pool
import datetime, json

signs = [
    'aries','taurus','gemini','cancer',
    'leo','virgo','libra','scorpio',
    'sagittarius','capricorn','aquarius','pisces'
]
years = [12,13,14,15,16,17,18,19]

def f(data):
    scraper = SimpleScraper()
    request = scraper.get_url('https://www.beliefnet.com/inspiration/astrology/{}.aspx?d={}'.format(data['sign'],data['date']))
    if 'error' not in request:
        res = scraper.get_elements_by_class('col-sm-9')
        text = res[0].get_text() if len(res) > 0 else 'no data' 
        response = {"sign":data['sign'],"date":data['date'],"text":text}
        return response
    else:
        response = {"sign":data['sign'],"date":data['date'],"text":"ERROR-->"+str(request)}
        return response

def main():
    total = []
    for year in years:
        extraction_list = []
        start_date = datetime.date(2000+year,1,1)
        end_date = datetime.date(2000+year,12,31)
        diff = end_date - start_date
        for sign in signs:
            for i in range(diff.days + 1):
                day = start_date + datetime.timedelta(days=i)
                extraction_list.append({"sign":sign,"date":day.strftime("%Y%m%d")})
    
        with Pool(5) as p:
            pool = p.map(f, extraction_list)
        
        for entry in pool:
            txt = entry['text']
            index = txt.index("\r\n")
            txt = txt[index+4:]
            txt = txt.lstrip()
            index = txt.index("\r\n")
            txt = txt[:index]
            entry['text'] = txt

            date = entry['date']
            entry['date'] = date[:4]+'-'+date[4:6]+'-'+date[6:8]
        
        total.extend(pool)

    with open('datoss.json', 'w') as outfile:
        json.dump(total, outfile)

if __name__== "__main__":
  main()
            
