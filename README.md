# genpark-enterprise-brand-voice-and-regulatory-claim-governance-skill

Enterprise terminology glossary enforcer, regulatory claim risk scanner, and brand voice compliance engine for generative AI workflows.

100% Python Standard Library implementation with zero external dependencies.

## Key Capabilities

- **Terminology Glossary Enforcement & Auto-Remediation**: Automatically replaces deprecated, off-brand, or non-inclusive terminology with approved enterprise vocabulary (e.g., `cheap` -> `cost-effective`, `blacklist` -> `denylist`).
- **Regulatory & Legal Liability Scanner**: Detects high-liability absolute claims (`100% guaranteed`, `zero risk`, `unhackable`, unverified medical assertions) with character-span offsets before publication.
- **Readability & Cadence Guardrails**: Flags overly dense sentences exceeding enterprise style thresholds.

## Architecture

```
[AI-Generated Marketing / Technical Copy]
                    │
                    ▼
┌──────────────────────────────────────────────────┐
│        EnterpriseBrandGovernanceEngine           │
│  1. Approved Terminology Glossary Rewriter       │
│  2. Regulatory Liability Claim Scanner           │
│  3. Sentence Length Readability Auditor          │
└──────────────────────────────────────────────────┘
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
[Remediated Clean Copy]    [Compliance Audit Report]
```

## MCP Server Integration

Run standard MCP stdio server:
```bash
python mcp_server.py
```

Exposed Tools:
- `audit_and_govern_enterprise_copy`: Scans generated text against enterprise terminology glossaries, regulatory risk patterns, and readability bounds.

## Quickstart (Python API)

```python
from client import EnterpriseBrandGovernanceEngine

res = EnterpriseBrandGovernanceEngine.audit_and_govern_content(
    "Our cheap platform is 100% guaranteed and uses a custom whitelist."
)
print("Remediated:", res["remediated_content"])
print("Risk Flags:", res["regulatory_risk_flags"])
```

---

## GenPark Ecosystem

- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
