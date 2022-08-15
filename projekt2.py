import requests
import json
import http.client, urllib.parse
from bs4 import BeautifulSoup


while True:
    
    class __init__():


        def printingResultsMetric(weather):
            star = json.loads(weather)
            star2 = (star["weather"])

            print("Pogoda: ")
            star2 = (star2[0]["description"])
            print(star2)
            star3 = (star["main"])

            print("Temperatura: ")
            star4 = (star3["temp"])

            print(star4, " C")
            print("Temperatura odczuwalna: ")
            star5 = (star3["feels_like"])
            print(star5, " C")
            print("ciśnienie")
            star6 = (star3["pressure"])
            print(star6, " hPa")
            print("Wilgotność")
            star7 = (star3["humidity"])
            print(star7, " %")

            return star2, star4, star5, star6, star7
        

        def apiWeatherResponse(query):

            response = requests.get(query)
            soup = BeautifulSoup(response.text, "lxml")
            soup = soup.text
            return soup

        def apiWeatherQuery(lat, lon, apiKey, respFormat = "", units = "", language="pl"):
#response Format is default for JSON, units for standard units.        


            lat = str(lat)
            lon = str(lon)
            queryPart1 = "https://api.openweathermap.org/data/2.5/weather?lat="
            queryPart2 = "&lon="
            queryPart3 = "&appid="
            queryPart4 = "&lang="

            queryApi = queryPart1 + lat + queryPart2 + lon + queryPart3 + apiKey + queryPart4 + language

            if respFormat != "":
                queryPart5 = "&mode="+mode
            
                queryApi = queryApi + queryPart5

            if units != "":
                queryPart6 = "&units="+units
            
                queryApi = queryApi + queryPart6

            return queryApi


        def latlot(place, apiKey):

            conn = http.client.HTTPConnection("api.positionstack.com")

            params = urllib.parse.urlencode({
                "access_key": apiKey,
                "query": place,
                "fields" : "results.label, results.latitude, results.longitude",
                "limit": 1,
                })

            conn.request('GET', '/v1/forward?{}'.format(params))

            res = conn.getresponse()
            data = res.read()
            jsonie = json.loads(data)
            jsonie2 = (jsonie["data"])
            jsonie3 = (jsonie2[0])
            label = (jsonie3["label"])
            lat = (jsonie3["latitude"])
            lon = (jsonie3["longitude"]) 

            return label, lat, lon
        
        psKey = "818aa02ef548e26636f6e682c592df69"
        
        placeOfStart = input("Wskaż skąd startujesz? ")

        placeOfMeta =  input("Wskaż kierunek ")

        apiWeatherKey = "1245f345f7e9aa3d88ec2f6b23fff7a9"
    
        st = latlot(placeOfStart, psKey)
        stLabel = st[0]
        stLat = st[1]
        stLon = st[2]
        
        mt = latlot(placeOfMeta, psKey)

        mtLabel = mt[0]
        mtLat = mt[1]
        mtLon = mt[2]
        
        print("Pogodę miejsca startu wyznaczono dla : ", stLabel)
        print("Pogodę miejsca mety wyznaczono dla : ", mtLabel)
        print("\n")

        apiSt = apiWeatherQuery(stLat, stLon, apiWeatherKey, respFormat = "", units = "metric")
        apiMt = apiWeatherQuery(mtLat,mtLon, apiWeatherKey, respFormat = "", units = "metric")

        weatherStart = apiWeatherResponse(apiSt)
        weatherMeta = apiWeatherResponse(apiMt)
 
        print(stLabel)
        wsVariables = printingResultsMetric(weatherStart)

        print("\n")
        
        print(mtLabel)
        wmVariables = printingResultsMetric(weatherMeta)

        print("Uzyskano zmienne: ", wsVariables, wmVariables)        


        with open('weatherStart.txt', 'w') as json_file:
          json.dump(weatherStart, json_file)
          

        with open('weatherMeta.txt', 'w') as json_file:
          json.dump(weatherMeta, json_file)


        print("Utworzono weatherStart.txt i weatherMeta.txt")
