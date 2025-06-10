from pytrends.request import TrendReq
import pandas as pd

#google a bağlan
pytrends=TrendReq(hl='tr-TR- tz=360')
#araştırılcak kelime
resorch_word=['hisse','altın','dollar','faiz']
country=['TR','USA' ]
for  cou in country:

  """ trend verisini al   ve hangi zaman , aralık, ülke de,  arama yapmak istediğini belirtirsin   / cat=0, kategori ıd si"""
  pytrends.build_payload(resorch_word, cat=0, timeframe='today 12-m', geo=cou)
  # zaman serisi verisini al (ilgi düzeyi zaman içerisinde)
  data=pytrends.interest_over_time()
  print(data.head())
  
  aa=pd.DataFrame(data)

aa.to_excel("trends.xlsx", index=True)