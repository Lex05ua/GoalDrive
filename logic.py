def get_progress_percentage(goal: float, current: float) -> float:
    """Calculates how much of the goal is achieved in %."""
    if goal <= 0:
        return 0.0
    return round((current / goal) * 100, 2)

def get_remaining_time(goal: float, current: float, monthly: float) -> float:
    """Calculates months left to reach the goal."""
    remaining = goal - current
    if remaining <= 0:
        return 0.0
    if monthly <= 0:
        return 0.0
    return round(remaining / monthly, 1)

def get_work_effort(amount: float, hourly_rate: float) -> dict:
    """Converts money into work hours and days (8h/day)."""
    hours = amount / hourly_rate
    days = hours / 8
    return {
        "hours": round(hours, 1),
        "days": round(days, 1)
    }