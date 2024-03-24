def lemmatize(doc):
    import re
    from pymorphy2 import MorphAnalyzer
    patterns = "[0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+"
    morph = MorphAnalyzer()
    doc = re.sub(patterns, ' ', doc)
    doc = doc.strip()
    doc = morph.normal_forms(doc)[0]
    return doc