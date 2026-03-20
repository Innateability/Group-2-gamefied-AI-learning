def add_xp(user, correct):
    user_id, level, xp, streak, weak = user

    if correct:
        xp += 10
        streak += 1
    else:
        streak = 0

    if xp >= level * 50:
        level += 1
        xp = 0

    return xp, level, streak