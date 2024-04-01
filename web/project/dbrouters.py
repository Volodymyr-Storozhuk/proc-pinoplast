class EurobudDbRouter:

    # Робоча версія
    def db_for_read(self, model, **hints):
        app_list = ('forming_kl', 'foaming_kl', 'forming_kr', 'foaming_kr')
        # print('read label0: current model:' + model._meta.app_label)

        # allow read on the legacy database
        if model._meta.app_label in app_list:
            if model._meta.app_label == 'forming_kl':
                # print('read label1: read from model:' + model._meta.app_label)
                return 'forming_db_kl'
            elif model._meta.app_label == 'forming_kr':
                # print('read label1: read from model:' + model._meta.app_label)
                return 'forming_db_kr'
            elif model._meta.app_label == 'foaming_kl':
                # print('read label1: read from model:' + model._meta.app_label)
                return 'foaming_db_kl'
            elif model._meta.app_label == 'foaming_kr':
                # print('read label1: read from model:' + model._meta.app_label)
                return 'foaming_db_kr'
        # allow read on the "default" (django related data) DB
        else:
            # print('read label1: read from model (default): ' + model._meta.app_label)
            return 'default'

    # Робоча версія
    def db_for_write(self, model, **hints):
        app_list = ('forming_kl', 'foaming_kl', 'forming_kr', 'foaming_kr')
        # print('write label0: current model:' + model._meta.app_label)

        # dont allow write on the legacy database
        # return None or False for the legacy database
        if model._meta.app_label in app_list:
            # print('write label1: deny write to model: ' + model._meta.app_label)
            return False
        # allow write on the "default" (django related data) DB
        else:
            # print('write label1: allow write to model (default): ' + model._meta.app_label)
            return 'default'

    # Робоча версія
    def allow_relation(self, obj1, obj2, **hints):
        app_list = ('forming_kl', 'foaming_kl', 'forming_kr', 'foaming_kr')
        # print(f'allow_relation label0: current obj1 | obj2: {obj1._meta.app_label} | {obj2._meta.app_label}')
        # print(f'allow_relation db0: current obj1 | obj2: {obj1._state.db} | {obj2._state.db}')

        if obj1._meta.app_label in app_list and obj2._meta.app_label in app_list:
            # print("allow_relation label1: in app list " + obj1._meta.app_label + " | " + obj2._meta.app_label)
            # print("allow_relation db1: in app list " + obj1._state.db + " | " + obj2._state.db)
            return True
        if obj1._meta.app_label not in app_list and obj2._meta.app_label not in app_list:
            # print("allow_relation label2: not in app list  " + obj1._meta.app_label + " | " + obj2._meta.app_label)
            # print("allow_relation db2: not in app list  " + obj1._state.db + " | " + obj2._state.db)
            return True

    # Робоча версія
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        app_list = ('forming_kl', 'foaming_kl', 'forming_kr', 'foaming_kr')

        if db == 'default':
            # dont allow migrations on the legacy database:
            # this will enable to actually alter the database schema of the legacy DB!
            if app_label not in app_list:
                # print('allow migrations for db: ' + db)
                # print('allow migrations for app: ' + app_label)
                return True
            # allow migrations on the "default" (django related data) DB
            else:
                # print('deny migrations for db: ' + db)
                # print('deny migrations for app: ' + app_label)
                return False
