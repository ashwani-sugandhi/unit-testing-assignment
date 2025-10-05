def is_feature_enabled(user_role: str) -> bool:
    """
    Temporary behavior: only 'admin' has the feature enabled.
    We'll use skip/expectedFailure in tests for roles not yet supported.
    """
    return user_role == "admin"
