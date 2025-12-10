import pathlib
import uuid
from datetime import datetime

def create_temp_outdir(root):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    unique_id = uuid.uuid4().hex[:8]
    temp_outdir_path = pathlib.Path(root) / f"{timestamp}_{unique_id}"
    temp_outdir_path.mkdir(parents=True, exist_ok=True)
    return temp_outdir_path