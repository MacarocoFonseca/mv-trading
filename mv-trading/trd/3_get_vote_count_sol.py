import requests

def getVoteCount(cityName, estimatedCost):
    total_votes = 0
    page = 1

    while True:
        api_url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost={estimatedCost}&page={page}"
        response = requests.get(api_url)

        if response.status_code != 200:
            return -1

        json_data = response.json()
        data = json_data.get('data', [])
        total_pages = json_data.get('total_pages', 1)
        # or
        # data = json_data['data']
        # total_pages = json_data['total_pages']

        if not data:
            return -1

        for outlet in data:
            user_rating = outlet.get('user_rating', {})
            votes = user_rating.get('votes', 0)
             # or
            # user_rating = outlet['user_rating']
            # votes = user_rating['votes']
            total_votes += votes

        if page >= total_pages:
            break

        page += 1

    return total_votes if total_votes > 0 else -1

# Sample Case 0
cityName = "Seattle"
estimatedCost = 110
print(getVoteCount(cityName, estimatedCost))  # Output: 2116

# Sample Case 1
cityName = "Delaware"
estimatedCost = 150
print(getVoteCount(cityName, estimatedCost))  # Output: -1
