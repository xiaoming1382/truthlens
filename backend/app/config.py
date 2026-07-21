import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAPH_DAEMON_URL = os.getenv("TELEGRAPH_DAEMON_URL", "http://13.237.89.59:7044/daemon")
TELEGRAPH_DISPATCHER_URL = os.getenv("TELEGRAPH_DISPATCHER_URL", "http://13.237.89.59:7044/miner-dispatcher")
PAYAI_FACILITATOR_URL = os.getenv("PAYAI_FACILITATOR_URL", "https://facilitator.payai.network")
