# This file describes the campaign to the game - mostly what scenario there are and the progression
# between them.

##############################################################
# Mutators for every mission

def scenario_example():
    return {
        "label": LStr("mission.example"),
        "description": LStr("mission.example.short"),
        "packages": ["mods/example-campaign/m-example/mission"]
    }

def scenario_second():
    # this second mission is unimplemented, just here as an example
    return {
        "label": LStr("mission.second"),
        "description": LStr("mission.second.short"),
        "packages": ["mods/example-campaign/m-second/mission"]
    }

##############################################################
# Helpers

def std_menu_flow(mutator, class_name):
    """Makes it easier to define mission below."""
    package_name = mutator()["packages"][0]
    return "StdMissionMenuFlow('%s', '%s()')" % (package_name, class_name)

##############################################################
# Actual mission list

# This class has to be called 'CampaignContents' so the game can find the missions
class CampaignContents:
     # unique identifier for our campaign (controls eg. where progress is stored)
    CAMPAIGN_ID = "campaign-example"
    # this package will get auto-loaded for each scenario in the campaign
    # it's main job is setting up things common to all scenario, and loading contents.py so
    # it is also available during the game
    SCENARIO_BASE_PACKAGE = "mods/example-campaign/scenario-base"

    # the list of scenarios (missions) to complete
    SCENARIOS = {
        "m-example": {
            # defines the 'menu flow' that happens after the scenario is selected
            # this uses the "standard" mission menu flow, which will load our main mission class
            # and use it to display the briefing, etc.
            "menu_flow": std_menu_flow(scenario_example, "ExampleMainMission"),
            "main_mutator": scenario_example, # the mutator defining the mission
            "icon": "icon_eye", # a 64x64 icon, usually should be provided in an asset bundle shipping with your mod
            "position": (-0.32, -0.36), # position on the map
            # if you have multiple missions in your campaign, you can specify progression by listing missions that have to be completed first here
            # just the identifiers, eg. ["m-some-other-mission", "m-yet-another-mission"]
            "requires": [] 
        },

        # this is a definition for the next mission - it's unimplemented, this is here just to show how to define progression
        "m-second": {
            "menu_flow": std_menu_flow(scenario_second, "SecondMainMission"),
            "main_mutator": scenario_second,
            "icon": "icon_probe", 
            "position": (-0.12, -0.4),            
            "requires": ["m-example"]
        }
    }
