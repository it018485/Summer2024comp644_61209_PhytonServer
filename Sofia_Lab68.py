import sqlalchemy as sa
from sqlalchemy import text
from faker import Faker
import sqlite3 

# I create a memory SQLite database
myMemoryDB = sa.create_engine("sqlite:///:memory:", echo=True)

# I create the container (MetaData) for my DB objects
Contenitore = sa.MetaData()

# Now I define the Table "users", which I put into my Container
users_table = sa.Table(
    "users",
    Contenitore,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("user_name", sa.String(50)),
    sa.Column("active", sa.Boolean),
)
# Now I create everything I have in the Container, in this case only a Table
Contenitore.create_all(myMemoryDB)

# I create a Faker object 
myFakeData = Faker()

# I connect to my memory DB and I cycle 10 times, adding fake data
with myMemoryDB.connect() as conn:
    for _ in range(10):
        conn.execute(users_table.insert().values
                     (user_name=myFakeData.user_name(),
                      id=myFakeData.uuid4(),
                      active=myFakeData.boolean()))
        
# TASK 2: Create a View of the memory table.
# Note! Some versions of sqlalchemy want the statement in "text" format.
    conn.execute(text('''
    CREATE VIEW miaView AS
    SELECT * FROM users
    '''))

# Run a simple SQL extraction
    result = conn.execute(text('''
    SELECT * FROM miaView WHERE active=True
    '''))

# Print the rows
    rows = result.fetchall()
    for row in rows:
        print(row)