""" HArold BERnie P. Garcia
DATALOG quiz01
Feb. 11, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code.
"""
class DrumKit:

    def __init__(self):
        self.top_hat = True
        self.snare = True


class DrumKitTest:
    def play_tophat(self):
        print("ding ding di-ding")

    def play_snare(self):
        print("bang bang ba-bang")


d = DrumKitTest()
d.play_tophat()
d.play_snare()

if d.play_snare == True:
    d.play_snare = False

if __name__ == "__main__":
    DrumKitTest()