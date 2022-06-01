
performances_metrics_measured = ["accuracy_score", "f1_score", "recall_score", "precision_score"]

def check_metrics_value_range(performances_list):
    """ This function checks if the values inside de performances_list list are indeed: positive, not greater than 1, not Null and a float (ie. not a string).
    """
    return all(metric >= 0 and metric <=1 and metric != None and isinstance(metric, float) for metric in performances_list)
    
    
def check_metrics_list_returned(keys):
    """ This function checks if the of the keys list are in performances_metrics_measured.
    In other words: Checks if the keys of the json we got from the GET call to the API are indeed the ones expected in performances_metrics_measured:
    - accuracy_score
    - f1_score
    - recall_score
    - precision_score

    Returns True if each one of the keys are a part of performances_metrics_measured, and False if not
    """
    return all(metric in performances_metrics_measured for metric in keys)