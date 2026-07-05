"""Test configuration for Asset Management Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "asset-management-agent", "category": "IT Operations"}
