from dataclasses import dataclass, field

from data.drugs import DRUGS, Role, Strength

_DRUGS_BY_NAME = {drug.name: drug for drug in DRUGS}

_INHIBITOR_WEIGHT = {
    Strength.STRONG: 3,
    Strength.MODERATE: 2,
    Strength.WEAK: 1,
}


@dataclass(order=True)
class Chain:
    severity: int
    inhibitor: str = field(compare=False)
    substrate: str = field(compare=False)
    reason: str = field(compare=False)


def _score(inhibitor, substrate):
    base = _INHIBITOR_WEIGHT[inhibitor.strength]
    return base * 2 if substrate.sensitive else base


def find_chains(med_names):
    meds = [_DRUGS_BY_NAME[name] for name in med_names if name in _DRUGS_BY_NAME]
    inhibitors = [drug for drug in meds if drug.role is Role.INHIBITOR]
    substrates = [drug for drug in meds if drug.role is Role.SUBSTRATE]

    chains = [
        Chain(
            severity=_score(inhibitor, substrate),
            inhibitor=inhibitor.name,
            substrate=substrate.name,
            reason=f"{inhibitor.strength.value} inhibitor slows clearance of "
                   f"{'sensitive ' if substrate.sensitive else ''}substrate",
        )
        for inhibitor in inhibitors
        for substrate in substrates
    ]
    return sorted(chains, reverse=True)