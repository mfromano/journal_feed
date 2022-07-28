from tokenize import String
from . import *

@dataclass
def JournalSite(ABC):
    url: String
    name: String
    selectors: Selector

@dataclass
def Selector(ABC):
    container: String
    jquery: String

ajronline = JournalSite(
    url = 'https://www.ajronline.org/toc/ajr/current',
    name = 'AJR',
    selectors = ''
)
