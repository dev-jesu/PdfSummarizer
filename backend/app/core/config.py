import os
from dotenv import load_dotenv

print("DEBUG: Current working directory =", os.getcwd())

load_dotenv()  # default behavior

print("DEBUG: GEMINI_API_KEY from env =", os.getenv("GEMINI_API_KEY"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
