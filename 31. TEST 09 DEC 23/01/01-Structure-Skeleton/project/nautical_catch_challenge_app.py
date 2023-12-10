from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."
        diver_to_add = self._find_diver_by_name(diver_name)
        if diver_to_add:
            return f"{diver_name} is already a participant."
        diver_to_add = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(diver_to_add)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        fish_to_add = self._find_fish_by_name(fish_name)
        if fish_to_add:
            return f"{fish_name} is already permitted."
        fish_to_add = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(fish_to_add)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._find_diver_by_name(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish = self._find_fish_by_name(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_needed_help = [d for d in self.divers if d.has_health_issue]
        for diver in divers_needed_help:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(divers_needed_help)}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_diver_by_name(diver_name)
        if diver:
            result = f"**{diver_name} Catch Report**\n"
            if diver.catch:
                result += '\n'.join(f.fish_details() for f in diver.catch)
            return result

    def competition_statistics(self):
        arranged_divers_good_health = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = None

        if arranged_divers_good_health:
            sorted_divers = list(sorted(arranged_divers_good_health, key=lambda d: (-d.competition_points, -len(d.catch), d.name)))

        result = "**Nautical Catch Challenge Statistics**\n"

        if sorted_divers:
            result += '\n'.join(d.__str__() for d in sorted_divers)
        return result

# _________________________HELPER METHODS_______________________________________________________________________________
    def _find_fish_by_name(self, given_fish_name: str):
        return next((f for f in self.fish_list if f.name == given_fish_name), None)

    def _find_diver_by_name(self, given_name: str):
        return next((d for d in self.divers if d.name == given_name), None)