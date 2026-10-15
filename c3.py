import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def getRandomTechnologyFact():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"Did you know? {data["text"]}")

    else:
        print("Error 404 URL is Invalid")


while True:
    user_input = input("Press Enter to get a random technology fast or type Q to quit: ")

    if user_input.lower() == "q":
        break
    else:
        getRandomTechnologyFact()
