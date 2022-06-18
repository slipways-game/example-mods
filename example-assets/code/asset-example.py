# A custom script class that lets us affect the SWDynamicView used for our custom structure, the 'frobnicator'.
# To work properly, it has to be referenced by name from the SWDynamicView.
class FrobnicatorView:
    def initialize(self, structure):
        # initialize some stuff when the object is first created
        self._last_level = None
        self._time = 0.0

    def update_after_change(self, structure):
        # play a sound when the lab first activates
        if structure.Level != self._last_level:
            if self._last_level is not None and structure.Level == 1:
                SoundCue.Custom("powerup").Play()
            self._last_level = structure.Level
    
    def each_frame(self, structure, delta_time):
        # bob up and down
        self._time += delta_time
        bob = f(math.sin(self._time) * 0.2) # f() cast the number to 'float', needed for the vector multiply below
        # self.model is accessible here thanks to "references" set on the "SWDynamicView" component
        self.model.transform.localPosition = Vector3.up * bob

# A 'global condition' class that makes sure our new planet type is added during map generation.
# It uses core functionality to do most of the job, so it's just a matter of configuration.
# This condition is activated using the 'starting_conditions' variable in mod.pkg.py
class MapGenAddMoonlikes(MapGenGuaranteePlanets):
    def __init__(self):
        MapGenGuaranteePlanets.__init__(self, [
            # add 'planet.moonlike' type planets
            # 7% of all planets close to the starting point
            # 10% elsewhere
            # replace 'barren', 'ice', 'lava', 'remnant' and 'arid' planets only
            ("planet.moonlike", 7, 10, ["planet.barren", "planet.ice", "planet.lava", "planet.remnant", "planet.arid"]),            
        ])
