# Arete HUD for Notion

Arete HUD is a Python-powered human interface for visualizing, tracking, or optimizing data from Notion and related productivity tools.

## 🚀 Features
- Visual overlay and heads-up display for Notion dashboards/tasks
- Real-time status tracking and updates
- Customizable widgets

## 🛠️ Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/AreteDriver/Arete-HUD.git
   cd Arete-HUD
   ```

2. **Install dependencies**  
   *(You may need Python 3.8+.)*
   ```sh
   pip install -r requirements.txt
   ```

3. **Configuration**
   - Create a `.env` or edit `config.py` to set Notion integration keys.
   - See [Notion developer docs](https://developers.notion.com/) for API credentials.

## ▶️ Usage

```sh
python aretehud.py
```
Or run the appropriate GUI or dashboard module for your platform.

## ⚙️ Configuration

- Edit `config.py` or use the GUI's built-in settings.
- Supported options:
  - NOTION_API_KEY
  - Dashboard widgets, overlays, etc.

## 🧑‍💻 Contributing

Pull requests are welcome!  
1. Fork the repo & create your branch.
2. Write clear commit messages and unit tests.
3. Open a PR describing your change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 🐞 Troubleshooting

- If dependencies fail:
  ```sh
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
- For Notion API errors: double-check your API key and permissions.
- See the log files in the project directory for diagnostics.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.