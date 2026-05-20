from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    INHIBITOR = "inhibitor"
    SUBSTRATE = "substrate"
    INDUCER = "inducer"


class Strength(Enum):
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"


@dataclass(frozen=True)
class Drug:
    name: str
    role: Role
    strength: Strength
    sensitive: bool = False


DRUGS = [
    Drug("ketoconazole", Role.INHIBITOR, Strength.STRONG),
    Drug("itraconazole", Role.INHIBITOR, Strength.STRONG),
    Drug("clarithromycin", Role.INHIBITOR, Strength.STRONG),
    Drug("grapefruit", Role.INHIBITOR, Strength.MODERATE),
    Drug("rifampin", Role.INDUCER, Strength.STRONG),
    Drug("carbamazepine", Role.INDUCER, Strength.STRONG),
    Drug("phenytoin", Role.INDUCER, Strength.STRONG),
    Drug("st johns wort", Role.INDUCER, Strength.STRONG),
    Drug("atorvastatin", Role.SUBSTRATE, Strength.WEAK, sensitive=True),
    Drug("alprazolam", Role.SUBSTRATE, Strength.WEAK, sensitive=True),
]