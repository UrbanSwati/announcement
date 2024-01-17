from utils import remove_duplicates


def test_remove_duplicates():
    phone_numbers = ["12345", "12345", "123456"]

    assert len(remove_duplicates(phone_numbers)) <= len(phone_numbers)