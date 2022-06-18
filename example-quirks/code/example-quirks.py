class ReplacementLabView:
    COLORS = [Color(0.5, 0.3, 0.3), Color(0.3, 0.6, 0.3)]

    def update_after_change(self, structure):
        active = structure.Level > 0
        self.renderer.material.SetColor("_BaseColor", self.COLORS[active])

#######################################################################

def mut_testmod_people_earn_extra():
    BONUS = 4
    return {
        "id": "people_earn_extra",
        # how this quirk is displayed
        "label": LStr("quality.people_earn_extra"),
        "description": LStr("quality.people_earn_extra.desc", 5),        
        # quirks with the same 'kind' won't get randomized together
        "kind": "cash",
        # how this quirk affects the score
        "score_modifier": -10,
        # the effects of applying the quirk - you can use the same types of effects
        # used for specifying technologies or perks in the spreadsheets
        "effects": [
            "quality(TestModQualityPeopleEarnExtra(%s))" % BONUS
        ],
        # extra packages loaded when this quirk is active, here no extra packages are needed
        # if you had a package in your mod called "quirk-package.pkg.py", you could load it by adding
        # ["mods/<your-mod-name>/quirk-package"] here
        "packages": []
    }

def mut_testmod_rich_sector():
    BONUS = 100
    return {
        # normal quirk stuff
        "id": "rich_sector",
        "label": LStr("sector_type.rich_sector"),
        "description": LStr("sector_type.rich_sector.desc", BONUS),
        "score_modifier": -10,
        "effects": [
            "cond(TestModConditionExtraMoney(%d))" % BONUS
        ],
        # control the shape of the region this sector type occupies on the galaxy map
        "area_center": Vector2(-0.23, 0.23), "area_radius": 0.05,
        "shape_offset": Vector2(0.5, 0.5),
    }

class TestModConditionExtraMoney(GlobalCondition):
    """Just grants extra money at the start of the scenario."""
    def __init__(self, bonus):
        self._bonus = bonus

    def activate(self):
        self.react_to(Trigger.ScenarioSetup, self.grant_resources)

    def grant_resources(self, _):
        game.Stock.Receive(Resource.Cash, self._bonus)

class TestModQualityPeopleEarnExtra:
    """An automatically applied quality that adds extra money flows on any planet exporting people."""
    def __init__(self, how_much):
        self.bonus = how_much

    def name(self): return LS("quality.people_earn_extra")
    def desc(self): return LS("quality.people_earn_extra.desc", None, self.bonus)
    def sentiment(self): return QualitySentiment.Positive

    def applies(self, node):
        return node.AmountExported(Resource.People) > 0

    def effects(self, node): 
        p_exported = node.AmountExported(Resource.People)
        return [ResourceFlow.Cash(p_exported * self.bonus, FlowCategory.SpecialBonuses)]

####################################################################

class TestModAddedFeatures(GlobalCondition):
    """This is our main definition condition that lets the game know what quirks and sector types we're adding.
       For this to work, you have to mention this in the 'starting_conditions' list in your mod.pkg.py.
    """
    def mod_sector_quirks(self):
        return [
            mut_testmod_people_earn_extra()
        ]

    def mod_sector_types(self):
        return [
            mut_testmod_rich_sector()
        ]
