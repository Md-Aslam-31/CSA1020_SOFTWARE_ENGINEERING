"""Password-hash verification sample for Experiment 24.

This file is a small learning exercise, not a complete authentication system.
"""

from collections.abc import Mapping
import hashlib
import hmac

DEFAULT_ITERATIONS = 200_000


def make_user_record(password: str, *, salt: bytes, iterations: int = DEFAULT_ITERATIONS) -> dict[str, str | int]:
    """Build a salted PBKDF2 record for a test or local demonstration."""
    if not isinstance(password, str) or not password:
        raise ValueError("password must be a non-empty string")
    if not isinstance(salt, bytes) or len(salt) < 16:
        raise ValueError("salt must contain at least 16 bytes")
    if isinstance(iterations, bool) or not isinstance(iterations, int) or iterations < 100_000:
        raise ValueError("iterations must be an integer of at least 100000")

    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return {"salt": salt.hex(), "iterations": iterations, "password_hash": digest.hex()}


def login(username: str, password: str, accounts: Mapping[str, object]) -> bool:
    """Return True only when the supplied password matches a valid stored hash."""
    if not isinstance(username, str) or not username or not isinstance(password, str) or not password:
        return False
    if not isinstance(accounts, Mapping):
        return False

    record = accounts.get(username)
    if not isinstance(record, Mapping):
        return False

    salt_hex = record.get("salt")
    expected_hex = record.get("password_hash")
    iterations = record.get("iterations")
    if not isinstance(salt_hex, str) or not isinstance(expected_hex, str):
        return False
    if isinstance(iterations, bool) or not isinstance(iterations, int) or not 100_000 <= iterations <= 2_000_000:
        return False

    try:
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(expected_hex)
    except ValueError:
        return False
    if len(salt) < 16 or len(expected) != hashlib.sha256().digest_size:
        return False

    actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(actual, expected)
