"""Asset Management Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_register_asset():
    """Test Register a new IT asset with specifications and assignment."""
    tools = AgentTools()
    result = await tools.register_asset(asset_type="test", serial_number="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_lifecycle():
    """Test Track asset lifecycle stage (procurement, deployed, maintenance, retired)."""
    tools = AgentTools()
    result = await tools.track_lifecycle(asset_id="test", action="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_license_compliance():
    """Test Check software license compliance across the organization."""
    tools = AgentTools()
    result = await tools.check_license_compliance(software="test", department="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forecast_refresh():
    """Test Forecast assets due for refresh based on age and warranty."""
    tools = AgentTools()
    result = await tools.forecast_refresh(asset_type="test", months_ahead=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.asset_management_agent_agent import AssetManagementAgentAgent
    agent = AssetManagementAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
