from database import connect

def get_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cur.fetchone()

    if not user:
        cur.execute("INSERT INTO users VALUES (?, 1, 0, 0, '')", (user_id,))
        conn.commit()
        return (user_id, 1, 0, 0, "")

    return user


def update_user(user_id, xp, level, streak, weak_topic):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE users SET xp=?, level=?, streak=?, weak_topic=?
    WHERE user_id=?
    """, (xp, level, streak, weak_topic, user_id))

    conn.commit()
    conn.close()