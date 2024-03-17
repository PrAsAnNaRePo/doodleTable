from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import pandas as pd
import os
from tempfile import NamedTemporaryFile

app = FastAPI()

if not os.path.exists("public_files"):
    os.makedirs("public_files")

app.mount("/files", StaticFiles(directory="public_files"), name="static")

class HTMLTable(BaseModel):
    html_table: str

@app.post("/setFile")
async def set_file(request: Request, html_table_data: HTMLTable):
    df = pd.read_html(html_table_data.html_table)[0]
    with NamedTemporaryFile(delete=False, dir="public_files", suffix='.xlsx') as temp_file:
        df.to_excel(temp_file.name)
        file_basename = os.path.basename(temp_file.name)
        file_url = str(request.url_for('static', path=file_basename))
    return {"message": "File created successfully", "download_url": file_url}
