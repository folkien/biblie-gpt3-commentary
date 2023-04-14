'''
    Dataclass for readings and commentary media post.

'''
from dataclasses import dataclass
from models.Commentary import Commentary
from models.Readings import Readings


@dataclass
class Post:
    ''' Dataclass for readings and commentary media post.'''
    readings: Readings = None
    commentary: Commentary = None

    def __post_init__(self):
        ''' Checks if all fields are not None '''
        if (self.readings is None):
            raise ValueError('Readings is None!')

        if (self.commentary is None):
            raise ValueError('Commentary is None!')
