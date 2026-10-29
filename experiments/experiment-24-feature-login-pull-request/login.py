def login(username: str, password: str, accounts: dict[str, str]) -> bool:
    """Teaching sample only; production must use salted password hashes/provider."""
    return username in accounts and accounts[username] == password
