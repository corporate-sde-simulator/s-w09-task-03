"""
Session Store — manages active user sessions.
This file is CLEAN — no conflicts. Don't modify.
"""


class SessionStore:
    def __init__(self, max_sessions_per_user=5):
        self.sessions = {}
        self.max_per_user = max_sessions_per_user

    def create(self, user_id: str, session_data: dict) -> str:
        import secrets
        session_id = secrets.token_hex(16)
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        # Evict oldest if over limit
        if len(self.sessions[user_id]) >= self.max_per_user:
            self.sessions[user_id].pop(0)
        self.sessions[user_id].append({'id': session_id, **session_data})
        return session_id

    def revoke(self, user_id: str, session_id: str) -> bool:
        if user_id in self.sessions:
            before = len(self.sessions[user_id])
            self.sessions[user_id] = [
                s for s in self.sessions[user_id] if s['id'] != session_id
            ]
            return len(self.sessions[user_id]) < before
        return False

    def get_active(self, user_id: str) -> list:
        return self.sessions.get(user_id, [])
