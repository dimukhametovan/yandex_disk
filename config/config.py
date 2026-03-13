import os
from dotenv import load_dotenv
load_dotenv()

YANDEX_DISK_TOKEN =  os.getenv("API_TOKEN")

BASE_URL = "https://cloud-api.yandex.net/v1/disk"