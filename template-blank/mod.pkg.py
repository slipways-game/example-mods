name = "Template: Blank mod"
version = "1.0"
description = "Start from this template to create your own mod.\nAfter downloading the mod, copy it to your own subfolder under the mods/ directory and start editing from there."
contents = [
    # a spreadsheet that defines new objects added to the game by your mod
    # you probably need this one
    
    "things.xls",

    # code for the new additions
    
    "code.py",
    
    # localized text for your mod
    
    "text-english.xls" / lang("english"), # this is the english version

    # custom graphics/sound for your mod
    # uncomment the lines below only after creating an asset bundle with the Slipways asset tool
    # refer to the modding documentation for details on how to do that
    
    #"assets.win", "assets.mac",
]
