name = "Example: Sector types and quirks"
version = "1.0"
description = "This mod is an example of how to add new sector types and quirks.\nIt's intended only as an aid for modders, it has no useful gameplay."
contents = [
    "code/example-quirks.py", # test mod code
    "text-english.xls" / lang("english"), # english text used by the mod
]
starting_conditions = [
    "TestModAddedFeatures()"
]
