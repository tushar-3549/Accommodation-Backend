import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

debug = (os.environ.get("DEBUG") or "").strip().lower()

if debug == "true":
    print("DEBUG ENABLED")
    from .dev import *  # noqa
elif debug == "false":
    print("DEBUG DISABLED")
    from .prod import *  # noqa
else:
    logger.error("Invalid DEBUG environment variable. Must be 'true' or 'false'.")
    raise ValueError("Invalid DEBUG environment variable. Must be 'true' or 'false'.")
