[project]
dependencies = [
    "fastapi",
    "uvicorn[standard]",       # ASGI server
    "sqlalchemy",              # ORM
    "alembic",                 # DB migrations
    "asyncpg",                 # Async PostgreSQL driver
    "pydantic-settings",       # Environment config
    "python-jose[cryptography]", # JWT auth
    "passlib[bcrypt]",         # Password hashing
    "python-multipart",        # File uploads
    "boto3",                   # AWS S3 for images
    "redis",                   # Caching / sessions
    "celery",                  # Background jobs (e.g. email, image resize)
    "pillow",                  # Image processing
]

[tool.uv]  # or use pip