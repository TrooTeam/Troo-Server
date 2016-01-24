import requests

lusi_url = "https://api.projectoxford.ai/luis/v1/application?id=48dd6691-4c38-485d-a82d-29d5ae92c60d&subscription-key=dd62b8675738406ebaacbe7546cb36cb&q="


def get_search_term(query):
    result = requests.get(lusi_url + query).json()

    if len(result["entities"]) > 0:
        return result["entities"]["entity"]
    else:
        return "Restaurants"
