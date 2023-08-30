from sqlalchemy import create_engine, text
import os


db_connection_string = "mysql+pymysql://luqf3de0ycyamk7eupi9:pscale_pw_aYMFlIsMwakAyGNPXnzPYt7Ic0GRQCfQxzsJB1DN0Pk@aws.connect.psdb.cloud/kelvincareers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
            return jobs
