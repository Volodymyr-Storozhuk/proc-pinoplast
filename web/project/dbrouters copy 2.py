
class EurobudDbRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'forming_kl':
            # print('read from model:' + model._meta.app_label)
            return 'forming_db_kl'
        elif model._meta.app_label == 'foaming_kl':
            # print('read from model:' + model._meta.app_label)
            return 'foaming_db_kl'
        elif model._meta.app_label == 'forming_kr':
            # print('read from model:' + model._meta.app_label)
            return 'forming_db_kr'
        elif model._meta.app_label == 'foaming_kr':
            # print('read from model:' + model._meta.app_label)
            return 'foaming_db_kr'
        # elif model._meta.app_label != 'forming_kl' and model._meta.app_label != 'foaming_kl' and model._meta.app_label != 'forming_kr' and model._meta.app_label != 'foaming_kr':
        #     print('label1: read from model:' + model._meta.app_label)
        #     return 'default'
        # elif model._meta.app_label == 'default':
        #     return 'default'
        # else:
        #     return None
        # print('read from model:' + model._meta.app_label)
        return 'default'

    def db_for_write(self, model, **hints):
        # dont allow write on the legacy database
        # return None or False for the legacy database
        if model._meta.app_label == 'forming_kl':
            # return 'forming_db_kl'
            return False
        elif model._meta.app_label == 'foaming_kl':
            # return 'foaming_db_kl'
            return False
        elif model._meta.app_label == 'forming_kr':
            # return 'forming_db_kr'
            return False
        elif model._meta.app_label == 'foaming_kr':
            # return 'foaming_db_kr'
            return False
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        app_list = ('forming_db_kl', 'foaming_db_kl', 'forming_db_kr', 'foaming_db_kr')
        if obj1._state.db in app_list and obj2._state.db in app_list:
            print("allow_relation label: " + obj1._meta.app_label + "|" + obj2._meta.app_label)
            print("allow_relation db: " + obj1._state.db + "|" + obj2._state.db)
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # dont allow migrations on the legacy database too:
        # this will enable to actually alter the database schema of the legacy DB!
        if db == 'forming_db_kl' and app_label == "forming_kl":
            return False
        if db == 'foaming_db_kl' and app_label == "foaming_kl":
            return False
        if db == 'forming_db_kr' and app_label == "forming_kr":
            return False
        if db == 'foaming_db_kr' and app_label == "foaming_kr":
            return False
        # allow migrations on the "default" (django related data) DB
        return True
