import os
import psycopg2
#databse_url=os.environ['postgres://tcykfsyhowqcje:1bc7dcbd9c0e7c7f74d3d3d1ed6045c9832048c53bb726e5b9fb26aaf676989c@ec2-3-220-193-133.compute-1.amazonaws.com:5432/d1c1c2jkicje']
try:
    conn=psycopg2.connect(host="ec2-54-211-55-24.compute-1.amazonaws.com",database="d5vg3bqvsednid",user="cyrvcmwerwegek",password="b96dd8be6079e019632c13464a7e483645a2bedf5d191536b35f4c5e66d08366",port="5432")
except:
    print("not connected")
cur=conn.cursor()
cur.execute("""create table users(firstname varchar(50),lastname varchar (50),mobile_no varchar (12),username varchar (60),password varchar (60))""")
conn.commit()
cur.close()
conn.close()