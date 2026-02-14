import os
##Code Written By @ItsMeMaster
##Code Written By @ItsMeMaster

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8525803667:AAEjpylk_qaZ62O_gIZmch46S8VQNYxcY1M")
    DB_NAME = os.environ.get("DB_NAME", "nattu")
    API_ID = int(os.environ.get("API_ID", 6886135))
    API_HASH = os.environ.get("API_HASH", "ee20a1c8a8e44eaa638b7254cbcc3012")
    
    # ADMIN_ID processing: allows single ID or space-separated list of IDs from env
    _admin_id_env = os.environ.get("ADMIN_ID", "2118600611")
    try:
        ADMIN_ID = [int(x) for x in _admin_id_env.split()]
    except ValueError:
        ADMIN_ID = [2118600611]

    DB_URL = os.environ.get("DB_URL", "mongodb+srv://nattu:nattu@cluster0.quvds.mongodb.net/?appName=Cluster0")
    
    try:
        LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1003744110162))
    except ValueError:
        LOG_CHANNEL = -1003744110162

    USERLINK = os.environ.get("USERLINK", "")
    TUTORIAL_VIDEO = os.environ.get("TUTORIAL_VIDEO", "")
