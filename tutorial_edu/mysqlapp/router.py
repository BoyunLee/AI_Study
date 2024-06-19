### 작성방법
# - app_label : 해당 app 이름 작성
# - return or db 부분에는 settings.py에 설정한 mysql 딕셔너리 키값 작성

class DBRouter :
    def db_for_read(self, model, **hints) :
        if model._meta.app_label == 'mysqlapp' :
            return 'mysql'
        return None
        
    def db_for_write(self, model, **hints) :
        if model._meta.app_label == 'mysqlapp' :
            return 'mysql'
        return None
        
    def allow_relation(self, obj1, obj2, **hints) :
        if obj1._meta.app_label == 'mysqlapp' or\
            obj2._meta.app_label == 'mysqlapp' :
            return True
        
        return None
        
    def allow_migrate(self, db, app_label, model_name=None, **hints) :
        if app_label == 'mysqlapp' :
            return db == 'mysql'
        
        return None