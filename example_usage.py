"""Example usage for Enterprise Brand Voice & Regulatory Claim Governance."""
from client import EnterpriseBrandGovernanceEngine

if __name__ == "__main__":
    draft = (
        "Our cheap cloud firewall uses a custom blacklist and master-slave replication. "
        "It is 100% guaranteed and unhackable with zero risk to your enterprise."
    )

    res = EnterpriseBrandGovernanceEngine.audit_and_govern_content(draft)
    print("Status:", res["status"])
    print("Terminology Replacements:", res["terminology_replacements"])
    print("Regulatory Flags:", res["regulatory_risk_flags"])
    print("Remediated Copy:", res["remediated_content"])
