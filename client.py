"""Enterprise Brand Voice and Regulatory Claim Governance Engine.
100% Python Standard Library.
"""

from typing import List, Dict, Any, Optional
import re


class EnterpriseBrandGovernanceEngine:
    """Audits and auto-remediates AI-generated enterprise copy against approved terminology
    glossaries, banned regulatory/legal risk claims, and sentence readability limits."""

    DEFAULT_TERMINOLOGY_MAP = {
        "cheap": "cost-effective",
        "blacklist": "denylist",
        "whitelist": "allowlist",
        "master-slave": "primary-replica",
        "ai hallucination": "ungrounded model output",
    }

    REGULATORY_RISK_PATTERNS = [
        {"category": "unsubstantiated_guarantee", "pattern": r"\b(100%\s+guaranteed|zero\s+risk|guaranteed\s+returns|never\s+fails)\b"},
        {"category": "unauthorized_medical_claim", "pattern": r"\b(cures|clinically\s+proven\s+to\s+eliminate|fda\s+approved\s+cure)\b"},
        {"category": "absolute_security_promise", "pattern": r"\b(unhackable|100%\s+breach-proof|immune\s+to\s+cyberattacks)\b"},
    ]

    @classmethod
    def audit_and_govern_content(
        cls,
        content: str,
        custom_glossary: Optional[Dict[str, str]] = None,
        max_sentence_words: int = 28,
    ) -> Dict[str, Any]:
        """Scans text for terminology violations, high-risk regulatory claims, and readability issues,
        returning both an audit report and an auto-remediated draft."""
        glossary = dict(cls.DEFAULT_TERMINOLOGY_MAP)
        if custom_glossary:
            glossary.update(custom_glossary)

        remediated_text = content
        terminology_replacements = []

        # 1. Enforce terminology glossary
        for banned_term, preferred_term in glossary.items():
            pattern = re.compile(re.escape(banned_term), re.IGNORECASE)
            matches = list(pattern.finditer(remediated_text))
            if matches:
                terminology_replacements.append({
                    "disallowed_term": banned_term,
                    "preferred_term": preferred_term,
                    "occurrences": len(matches),
                })
                remediated_text = pattern.sub(preferred_term, remediated_text)

        # 2. Detect regulatory / legal risk claims
        regulatory_flags = []
        for rule in cls.REGULATORY_RISK_PATTERNS:
            for match in re.finditer(rule["pattern"], content, re.IGNORECASE):
                regulatory_flags.append({
                    "risk_category": rule["category"],
                    "flagged_phrase": match.group(0),
                    "span": [match.start(), match.end()],
                })

        # 3. Check sentence length readability
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', content) if s.strip()]
        long_sentences = []
        for idx, sent in enumerate(sentences):
            word_count = len(re.findall(r'\w+', sent))
            if word_count > max_sentence_words:
                long_sentences.append({"sentence_index": idx, "word_count": word_count, "preview": sent[:60] + "..."})

        compliant = (len(regulatory_flags) == 0) and (len(terminology_replacements) == 0)
        return {
            "status": "COMPLIANT_APPROVED" if compliant else "GOVERNANCE_ACTION_REQUIRED",
            "compliant": compliant,
            "terminology_replacements": terminology_replacements,
            "regulatory_risk_flags": regulatory_flags,
            "readability_warnings": long_sentences,
            "remediated_content": remediated_text,
        }
