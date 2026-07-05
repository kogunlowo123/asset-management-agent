# Asset Management Agent

[![CI](https://github.com/kogunlowo123/asset-management-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/asset-management-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: IT Operations | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

IT asset management agent that tracks hardware and software assets throughout their lifecycle, manages procurement workflows, monitors license compliance, forecasts refresh cycles, and generates asset reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `register_asset` | Register a new IT asset with specifications and assignment |
| `track_lifecycle` | Track asset lifecycle stage (procurement, deployed, maintenance, retired) |
| `check_license_compliance` | Check software license compliance across the organization |
| `forecast_refresh` | Forecast assets due for refresh based on age and warranty |
| `generate_asset_report` | Generate asset inventory and utilization report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/assets/register` | Register asset |
| `PUT` | `/api/v1/assets/{asset_id}/lifecycle` | Track lifecycle |
| `GET` | `/api/v1/assets/licenses` | Check license compliance |
| `GET` | `/api/v1/assets/refresh-forecast` | Forecast refresh |
| `POST` | `/api/v1/assets/report` | Generate report |

## Features

- Asset Tracking
- Lifecycle Management
- License Compliance
- Procurement Workflow
- Refresh Forecasting

## Integrations

- Servicenow Cmdb
- Snipe It
- Flexera
- Snow Software
- Microsoft Intune

## Architecture

```
asset-management-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── asset_management_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CMDB + Asset Management Platform + Procurement**

---

Built as part of the Enterprise AI Agent Platform.
