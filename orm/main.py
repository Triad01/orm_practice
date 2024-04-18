from sqlalchemy import create_engine, Column, String, Integer, Sequence, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "#Special1", "orm_practice_db"), pool_pre_ping=True)
Session = sessionmaker()
Session.configure(bind=engine)  # once engine is available

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)


ed_user = User(name = "ed", fullname="ed jones", nickname="edsnickname")

session = Session()
session.add(ed_user)
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

our_user = session.query(User).filter_by(name="ed").first()

ed_user.nickname = 'eddie' #updating ed's nickname
#print(our_user)


#print(session.dirty)
#print(session.new)
#session.commit()
#QUERRYING THE DATABASE=============================================
"""
for instance in session.query(User).order_by(User.id):
    print(instance)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label("name_label")).all():
    print(row.name_label)

print("=================")
for row in session.query(User.nickname.label("nickname_label")).all():
    print(row.nickname_label)

for u in session.query(User).order_by(User.id):
    print(u)

for name in session.query(User.name).filter(User.fullname=="Wendy Williams"):
    print(name)

for name in session.query(User).filter(User.name.like("%ed%")):
    print(name)

print("and query===================")
our_user = session.query(User.name).filter(User.name == 'ed', User.fullname == 'Ed Jones')
"""
for user in session.query(User).filter(text("id<224")).order_by(text("id")).all():
    print(user.name)

for user in session.query(User).filter(User.id < 224).order_by(User.id).all():
    print(user.name)
# counting ==================================
count = session.query(User.name).filter(User.name.like("%ed")).count()
print(count)
session.close()
