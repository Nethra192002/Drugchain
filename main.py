from src.detector import find_chains

SAMPLE_MEDS = ["ketoconazole", "atorvastatin", "lisinopril"]


def format_chain(chain):
    return (f"[severity {chain.severity}] {chain.inhibitor} + {chain.substrate} "
            f"\u2014 {chain.reason}")


def run(med_names):
    chains = find_chains(med_names)
    if not chains:
        return "No interaction chains found."
    header = f"Found {len(chains)} chain(s), most severe first:"
    return "\n".join([header] + [format_chain(chain) for chain in chains])


if __name__ == "__main__":
    print(run(SAMPLE_MEDS))