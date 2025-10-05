from datetime import datetime

def greeting(now_provider=datetime.now):
    """
    Return a greeting string based on the hour of day.
    now_provider: a callable returning a datetime (injected for testing).
    """
    hour = now_provider().hour
    if 5 <= hour < 12:
        return "good morning"
    if 12 <= hour < 18:
        return "good afternoon"
    if 18 <= hour < 22:
        return "good evening"
    return "hello night owl"
