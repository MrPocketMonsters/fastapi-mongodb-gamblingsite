def individual_serial(document:dict, model) -> dict:
    result = {"id": str(document["_id"])}
    for key in model.__fields__.keys():
        result[key] = document[key]

    return result

def list_serial(documents, model) -> list:
    return [individual_serial(document, model) for document in documents]
