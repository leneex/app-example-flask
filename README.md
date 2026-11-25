# Flask

Example [Flask](https://flask.palletsprojects.com/en/3.0.x/) app. Flask is a lightweight Python web framework that is easy to start with and easy to extend.

## Deploy settings

| Field | Value |
| --- | --- |
| Build | Railpack |
| Project directory | `/` |
| Install command | leave empty |
| Build command | leave empty |
| Start command | leave empty |
| Application port | `8000` |
| Health check path | `/` |

## <a name="dev"></a>Run locally

```bash
# virtual environment and dependencies
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# start the app
python3 main.py
```
