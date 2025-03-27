import pymongo

class MongoDB():
    def __init__(self):
        # 连接数据库
        self.conn = pymongo.MongoClient('mongodb://localhost:27017/')
        # 获取数据库  不存在则创建
        self.db = self.conn["demo"]
        # 获取集合对象 不存在则创建
        self.coll = self.db['coll']
    
    # 获取所有数据库
    def get_dbs(self):
        dblist = self.conn.list_database_names()
        return dblist
    # 获取所有集合
    def get_cols(self):
        print(self.db.list_collection_names())

    # 插入一条记录
    def insert_one(self,dict):
        ans = self.coll.insert_one(dict)
        if ans.inserted_id != None:
            return True
        return False
    
    # 插入多条记录
    def insert_many(self,dict_list):
        ans = self.coll.insert_many(dict_list)
        if len(ans.inserted_ids) > 0:
            return True
        return False

    # 查询所有数据 return:list
    def find_all(self):
        ans = []
        for data in self.coll.find({},{'_id':0,'title':1,'year':1}):
            ans.append(data)
        return ans
    
    # 根据查询条件查询数据 return:list
    def find_by_query(self,query_dict):
        ans = []
        for data in self.coll.find(query_dict):
            ans.append(data)
        return ans