#########################################################
# Tech: The GECK project

class EdenizeAction:
    """Implements the custom action that lets ut improve earthlike planets."""

    def applies(self, node):
        # only on earthlike planets
        return node.NodeType == "planet.earthlike" and not node.CustomData.Has("edenized")

    def execute(self, node):
        # attach the planetary 'quirk' that implements the actual change
        # this will also set the 'edenized' flag in custom data
        attach = ConsAttachQualityOnce(node, "edenized", "QualityEdenized()")
        commands.IssueScriptedConsequence(attach)
        # we can return data here that will automatically be passed to revert() when the action
        # is undone - this is useful with more complex actions, here it's just as an example
        return {"custom": "data"}        

    def revert(self, data):
        # since all the work done in execute() was done using consequences
        # we do not have to manually revert anything
        # we still implement the method to let the engine know the action is reversible
        pass

class QualityEdenized:
    """A planetary quirk that gets added as a result of the action above."""
    BONUS_HAPPINESS = 1

    def name(self): return LStr("quirk.edenized")
    def desc(self): return LStr("quirk.edenized.desc", self.BONUS_HAPPINESS)

    # show a badge on the planet
    def visibility(self, node):
        return 1
    # the contents of the badge
    def icon(self, node): 
        return {"type": "positive", "text": ":H:"}

    def effects(self, node):
        # check conditions
        if node.Level < 2: return # not successful?
        if not node.ActuallyProduces(Resource.People): return # no people?
        # everything okay, add the happiness bonus
        return [
            ResourceFlow.Happiness(self.BONUS_HAPPINESS, FlowCategory.TechBasedHappiness)
        ]

#########################################################
# Tech: Exploratory science

class ScienceForColonizing(GlobalCondition):
    """A global condition whose main purpose is to react to ingame events."""
    def __init__(self, resource_id, science_bonus):
        self._resource = Resource.All[resource_id]
        self._bonus = science_bonus

    def activate(self):
        """This runs whenever the condition is activated - after the tech is invented or game is reloaded."""
        self.react_to(Trigger.PlanetColonized, self.when_node_colonized)

    def when_node_colonized(self, data):
        # extract the node from the data dictionary
        node = data["node"]
        # is it something we're interested in?
        has_the_resource = any(p == self._resource for p in node.Industry.Products)
        if not has_the_resource: return # nope, not the right resource
        # yes, grant resources
        # we use a consequence so this plays nicely with undo
        grant = ConsGrantResources(self._bonus, Resource.Science, node)
        commands.IssueScriptedConsequence(grant)

    def info(self):
        # this adds a description to the condition, which will automatically
        # be included as part of the description of the tech
        # other uses for this method include eg. displaying a badge and tooltip
        # for the condition in the top-left corner
        ci = CondInfo()
        ci.FullDescription = LStr("cond.science_for_colonizing.desc", self._resource.ID, self._bonus)
        return ci

#########################################################
# Tech: The GECK project

class CapSlipwayCost(GlobalCondition):
    """Makes sure that slipways never cost more than a limit."""

    def __init__(self, maximum_cost):
        self._maximum = maximum_cost

    def global_cost_adjustment(self, thing):
        """A magic method that is consulted for the cost of everything. 
           Lets us inject a method modifying connection costs."""
        # is the thing being payed for a new connection?
        if isinstance(thing, PlannedConnection):
            # yes, apply our modifier
            return self.change_connection_cost
        return None
 
    def change_connection_cost(self, current_cost, conn):
        # if the cash cost is over the maximum, reset it to the maximum
        if current_cost.Cash > self._maximum:
            current_cost = current_cost.Replace(Resource.Cash, self._maximum)
        return current_cost

    def info(self):
        # this adds a description to the condition, see other conditions above
        ci = CondInfo()
        ci.FullDescription = LStr("cond.cap_slipway_cost.desc", self._maximum)
        return ci

#########################################################
# Tech: Plant metabolism

class PlantMetabolismProject(PlanetProject):
    """Defines stuff about the project that is important before its built.
       After its built, it's effects are controlled by the associated quality."""
    def available(self, node):
        # respect base rules
        if not PlanetProject.available(self, node): return False
        # this project only applies if there is an unmet need for food
        return node.HasUnmetNeedFor(Resource.All["F"])

class PlantMetabolismQuality:
    """This quality actually implements the effects of the above project."""
    def name(self): return LStr("quality.plant_metabolism")
    def desc(self): return LStr("quality.plant_metabolism.desc")

    def effects(self, node):
        # we don't check any conditions, since we wouldn't be able to build the project
        # if it didn't work on the planet
        return [
            ChangeNeeds.Replace(Resource.All["F"], Resource.All["L"])
        ]

#########################################################
# Tech: Research bots

class ScienceOnSuccessful:
    """This quality adds a science product to all successful planets that already produce something."""
    def __init__(self, required_product):
        self._required = Resource.All[required_product]

    def name(self): return LStr("quality.science_on_successful")
    def desc(self): return LStr("quality.science_on_successful.desc", self._required.ID)

    def applies(self, node):
        """This method control which nodes this quality will be active on."""
        if node.Level < 2: return False
        if not node.ActuallyProduces(self._required): return False
        return True

    def effects(self, node):
        # always the same effects, since the conditions were checked already
        return [
            # when adding products, we need to tag them with what added them so that
            # the game engine can distinguish special products from one another
            ChangeProducts.AddOne(Resource.Science, "science_on_successful")
        ]
