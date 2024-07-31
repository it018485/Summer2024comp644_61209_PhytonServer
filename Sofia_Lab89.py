import sqlalchemy as sa
from sqlalchemy import String, Integer, Column, ForeignKey, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# I create two dictionaries with my data
myUsers = {
    10: 'Sofia',
    20: 'Maria',
    30: 'Gino'
}

MyPosts = {
    (11, 'ciao belli', 10),
    (12, 'this one was a challenge', 20),
    (13, 'hopefully it works', 30)
}

DATABASE_URL = "mariadb+mariadbconnector://root:SofiaDB@localhost/IP_DB"
MioDB = sa.create_engine(DATABASE_URL)

# I create my Class and I put inside the declariations of my 2 tables.
class MyClass(DeclarativeBase):
    pass

class User(MyClass):
    __tablename__='users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50),nullable=False)

class Posts(MyClass):
    __tablename__='posts'
    post_id = Column(Integer, primary_key=True)
    post_descr = Column(String(125),nullable=False)
    post_user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

# I create everything that is inside my class (2 tables)
MyClass.metadata.create_all(MioDB)

# I cycle my first dictionary and I insert data in Users.
for user_id, user_name in myUsers.items():
    insert_query = text(f"INSERT INTO users (user_id, user_name) VALUES ({user_id}, '{user_name}');")

    with MioDB.connect() as connection:
        connection.execute(insert_query)
        connection.commit()

# I cycle my second dictionary and I insert data in Posts.
for post in MyPosts: 
    post_id, post_descr, post_user_id = post
    insert_query = text(f"INSERT INTO posts (post_id, post_descr, post_user_id) VALUES ({post_id}, '{post_descr}', {post_user_id});")

    with MioDB.connect() as connection:
        connection.execute(insert_query)
        connection.commit()