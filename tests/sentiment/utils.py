
def check_sentiment_in_response_are_int(responses):
    """ This function checks if the values (sentiment calculated by the ML algorithm) inside the response are indeed an int like expected.
    Input: List of dictionnaries
        ex: [{'Sentence': 'The app is bad', 'sentiment': 0}, {'Sentence': 'I like it very much', 'sentiment': 1}]
    Returns: True if the sentiment in the response are all ints and False if not.
    """
    responses = [r.json() for r in responses]
    return all(isinstance(responses[i]["sentiment"], int) for i in range(0, len(responses)))
    

def check_sentiment_in_response_are_within_range(responses):
    """ This function checks if the values (sentiment calculated by the ML algorithm) inside the response are either 0 or 1 like expected.
        Input: List of dictionnaries
        ex: [{'Sentence': 'The app is bad', 'sentiment': 0}, {'Sentence': 'I like it very much', 'sentiment': 1}]
    Returns: True if the sentiment in the response is either 0 or 1.
    """
    responses = [r.json() for r in responses]
    return all(responses[i]["sentiment"] >= 0 and responses[i]["sentiment"] <= 1 for i in range(0, len(responses)))


def check_status_code_is_200_in_list_of_responses(responses):
    """ This function checks if the list of requests all ends up with a status_code of 200
        Input: List of reponses (requests.get(xxx))
        ex:[{'Sentence': 'The app is bad', 'sentiment': 0}, {'Sentence': 'I like it very much', 'sentiment': 1}]
    Returns: True if the request went through successfully.
    """
    return all(r.status_code == 200 for r in responses)
