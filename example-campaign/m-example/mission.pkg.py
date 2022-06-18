name = "Mission - Example mission"
contents = [
    "mission-example.py", # mission code
]
starting_conditions = [
    # base stuff
    "StandardMapgen()", # to get the map generated
    "StandardConditions('no_time_limit')", # load some standard rules
    "CampaignScoring()", # special scoring rules for campaigns
    # mission-specific
    "ExampleMainMission()", # our own mission-specific condition
]