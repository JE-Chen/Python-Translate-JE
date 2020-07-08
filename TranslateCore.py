import sys
from GoogleTrans import GoogleTrans
from Translate import Translate

class TransCore():

    def __init__(self):
        try:
            self.GoogleTrans=GoogleTrans()
            self.Translate=Translate()
        except Exception as Err:
            print(Err)
            sys.exit()
