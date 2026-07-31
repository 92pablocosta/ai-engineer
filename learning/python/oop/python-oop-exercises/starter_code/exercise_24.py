class BrokenStorage:
    pass


def save_document(storage, text):
    return storage.save(text)


# TODO: catch the error caused by this missing duck-typed method.
