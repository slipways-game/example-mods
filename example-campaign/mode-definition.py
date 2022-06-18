class NewCampaign(GlobalCondition):
    def mod_new_game_mode(self):
        """Defining this method allows us to specify a new game mode we'd like to add to Slipways."""
        return {
            # the name to display on the mode list
            "label": LStr("mode.example-campaign.title"),
            # the package for running our new game mode - this should be a separate package from your mod.pkg.py
            # this package will be loaded when the player selects your mode from the mode menu
            "package": "mods/example-campaign/menu", 
            # the 'type' of play, ie. which of the base game modes your new mode resembles the most
            # should be "standard", "campaign" (for new campaigns) or "sandbox" (for endless-based modes)            
            "mode_type": "campaign"
        }
