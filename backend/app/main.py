from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import tasks, chat  # apne project ke hisaab se imports same rakho

app = FastAPI(title="Todo Backend")

# ✅ CORS: allow from anywhere (minikube service tunnel ports change hotay rehtay hain)
# NOTE: allow_origins="*" ke saath allow_credentials False hona chahiye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(tasks.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
