import pytest
from utils.helpers import normalize_price, is_non_empty_string

@pytest.mark.parametrize(
	"raw,expected",
	[
		("11,99 zł", 11.99),
		("4.99 PLN", 4.99),
		("  0,00 zł ", 0.0),
		("abc", 0.0),
		("", 0.0),
	],
)
def test_normalize_price(raw, expected):
	assert normalize_price(raw) == expected

@pytest.mark.parametrize(
	"value,expected",
	[
		("hello", True),
		("  spaced ", True),
		("   ", False),
		("", False),
		(123, False),
	],
)
def test_is_non_empty_string(value, expected):
	assert is_non_empty_string(value) is expected 