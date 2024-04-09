import requests

API_KEY = "56e5235f39923eadf0c58f4e21aca108"


def get_data(place, forecast_days=None):  # pass forecast_days argument is not mandatory
    # do not forget http://
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_values = 8 * forecast_days  # each day has 8 elements in filtered_data
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
