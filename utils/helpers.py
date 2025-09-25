def normalize_price(text: str) -> float:
	"""Convert a price string like '11,99 zł' or '4.99 PLN' to a float (11.99, 4.99).
	Returns 0.0 if parsing fails.
	"""
	if not isinstance(text, str):
		return 0.0
	clean = (
		text.replace("\xa0", " ")
		.replace("zł", "")
		.replace("PLN", "")
		.strip()
	)
	# Replace comma decimal with dot
	clean = clean.replace(",", ".")
	digits = "".join(ch for ch in clean if ch.isdigit() or ch == ".")
	try:
		return float(digits) if digits else 0.0
	except ValueError:
		return 0.0


def is_non_empty_string(value) -> bool:
	"""Return True if value is a non-empty string after trimming."""
	return isinstance(value, str) and value.strip() != "" 