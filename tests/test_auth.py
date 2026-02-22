import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from authService import AuthService

class TestMergeResolution:
    def test_no_conflict_markers(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'authService.py')) as f:
            content = f.read()
        assert '<<<<<<<' not in content, "Conflict markers still present"
        assert '=======' not in content, "Conflict markers still present"
        assert '>>>>>>>' not in content, "Conflict markers still present"

    def test_bcrypt_import(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'authService.py')) as f:
            content = f.read()
        assert 'import bcrypt' in content, "bcrypt import missing (Arjun's change)"

    def test_jwt_import(self):
        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'authService.py')) as f:
            content = f.read()
        assert 'import jwt' in content, "jwt import missing (Priya's change)"

    def test_validate_token_exists(self):
        auth = AuthService()
        assert hasattr(auth, 'validate_token'), "validate_token method missing"

    def test_generate_token_exists(self):
        auth = AuthService()
        assert hasattr(auth, 'generate_token'), "generate_token method missing"

    def test_hash_uses_bcrypt(self):
        auth = AuthService()
        hashed = auth.hash_password('test123')
        assert hashed.startswith('$2'), "hash_password should use bcrypt"

    def test_login_returns_token(self):
        auth = AuthService()
        hashed = auth.hash_password('mypassword')
        result = auth.login('testuser', 'mypassword', hashed)
        assert result['success'] is True
        assert 'token' in result, "login should return a JWT token"
