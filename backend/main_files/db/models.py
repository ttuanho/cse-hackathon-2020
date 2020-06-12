# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'sys_user'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)

#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                             self.name, self.fullname, self.nickname)
        
#         return "<sys_user( \
#             username = '%s', \
#             email = '%s', \
#             profile_img_url = '%s',\ 
#             firstname = '%s', \
#             lastname = '%s', \
#             city = '%s', \
#             country = '%s', \
#         )" % (\
            
#         )