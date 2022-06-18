name = "Example: Custom assets"
version = "1.0"
description = "An example of how to add things to the game that require custom assets.\nIt's intended only as an aid for modders, it has no useful gameplay."
author = "krajzeg"
contents = [
    "code/asset-example.py", # code for the new additions

    # a spreadsheet defines a new planet type, a new structure and a new resource
    # we will be providing graphics/sound for those from the asset bundle
    "additions.xls",

    # The asset bundle to load. These are exported using the Slipways asset-tool, which you can find on the Slipways Github.
    # The actual assets used are the example ones shipping with the tool.
    "assets.win", # Windows version of the bundle
    "assets.mac", # Mac version of the bundle

    "text-english.xls" / lang("english"), # english text
]
starting_conditions = [
    "MapGenAddMoonlikes()", # this condition class ensures that our newly added planet type actually appears after map generation
]