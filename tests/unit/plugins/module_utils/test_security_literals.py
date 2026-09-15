# Copyright: (c) 2026, Dell Technologies
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Security regression tests for credential fixtures.

Scope: only test_storage_node.py, the file where the CxSAST
"Use Of Hardcoded Password" finding was previously in the "To Verify"
(open) state. Other files with a similar "password" fixture value were
already reviewed and dispositioned as "Not Exploitable" by the security
team; they are intentionally left untouched here so that prior triage in
CxSAST is not invalidated by a content change (Checkmarx re-opens a
finding as new/"To Verify" whenever the flagged line's content changes).
"""

from pathlib import Path
import re


# Matches a dict/kwarg literal string assigned directly to a "password" key,
# e.g. {'password': 'literal-value'} or "password": "literal-value".
PASSWORD_STRING_LITERAL = re.compile(r'''["']password["']\s*:\s*["'][^"']+["']''')

STORAGE_NODE_TEST_FILE = (
    Path(__file__).parents[1] / "modules" / "test_storage_node.py"
)


def test_storage_node_test_does_not_assign_literal_password_strings():
    """test_storage_node.py must not assign a hardcoded string literal to a
    'password' field. Use a runtime-generated value (e.g. uuid.uuid4().hex)
    instead, so the value can never be mistaken for a real credential."""
    content = STORAGE_NODE_TEST_FILE.read_text(encoding="utf-8")

    assert not PASSWORD_STRING_LITERAL.search(content)
