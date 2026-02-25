import os
import os
from dotenv import load_dotenv
# Load environment variables from openai.env file
load_dotenv("../assets/openai.env")

# Read the OPENAI_API_KEY from the environment
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_API_BASE"] = api_base