from dotenv import load_dotenv
import os 

load_dotenv()

Groq_api = os.getenv("groq_api")
News_data_api = os.getenv("NEWS_DATA_API_KEY")
sarvam_api = os.getenv("sarvam_api_key")

if not Groq_api:
    raise ValueError("groq api key not found in .env")
if not News_data_api:
    raise ValueError("news data api not found in .env")