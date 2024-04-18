from sqlalchemy import create_engine, Column, String, Integer, Sequence
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
print(our_user)


print(session.dirty)
print(session.new)
session.commit()

session.close()
