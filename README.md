# NEURA by LUXORANOVA

A fully automated, self-optimizing AI SaaS factory with zero manual operations.

## Core Components

1. **Agent System**
   - CrewAI-based agent orchestration
   - Multiple agent roles (Researcher, Writer, Developer, Analyst)
   - Self-improving feedback loops
   - Auto-logging and optimization

2. **Control Dashboard**
   - Appsmith-based monitoring interface
   - Real-time agent status
   - Task management
   - System metrics visualization

3. **Voice Control**
   - TermGPT integration
   - Natural language command processing
   - Voice-activated system control
   - Command history tracking

4. **Mobile Interface**
   - Real-time updates via Socket.io
   - Responsive web interface
   - Agent monitoring and control
   - Task creation and management

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/neura.git
cd neura
```

2. **Set Up Docker Environment**
```bash
docker-compose up -d
```

3. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

4. **Start Core Services**
```bash
# Start FastAPI backend
python core/main.py

# Start Socket.io server
python core/mobile/socket_server.py

# Start voice control system
python core/voice/commander.py
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| FastAPI Backend | 8000 | Core API endpoints |
| Socket.io Server | 8001 | Real-time mobile updates |
| Ollama | 11434 | Local LLM service |
| OpenWebUI | 3000 | LLM interface |
| n8n | 5678 | Workflow automation |
| Flowise | 3001 | Agent chains |
| Appsmith | 80 | Control dashboard |
| Uptime-Kuma | 3002 | Service monitoring |
| ChromaDB | 8001 | Vector storage |
| SuperAGI | 9000 | Agent management |
| Grafana | 3003 | Metrics visualization |

## Features

### 1. Agent System
- Multiple agent roles with specific capabilities
- Self-improving feedback loops
- Inter-agent communication
- Auto-logging and optimization

### 2. Task Management
- Create and assign tasks to agents
- Monitor task progress
- View task history
- Auto-optimization of task distribution

### 3. Voice Control
- Natural language commands
- System status queries
- Agent creation and management
- Task execution

### 4. Mobile Access
- Real-time system monitoring
- Agent control
- Task management
- System metrics

### 5. Monitoring
- Service health checks
- Resource usage tracking
- Performance metrics
- Auto-recovery

## API Endpoints

### Core API
- `GET /health` - System health status
- `GET /agents` - List all agents
- `POST /agents` - Create new agent
- `GET /tasks` - List all tasks
- `POST /tasks` - Create new task
- `GET /metrics` - System metrics

### WebSocket Events
- `system_status` - Real-time system updates
- `agents_list` - Agent status updates
- `metrics_update` - Live metrics
- `task_created` - Task creation notifications

## Development

1. **Local Development**
```bash
# Start services in development mode
docker-compose -f docker-compose.dev.yml up -d

# Start backend with auto-reload
uvicorn core.main:app --reload
```

2. **Testing**
```bash
pytest tests/
```

## Security

- All API endpoints are secured
- WebSocket connections authenticated
- Voice commands verified
- Data encryption in transit and at rest

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See LICENSE file for details.

## Support

For support, email support@luxoranova.ai or join our Discord community.
