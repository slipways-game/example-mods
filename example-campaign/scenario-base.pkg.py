name = "Scenario - Base Package"
# This package is loaded by every scenario in the custom campaign.
# Contains stuff that every mission will need.
contents = [
    # standard stuff that we're gonna need
    "/modes/standard/mapgen.py",
    "/modes/standard/setup.py",
    # generic support for campaigns
    "/modes/campaign-diaspora/campaigns.py", 
    "/modes/campaign-diaspora/campaign-scenario-base.xls",
    # the contents of our campaign
    "contents.py",
]
starting_conditions = [
    "StandardQuests()", # standard quest support (council tasks)
    "CampaignStats()",  # the campaign-specific implementation of the info tabs (scoring, domain etc.)
    "SixTechLevels()",  # the standard technology system
    "CampaignStorage()", # makes sure our progress through the campaign is saved
]
