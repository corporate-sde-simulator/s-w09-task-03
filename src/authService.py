"""
Auth Service — handles user authentication and token management.
"""

<<<<<<< HEAD (Arjun's branch)
import hashlib
import bcrypt
import secrets
from datetime import datetime, timedelta
=======
import hashlib
import secrets
import jwt
from datetime import datetime, timedelta
>>>>>>> feature/token-validation (Priya's branch)


class AuthService:
    def __init__(self, secret_key='app-secret-key-2026'):
        self.secret_key = secret_key
        self.active_sessions = {}
        self.failed_attempts = {}
        self.MAX_ATTEMPTS = 5
        self.LOCKOUT_MINUTES = 15

<<<<<<< HEAD (Arjun's branch)
    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt (industry standard)."""
        salt = bcrypt.gensalt(rounds=12)
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against bcrypt hash."""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
=======
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256 (basic)."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against SHA-256 hash."""
        return self.hash_password(password) == hashed

    def generate_token(self, user_id: str) -> str:
        """Generate a JWT token for authenticated user."""
        payload = {
            'user_id': user_id,
            'issued_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(hours=24)).isoformat(),
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def validate_token(self, token: str) -> dict:
        """Validate a JWT token and return the payload."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            expires = datetime.fromisoformat(payload['expires_at'])
            if datetime.now() > expires:
                return {'valid': False, 'error': 'Token expired'}
            return {'valid': True, 'user_id': payload['user_id']}
        except jwt.InvalidTokenError:
            return {'valid': False, 'error': 'Invalid token'}
>>>>>>> feature/token-validation (Priya's branch)

    def login(self, username: str, password: str, stored_hash: str) -> dict:
        """Authenticate a user."""
        # Check lockout
        if self._is_locked_out(username):
            return {'success': False, 'error': 'Account locked. Try again later.'}

        if not self.verify_password(password, stored_hash):
            self._record_failure(username)
            remaining = self.MAX_ATTEMPTS - self.failed_attempts.get(username, {}).get('count', 0)
            return {'success': False, 'error': f'Invalid password. {remaining} attempts left.'}

        # Clear failed attempts on success
        self.failed_attempts.pop(username, None)

<<<<<<< HEAD (Arjun's branch)
        session_id = secrets.token_hex(32)
        self.active_sessions[session_id] = {
            'username': username,
            'created_at': datetime.now(),
        }
        return {'success': True, 'session_id': session_id}
=======
        token = self.generate_token(username)
        self.active_sessions[token] = {
            'username': username,
            'created_at': datetime.now(),
        }
        return {'success': True, 'token': token}
>>>>>>> feature/token-validation (Priya's branch)

    def _is_locked_out(self, username: str) -> bool:
        info = self.failed_attempts.get(username)
        if not info or info['count'] < self.MAX_ATTEMPTS:
            return False
        elapsed = (datetime.now() - info['last_attempt']).total_seconds() / 60
        if elapsed > self.LOCKOUT_MINUTES:
            self.failed_attempts.pop(username)
            return False
        return True

    def _record_failure(self, username: str):
        if username not in self.failed_attempts:
            self.failed_attempts[username] = {'count': 0, 'last_attempt': None}
        self.failed_attempts[username]['count'] += 1
        self.failed_attempts[username]['last_attempt'] = datetime.now()
