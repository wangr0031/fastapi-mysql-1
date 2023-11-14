import uvicorn

from app.core.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        app="api.app:app",
        host=settings.config.APP_HOST,
        port=settings.config.APP_PORT,
        log_level=settings.config.LOG_LEVEL,
        reload=settings.config.HOT_RELOAD,
    )
