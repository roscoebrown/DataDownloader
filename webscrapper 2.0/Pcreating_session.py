from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
import Pmaking_table as Prc
session= sessionmaker(bind = Prc.engine)
session = session()

ed_user = Prc.User(name = 'ed', fullname = 'Ed Jones', nickname = 'edsnickname')
session.add(ed_user)

our_user = session.query(Prc.User).filter_by(name='ed').first() 

print(our_user)