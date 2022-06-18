name = "Example: New council race"
version = "1.0"
description = "An example of how to add a full new race to the game.\nIt's intended only as an aid for modders, it has no useful gameplay."
contents = [
    # code for the new additions
    "new-race.py", 
    # a spreadsheet that defines everything the new council race needs
    "new-race.xls",

    # The asset bundle to load, containing the assets for the new race.
    # These are exported using slipways-bundle-tool, which you can find on the Slipways Github.
    # The actual assets used are the example ones shipping with slipways-bundle-tool by default.
    "assets.win", # Windows version of the bundle
    "assets.mac", # Mac version of the bundle

    "text-english.xls" / lang("english"), # english text for the race
]
