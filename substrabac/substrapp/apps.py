from django.apps import AppConfig
from django.db.models.signals import post_delete, pre_save


class SubstrappConfig(AppConfig):
    name = 'substrapp'

    def ready(self):
        from .signals.algo.post_delete import algo_post_delete
        from .signals.challenge.post_delete import challenge_post_delete
        from .signals.data.post_delete import data_post_delete
        from .signals.dataset.post_delete import dataset_post_delete
        from .signals.model.post_delete import model_post_delete
        from .signals.data.pre_save import data_pre_save

        # registering signals with the model's string label
        from substrapp.models import Algo, Challenge, Data, Dataset, Model

        post_delete.connect(algo_post_delete, sender=Algo)
        post_delete.connect(challenge_post_delete, sender=Challenge)
        post_delete.connect(data_post_delete, sender=Data)
        post_delete.connect(dataset_post_delete, sender=Dataset)
        post_delete.connect(model_post_delete, sender=Model)

        pre_save.connect(data_pre_save, sender=Data)
