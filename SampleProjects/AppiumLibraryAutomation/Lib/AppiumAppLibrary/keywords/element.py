from AppiumLibrary.keywords import _ElementKeywords
from AppiumLibrary.keywords.keywordgroup import KeywordGroup

__version__ = '1.0.1'


class ElementManagementKeywords(KeywordGroup):

    def __init__(self):
        self.element_management = _ElementKeywords()
