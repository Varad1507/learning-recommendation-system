import pandas as pd

from backend.app import create_app
from backend.database import db
from backend.models import Resource

app = create_app()

CSV_PATH = "data/resources.csv"

with app.app_context():
    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():
        resource = Resource(
            topic=row["Topic"],
            difficulty=row["Difficulty"],
            resource_type=row["ResourceType"],
            title=row["Title"],
            link=row["Link"]
        )
        db.session.add(resource)

    db.session.commit()

print("✅ Resources migrated successfully")
