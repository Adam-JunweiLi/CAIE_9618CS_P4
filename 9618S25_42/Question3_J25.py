# ================================
# Question 3 – May/June 2025
# ================================

class Animal:
    def __init__(self, name, sound, size, intelligence):
        self.Name = name
        self.Sound = sound
        self.Size = size
        self.Intelligence = intelligence

    def Description(self):
        return (
            "The animal's name is " + self.Name +
            ", it makes a " + self.Sound +
            ", its size is " + str(self.Size) +
            " and its intelligence level is " + str(self.Intelligence)
        )


class Parrot(Animal):
    def __init__(self, name, sound, size, intelligence, wingspan, words):
        super().__init__(name, sound, size, intelligence)
        self.WingSpan = wingspan
        self.NumberWords = words

    def ChangeNumberWords(self, change):
        self.NumberWords += change

    def Description(self):
        return (
            super().Description() +
            ". It has a wingspan of " + str(self.WingSpan) +
            "cm and can say " + str(self.NumberWords) + " words."
        )


class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, territory):
        super().__init__(name, sound, size, intelligence)
        self.TerritorySize = territory

    def SetTerritorySize(self, change):
        self.TerritorySize += change

    def Description(self):
        return (
            super().Description() +
            ". Its territory is " + str(self.TerritorySize) + " square miles."
        )


# ---------- 3(d)(i) ----------
Animal1 = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
Animal2 = Wolf("Nighteyes", "Howl", 8, 7, 100)
Animal3 = Animal("Copper", "Neigh", 10, 6)

# ---------- 3(d)(ii) ----------
Animal2.SetTerritorySize(-20)
Animal1.ChangeNumberWords(2)

print(Animal1.Description())
print(Animal2.Description())
print(Animal3.Description())

# ---------- 3(d)(iii) ----------
# Screenshot replaced by comment
