from app.cafe import Cafe

from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friends_without_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            friends_without_masks += 1

    if friends_without_masks > 0:
        return f"Friends should buy {friends_without_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
