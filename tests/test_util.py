from utils import remove_duplicates


def test_remove_duplicates():
    phone_numbers = ["12345", "12345", "123456"]

    assert remove_duplicates(phone_numbers) == ["12345", "123456"]