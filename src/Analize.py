from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()


def get_key_sentences(review):
    pass


def get_keywords(review):
    response = alchemyapi.sentiment("text", review, {"sentiment": 1})
    print(response["entities"])