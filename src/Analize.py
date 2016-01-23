from alchemyapi import AlchemyAPI

alchemyapi = AlchemyAPI()


def get_key_sentences(review):
    pass


def get_entities(review):
    entities = alchemyapi.keywords("text", review, {"sentiment": 1})

    result = []
    for entity in entities["keywords"]:
        print entity
        if "score" not in entity["sentiment"]:
            continue
        weighted_score = float(entity["relevance"]) * float(entity["sentiment"]["score"])
        result.append((entity["text"], float(entity["sentiment"]["score"]), weighted_score))
    result = sorted(result, key=lambda data: abs(data[2]), reverse=True)
    return result


def get_sentiment(review):
    sentiment = alchemyapi.sentiment("text", review)
    print(sentiment)
    return float(sentiment["docSentiment"]["score"])


def handle_review(text, restaurant):
    entities = get_entities(text)
    sentiment = get_sentiment(text)
    #record(entities, sentiment,entities)




