from tokenize import String
from . import *

@dataclass
def XMLFields(ABC):
    url: String
    name: String
    selectors: Selector

@dataclass
def Selector(ABC):
    url: String
    jquery: String
