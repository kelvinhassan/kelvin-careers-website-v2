from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+mysqlconnector://asqx5nahdx2b9yo6dvdy:pscale_pw_Y9GPLPeM3RHjRxesz9hOzvb7NmyC3uEgF0FBRtygckc@aws.connect.psdb.cloud:3306/kelvincareers"

engine = create_engine(db_connection_string, echo=True)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
            return jobs
