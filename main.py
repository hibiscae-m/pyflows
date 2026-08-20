#!/bin/env python3

from fastapi import FastAPI, File, UploadFile, HTTPException
from starlette.responses import FileResponse
from starlette.background import BackgroundTasks
import os
import uuid

app = FastAPI()
out_dir = 'out/'
in_dir = 'in/'

def generate_file(size_mb):
    mb = 1000000
    new_uuid = str(uuid.uuid4())
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    with open(out_dir + new_uuid, 'wb') as file:
        file.write(os.urandom(size_mb*mb))
        file.close()
    return new_uuid

def remove_file(path: str) -> None:
    os.unlink(path)

@app.get("/getfile/{size_mb}")
async def read_getfile(size_mb: int, background_tasks: BackgroundTasks):
    try:
        file = generate_file(size_mb)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong...')
    background_tasks.add_task(remove_file, out_dir + file)
    return FileResponse(out_dir + file, media_type='application/octet-stream', filename=file)

@app.post("/putfile")
async def upload(file: UploadFile = File(...)):
    try:
        new_uuid = str(uuid.uuid4())
        if not os.path.isdir(in_dir):
            os.mkdir(in_dir)
        with open(in_dir + new_uuid, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong...')
    finally:
        file.file.close()

    remove_file(in_dir + new_uuid)
    return {"message": f"File uploaded successfully"}
