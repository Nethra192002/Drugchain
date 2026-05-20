from src.detector import find_chains


def test_finds_known_chain():
    chains = find_chains(["ketoconazole", "atorvastatin"])
    assert len(chains) == 1
    assert chains[0].inhibitor == "ketoconazole"
    assert chains[0].substrate == "atorvastatin"


def test_ignores_unknown_drug():
    chains = find_chains(["ketoconazole", "atorvastatin", "lisinopril"])
    assert len(chains) == 1


def test_no_chain_without_inhibitor():
    chains = find_chains(["atorvastatin", "alprazolam"])
    assert chains == []


def test_no_chain_without_substrate():
    chains = find_chains(["ketoconazole", "clarithromycin"])
    assert chains == []


def test_empty_list_is_safe():
    assert find_chains([]) == []


def test_sensitive_substrate_scores_higher():
    sensitive = find_chains(["ketoconazole", "atorvastatin"])[0]
    assert sensitive.severity == 6


def test_chains_sorted_by_severity():
    chains = find_chains(["ketoconazole", "grapefruit", "atorvastatin"])
    severities = [chain.severity for chain in chains]
    assert severities == sorted(severities, reverse=True)