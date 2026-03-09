import pytest

from rofi_rbw.models.card import Card
from rofi_rbw.models.credentials import Credentials
from rofi_rbw.models.note import Note


@pytest.mark.parametrize(
    "entry",
    [
        Note("test", "", [], "some notes"),
        Credentials("test", "", [], "user", "pass", False, "", []),
        Card("test", "", [], None, "1234", None, "1", "2025", None, None),
    ],
    ids=["note", "credentials", "card"],
)
def test_default_target_return_values(entry):
    for target in entry.default_target:
        assert entry[target] is not None
