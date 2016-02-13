from NorvigSpell import NorvigSpell as Spell


class zaSpeller:

    def check_spelling(self, word):

        incorrectFlag = False

        corrected = self.spel.correct(word)
        if word != corrected:
            print 'corrected ', word, 'to', corrected
            incorrectFlag = True

        return incorrectFlag, corrected

    def __init__(self):
        check=['spel','spellin','categorie','category','gandi']
        self.spel = Spell()

        map(self.check_spelling,check)





if __name__ == '__main__':
        zaSpeller()