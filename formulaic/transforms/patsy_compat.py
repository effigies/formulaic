from formulaic.utils.stateful_transforms import stateful_transform


@stateful_transform
def Q(variable, _context=None):
    return _context[variable]
