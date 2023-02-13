import random

fond = 0
GDP = 7.98*10**9
EveryMonth = [GDP]

class Pop():
    count = 0
    cut = 0

    def __init__(self) -> None:
        Pop.count += 1
        self.cut = random.randint(0, 400)
        global fond
        fond += self.cut

    def getCount() -> int:
        return Pop.count

    def vote(self):
        return random.randint(0, 1)

    def taxCut(self):
        global fond
        fond += self.cut



class Region():
    pops = []
    MoP = 3800

    def __init__(self) -> None:
        for i in range(0, 1341270):
            self.pops.append(Pop())

    def voteCounter(self) -> int:
        votes = 0
        for i in self.pops:
            votes += i.vote()
        return votes

    def newMeanOfProduction(self, mod, id):
        self.MoP += 1
        cases = [5, 10, 20,
                 25, 30, 40, 45, 50, 100, 200, 300, 1000]
        id = random.randint(id, len(cases) - 1)
        workplaces = cases[id]
        global GDP
        GDP =  GDP + (3 * workplaces * 1498) * mod
        for i in range(0, workplaces):
            self.pops.append(Pop())
    
    def isWon(self) -> float:
        return world.voteCounter() * 100 / Pop.getCount()

    def newMonth(self, mod):
        for i in self.pops:
            i.taxCut()

        for i in range(0, int(random.randint(0, 50) * (mod/2))):
            if self.isWon() > 50:
                cases = [20000, 28000, 40000, 80000, 140000, 260000, 400000, 700000, 1500000, 3000000, 7000000, 10000000]
                id = random.randint(0, len(cases) - 1)
                cost = cases[id]
                global fond
                fond -= cost
                self.newMeanOfProduction(mod, id)
    

world = Region()
print("Month: ", i+1)
print("Population: ", Pop.getCount())
print("Fond money: ", fond)
print("MoPs: ", world.MoP)
print("GDP: ", GDP)
print("GDP per capita: ", GDP / Pop.getCount())

for i in range(0, 12):
    world.newMonth(i+5)
    print("Month: ", i+1)
    print("Population: ", Pop.getCount())
    print("Fond money: ", fond)
    print("MoPs: ", world.MoP)
    print("GRP: ", GDP)
    print("GRP per capita: ", GDP / Pop.getCount())
    EveryMonth.append(GDP)
    print()

x = 0
for i in EveryMonth:
    x += i
print("GDP(annual): ", x)
