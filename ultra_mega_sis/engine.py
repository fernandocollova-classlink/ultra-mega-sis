from pathlib import Path

from sqlalchemy import create_engine

from ultra_mega_sis.models import Base

Path("db.sqlite").unlink(missing_ok=True)
ENGINE = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(bind=ENGINE, checkfirst=True)
