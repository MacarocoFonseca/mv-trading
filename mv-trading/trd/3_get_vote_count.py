import requests

def getVoteCount(cityName, estimatedCost):
    api_url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost={estimatedCost}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return -1

    json_data = response.json()
    data = json_data.get('data', [])

    if not data:
        return -1

    total_votes = 0
    for outlet in data:
        user_rating = outlet.get('user_rating', {})
        votes = user_rating.get('votes', 0)
        total_votes += votes

    return total_votes

# Sample Case 0
cityName = "Seattle"
estimatedCost = 110
print(getVoteCount(cityName, estimatedCost))  # Output: 2116

# Sample Case 1
cityName = "Delaware"
estimatedCost = 150
print(getVoteCount(cityName, estimatedCost))  # Output: -1
