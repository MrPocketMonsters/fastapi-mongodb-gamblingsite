def individual_serial(document:dict, model) -> dict:
    '''Returns a dictionary with the "id" key and all fields in the provided model.'''
    result = {"id": str(document["_id"])}
    for key in model.__fields__.keys():
        result[key] = document[key]

    return result

def list_serial(documents, model) -> list[dict]:
    '''Returns a list with the individual_serial(document, model) for each document in Cursor documents.'''
    return [individual_serial(document, model) for document in documents]
