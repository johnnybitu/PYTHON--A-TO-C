class father:
    def __init__(self):
        super().__init__()
        self.dna = "lazy"
        self.hair = "blcak"
    def show(self):
        self.mood = "angry"
        return self.mood

class mother:
    def __init__(self):
        super().__init__()
        self.writing = "clen"
        self.wnat = "icecream"
    def showm (self):
        self.mom = "mom is "
        return self.mom

class child(father, mother):
    def __init__(self):
        super().__init__()
        self.nature = self.dna
        self.hairs = self.hair
        self.writings = self.writing
    def childeren (self):
        self.overall = "good"
        return self.overall
        

johnny = child()
print(f'{ johnny.dna, johnny.hair, johnny.writing, johnny.childeren(), johnny.overall}')