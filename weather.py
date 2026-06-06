import requests

API_KEY = "15be413192a0e87f3f7934b403c482c1"

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    print(url)

    response = requests.get(url)

    data = response.json()

    print(data)

    if data["cod"] == 200:

        print("\nWeather Report")
        print ("-" * 20)

        print("City:", data["name"])
        print("Country", data["sys"]["country"])
        print("Code", data["cod"])
        print("Longitude:", data["coord"]["lon"])
        print("Latitude", data["coord"]["lat"])
        print("Condition", data["weather"][0]["description"])
        print("Temperature", data["main"]["temp"], "°C")
        print("Feels like", data["main"]["feels_like"], "°C")
        print("Humidity", data["main"]["humidity"], "%")
        print("Pressure", data["main"]["pressure"], "hPa")
        print("Wind Speed", data["wind"]["speed"], "m /s")

    else:
        print("City not found!")

while True:
    city = input("Enter city name (or exit): ")

    if city.lower() == "exit":
            break

    get_weather(city)