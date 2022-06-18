# Defines rules specific to the new race.
class StickpeopleRules(RaceRules):
    def __init__(self): RaceRules.__init__(self, "stick")
    
    def reward_for_level(self, lv):
        if lv == 1: return RewardEventOptions(self.race())
        if lv == 2: return RewardImmediate(40, 4)
        if lv == 3: return RewardTechDiscount(self.race(), 20)
        if lv == 4: return RewardHub(self.race())

class StickHubQuality(HubworldQuality):
    BONUS = 4
    def race_id(self): return "stick"
    def score_basis(self, node):
        return self.BONUS # the stick people just give you a constant +4 happiness for their hubworld
    def score(self, node):
        return math.floor(self.score_basis(node))
    def extra_desc_args(self):
        return (self.BONUS,)