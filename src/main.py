from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


from src.api.security_params import router as router_security_params


app = FastAPI()

app.include_router(router_security_params)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
