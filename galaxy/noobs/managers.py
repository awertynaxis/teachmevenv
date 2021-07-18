from django.db.models import Manager


class BaseFilterManager(Manager):
    def not_archived(self):
        return self.filter(archived=True)