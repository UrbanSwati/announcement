from utils import remove_duplicates


def test_remove_duplicates():
    emails = ["test", "test2", "test"]

    assert remove_duplicates(emails) == ["test", "test2"]