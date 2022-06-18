# Main entry point to the mod
name = "Example: Campaign"
version = "1.0"
description = "An example of how to add a new campaign to the game.\nIt's intended only as an aid for modders, it has no useful gameplay."
contents = [
    # this is just a small piece of code (one GlobalCondition class) that defines a new game mode - in this case, our new campaign
    "mode-definition.py",
    # localized strings should always be loaded by the main mod package, otherwise they won't work correctly later
    "text-english.xls" / lang("english")
]
starting_conditions = [
    "NewCampaign()" # this makes the game activate our new GlobalCondition
]
