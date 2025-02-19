#!/usr/bin/env python3
"""
Module for Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Base class for authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            Check if a path requires authentication
        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ "
        Gets the Authorization header from the request
        Args:
            request: the Flask request object
        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Gets the current user from the request
        Args:
            the Flask request object
        Returns:
            None
        """
        return None
