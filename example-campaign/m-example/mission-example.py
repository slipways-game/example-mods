class ExampleMainMission(MainMission):
    def __init__(self):
        MainMission.__init__(self, "example", [EMGoalSuccessfulPlanets(2)])

    @staticmethod
    def get():
        return game.Conditions.Get("ExampleMainMission()").PythonObject

    def scenario_id(self): return "m-example"

    def scoring_rules(self):
        return []

    def conditions(self): 
        return [
            (WinMissionOnTime, "ExampleMainMission()", 25),
        ]
    
    def perks_available(self):
        return ["well_prepared", "reciprocity", "miners", "prospectors", "prosperity", "nutrition", "efficient", "joint_factories", "scholars", "curiosity"]

    def things_to_explain(self):
        return []    


class EMGoalSuccessfulPlanets:
    def __init__(self, required_count):
        self._required = required_count
    def state(self):
        count = game.Nodes.CountPlanetsWithLevelOrHigher(2)
        return count
    def check_completion(self):
        return self.state() >= self._required
    def description(self): return LStr("mission.example.goal.successful_planets", self._required)
    def short(self):
        current = self.state()
        return "%d/%d:lv2:" % (current, self._required)
