# Arete HUD - Multi-AI Query Aggregator & Synthesizer

Arete HUD is a powerful utility tool that streamlines your AI workflow by querying multiple AI providers simultaneously, analyzing their responses, and synthesizing comprehensive insights—all through a unified FastAPI backend.

## 🎯 Problem It Solves

**User Challenges:**
- ❌ **Context Switching:** Manually copying questions between different AI platforms (ChatGPT, Claude, Gemini, etc.)
- ❌ **Fragmented Insights:** Missing valuable perspectives by only consulting one AI provider
- ❌ **Time Waste:** Spending hours comparing responses across multiple AI tools
- ❌ **Decision Paralysis:** Difficulty synthesizing conflicting or complementary AI answers

**Arete HUD's Solution:**
- ✅ **Single Query, Multiple Answers:** Ask once, get responses from all your preferred AI providers
- ✅ **Intelligent Analysis:** Automatically identify differences and patterns across responses
- ✅ **Smart Synthesis:** Generate comprehensive master answers combining the best insights
- ✅ **Context Management:** Organize queries by topics for better knowledge retention

## 🚀 Key Features

- **Multi-Provider AI Querying**: Query multiple AI providers (OpenAI, Anthropic, Google, etc.) in parallel
- **Difference Analysis**: Automatically analyze and highlight differences between AI responses
- **Answer Synthesis**: Intelligently combine multiple AI perspectives into comprehensive answers
- **Topic-Based Organization**: Categorize and manage queries by subject matter
- **REST API Architecture**: Clean, scalable FastAPI backend for easy integration
- **Context Preservation**: Maintain conversation context across multiple queries

## 🔧 Technical Specifications

**Backend Architecture:**
- **Framework:** FastAPI (modern, high-performance Python web framework)
- **Language:** Python 3.8+
- **API Style:** RESTful JSON endpoints
- **CORS Support:** Configured for local development (localhost, 127.0.0.1)

**Core Components:**
- `main.py` - FastAPI application with API routes
- `agents.py` - Agent management and AI provider integration
- `context_manager.py` - Context and topic management system

**API Endpoints:**
- `GET /topics` - Retrieve available topics
- `GET /context` - Get current context state
- `POST /ask` - Query multiple AI providers simultaneously
- `POST /analyze` - Analyze differences between AI responses
- `POST /synthesize` - Synthesize a comprehensive answer from multiple responses

## 🛠️ Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/AreteDriver/Arete-HUD.git
   cd Arete-HUD
   ```

2. **Install dependencies**  
   *(Requires Python 3.8 or higher)*
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure AI Providers**
   - Set up API keys for your preferred AI providers (OpenAI, Anthropic, Google, etc.)
   - Create a `.env` file or configure environment variables with your API credentials

## ▶️ Usage

**Start the FastAPI server:**
```sh
cd backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

**Example API Requests:**

**Query Multiple AI Providers:**
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the benefits of microservices architecture?",
    "providers": ["openai", "anthropic", "google"],
    "topics": ["software-architecture"]
  }'
```

**Analyze Response Differences:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {...}
  }'
```

**Synthesize Master Answer:**
```bash
curl -X POST "http://localhost:8000/synthesize" \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {...}
  }'
```

## 💼 Value Proposition

**Time Efficiency:**
- Reduce AI consultation time by 70% - no more manual copy-pasting between platforms
- Get parallel responses instead of sequential queries

**Better Decision Making:**
- Benefit from diverse AI perspectives on complex problems
- Identify consensus and outliers across different models
- Make informed decisions with synthesized, comprehensive insights

**Enhanced Productivity:**
- Integrate multi-AI querying into existing workflows via REST API
- Build custom frontends or automation tools on top of Arete HUD
- Maintain organized knowledge with topic-based categorization

**Workflow Integration:**
- Use as a backend for custom AI dashboards
- Integrate with productivity tools and automation scripts
- Build browser extensions or CLI tools leveraging the API

## 🧑‍💻 Contributing

Pull requests are welcome!  
1. Fork the repo & create your branch from `main`.
2. Make your changes and ensure code quality.
3. Write clear commit messages and add tests where applicable.
4. Open a PR describing your changes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🐞 Troubleshooting

**Dependency Installation Issues:**
```sh
pip install --upgrade pip
cd backend
pip install -r requirements.txt
```

**API Server Not Starting:**
- Ensure Python 3.8+ is installed: `python --version`
- Check for port conflicts on port 8000
- Verify all dependencies are installed

**AI Provider Errors:**
- Double-check your API keys are correctly configured
- Ensure you have active subscriptions/credits with your AI providers
- Check network connectivity and firewall settings

**CORS Issues:**
- The backend is configured for local development by default
- For production deployment, update CORS settings in `main.py`

Check the application logs for detailed error messages and diagnostics.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.