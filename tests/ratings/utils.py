
def check_ratings_in_response_are_int(responses):
    """ This function checks if the values (ratings calculated by the ML algorithm) inside the response are indeed an int like expected.
    Input: List of dictionnaries
        ex: [{'Sentence': 'The app is bad', 'Ratings': 1}, {'Sentence': "I guess it's fine", 'Ratings': 4}, {'Sentence': 'Meh', 'Ratings': 3}, {'Sentence': 'Dope', 'Ratings': 5}, {'Sentence': 'I like it very much', 'Ratings': 5}]
    Returns: True if the ratings in the response are all ints and False if not.
    """
    responses = [r.json() for r in responses]
    return all(isinstance(responses[i]["Ratings"], int) for i in range(0, len(responses)))
    

def check_ratings_in_response_are_within_range(responses):
    """ This function checks if the values (ratings calculated by the ML algorithm) inside the response are within the 0, 5 range like expected.
        Input: List of dictionnaries
        ex: [{'Sentence': 'The app is bad', 'Ratings': 1}, {'Sentence': "I guess it's fine", 'Ratings': 4}, {'Sentence': 'Meh', 'Ratings': 3}, {'Sentence': 'Dope', 'Ratings': 5}, {'Sentence': 'I like it very much', 'Ratings': 5}]
    Returns: True if the ratings in the response are higher than 0 and lower than 5 and False if not.
    """
    responses = [r.json() for r in responses]
    return all(responses[i]["Ratings"] >= 0 and responses[i]["Ratings"] <= 5 for i in range(0, len(responses)))


def check_status_code_is_200_in_list_of_responses(responses):
    """ This function checks if the list of requests all ends up with a status_code of 200
        Input: List of reponses (requests.get(xxx))
        ex: [{'Sentence': 'The app is bad', 'Ratings': 1}, {'Sentence': "I guess it's fine", 'Ratings': 4}, {'Sentence': 'Meh', 'Ratings': 3}, {'Sentence': 'Dope', 'Ratings': 5}, {'Sentence': 'I like it very much', 'Ratings': 5}]
    Returns: True if the ratings in the response are higher than 0 and lower than 5 and False if not.
    """
    return all(r.status_code == 200 for r in responses)



# def check_metrics_list_returned(keys):
#     """ This function checks if the of the keys list are in performances_metrics_measured.
#     In other words: Checks if the keys of the json we got from the GET call to the API are indeed the ones expected in performances_metrics_measured:
#     - accuracy_score
#     - f1_score
#     - recall_score
#     - precision_score

#     Returns True if each one of the keys are a part of performances_metrics_measured, and False if not
#     """
#     return all(metric in performances_metrics_measured for metric in keys)