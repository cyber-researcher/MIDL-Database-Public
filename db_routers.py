class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hint):  # this allows the route_app_labels to read the db
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_for_write(self, model, **hint):  # this allows the route_app_labels to write the db
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_for_relation(self, obj1, obj2, **hint):  # this allows the route_app_labels to make relations the db
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hint):  # What apps can migrate onto the db
        if app_label in self.route_app_labels:
            return db == 'users'
        return None


class Modules:
    route_app_labels = {'modules'}

    def db_for_read(self, model, **hint):  # this allows the route_app_labels to read the db
        if model._meta.app_label in self.route_app_labels:
            return 'modules'
        return None

    def db_for_write(self, model, **hint):  # this allows the route_app_labels to write the db
        if model._meta.app_label in self.route_app_labels:
            return 'modules'
        return None

    def db_for_relation(self, obj1, obj2, **hint):  # this allows the route_app_labels to make relations the db
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None