name = "Campaign - Example"
# This is the 'menu' package for the campaign - it's loaded for the 'scenario select' screen and it's main
# job is to point to 'contents.py', where the scenarios are defined.
contents = [
    # these are copied from the core game's modes/campaign.pkg.py, and provide basic campaign functionality
    # files from core are easier to specify with absolute paths starting with "/"
    "/modes/campaign-diaspora/campaign-menu.py",
    "/modes/campaign-diaspora/campaigns.py",
    "/modes/campaign-diaspora/campaign-storage.py",
    "/modes/standard/mapgen.py",
    # this file specifies all the contents for our campaign
    "contents.py"
]
starting_conditions = [
    "SixTechLevels()" # we need the standard "technologies" condition activated so that selecting techs for the mission works properly
]
