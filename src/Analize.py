from alchemyapi import AlchemyAPI
from crud import put

alchemyapi = AlchemyAPI()


def get_key_sentences(review):
    pass


def get_entities(review):
    entities = alchemyapi.entities("text", review, {"sentiment": 1})
    result = []
    for entity in entities["entities"]:
        if "score" not in entity["sentiment"]:
            continue
        weighted_score = float(entity["relevance"]) * float(entity["sentiment"]["score"])
        result.append({"text": entity["text"], "score": float(entity["sentiment"]["score"]), "weighted_score": weighted_score})
    result = sorted(result, key=lambda data: abs(data["weighted_score"]), reverse=True)
    return result


def get_keywords(review):
    entities = alchemyapi.keywords("text", review, {"sentiment": 1})
    result = []
    for entity in entities["keywords"]:
        if "score" not in entity["sentiment"]:
            continue
        weighted_score = float(entity["relevance"]) * float(entity["sentiment"]["score"])
        result.append({"text": entity["text"], "score": float(entity["sentiment"]["score"]), "weighted_score": weighted_score})
    result = sorted(result, key=lambda data: abs(data["weighted_score"]), reverse=True)
    return result


def get_sentiment(review):
    sentiment = alchemyapi.sentiment("text", review)
    print(sentiment)
    return float(sentiment["docSentiment"]["score"])


def handle_review(selector, text, restaurant):
    keywords = get_keywords(text)
    sentiment = get_sentiment(text)
    put(selector, {"audioName": restaurant, "avgSentiment": sentiment, "reviewTags": keywords, "reviewText": text})
