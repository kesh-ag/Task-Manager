from sqlmodel import Session, create_engine

Database_URL="postgresql+psycopg2://postgres:Kesh161206@localhost:5433/task_manager_db"
engine = create_engine(Database_URL) 

def get_session():
    with Session(engine) as session:
        yield session 