"""MCP server for Enterprise Brand Voice & Regulatory Claim Governance."""
import sys
import json
from client import EnterpriseBrandGovernanceEngine


def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "audit_and_govern_enterprise_copy",
                    "description": "Scans generated text against enterprise terminology glossaries, regulatory risk patterns, and readability bounds",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "content": {"type": "string"},
                            "custom_glossary": {"type": "object"},
                            "max_sentence_words": {"type": "integer", "default": 28},
                        },
                        "required": ["content"],
                    },
                }
            ]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "audit_and_govern_enterprise_copy":
            res = EnterpriseBrandGovernanceEngine.audit_and_govern_content(
                args.get("content", ""),
                custom_glossary=args.get("custom_glossary"),
                max_sentence_words=args.get("max_sentence_words", 28),
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
