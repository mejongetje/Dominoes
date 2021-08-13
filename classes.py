import itertools
import random

class Tile:
    def __init__(self, nose, mouth):
        self.nose = nose
        self.mouth = mouth

    def switch(self):
        self.nose, self.mouth = self.mouth, self.nose

    def __repr__(self):
        return f'({self.nose}, {self.mouth})'

    def __lt__(self, other):
        if isinstance(other, Tile):
            return self.nose < other.nose
        else:
            return False

    # def __eq__(self, other):
    #     if isinstance(other, Tile):
    #         return self.nose == other.nose
    #     else:
    #         return False


class DomSet:
    def __init__(self):
        self.tiles = []
        a = 0
        for x in range(7): 
            if x > 0:  
                a += 1
            for y in range(a,7):
                t = Tile(x,y)
                self.tiles.append(t)

    def __getitem__(self, s):
        return self.tiles[s]


class Game:
    def __init__(self):
        self.hand = [[],[],[],[]]
        dom_set = DomSet()
        playset = dom_set.tiles[:]
        random.shuffle(playset)
        index_cycle = itertools.cycle([0,1,2,3])        
        for tile in playset:
            self.hand[next(index_cycle)].append(tile)
        for lst in self.hand:
            lst.sort(key=lambda x: x.mouth, reverse=True) 
            lst.sort(key=lambda x: x.nose, reverse=True)
        self.doublesix = self.doublesix_searcher()
        self.sixsix = 1 if self.doublesix == 0 else (2 if self.doublesix == 7 else (3 if self.doublesix == 14 else 4))
        self.active_position = 0

    def doublesix_searcher(self):
        ch = list(itertools.chain(*self.hand))
        for x in range(len(ch)):
            if ch[x].nose == 6 and ch[x].mouth == 6:
                self.doublesix = ch.index(ch[x])
                return self.doublesix


class Player:

    players = []

    def __init__(self, name, type="human", active=" "):
        self.name = name
        self.games_won = 0
        self.hand = None
        self.type = type
        self.active = active
        __class__.players.append(self)

    def __repr__(self):
        return self.name

p1 = Player('Froggy', 'digital')
p2 = Player('Bigga', 'digital', '_')
p3 = Player('Pops', 'digital', '_')
p4 = Player('You', 'human')


