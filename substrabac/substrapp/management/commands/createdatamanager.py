import json
import ntpath

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from rest_framework import status

from substrapp.management.commands.bulkcreatedatasample import bulk_create_data_sample
from substrapp.serializers import DataManagerSerializer, LedgerDataManagerSerializer
from substrapp.utils import get_hash
from substrapp.views.datasample import LedgerException


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class Command(BaseCommand):
    help = '''
    create datamanager
    python ./manage.py createdatamanager '{"dataset": {"name": "foo", "data_opener": "./opener.py", "description": "./description.md", "type": "foo", "challenge_keys": []}, "data": {"paths": ["./data.zip", "./train/data"], "test_only": false}}'
    python ./manage.py createdatamanager dataset.json
    # datamanager.json:
    # challenge_keys are optional
    # {"datamanager": {"name": "foo", "data_opener": "./opener.py", "description": "./description.md", "type": "foo", "challenge_keys": []}, "data": {"paths": ["./data.zip", "./train/data"], "test_only": false}}
    '''

    def add_arguments(self, parser):
        parser.add_argument('data_input', type=str)

    def handle(self, *args, **options):

        # load args
        args = options['data_input']
        try:
            data_input = json.loads(args)
        except:
            try:
                with open(args, 'r') as f:
                    data_input = json.load(f)
            except:
                raise CommandError('Invalid args. Please review help')
        else:
            if not isinstance(data_input, dict):
                raise CommandError('Invalid args. Please provide a valid json file.')

        datamanager = data_input.get('data_manager', None)
        if datamanager is None:
            return self.stderr.write('Please provide a data_manager')
        if 'name' not in datamanager:
            return self.stderr.write('Please provide a name to your data_manager')
        if 'type' not in datamanager:
            return self.stderr.write('Please provide a type to your data_manager')
        if 'data_opener' not in datamanager:
            return self.stderr.write('Please provide a data_opener to your data_manager')
        if 'description' not in datamanager:
            return self.stderr.write('Please provide a description to your data_manager')

        data_samples = data_input.get('data_samples', None)
        if data_samples is None:
            return self.stderr.write('Please provide some data samples')
        if 'paths' not in data_samples:
            return self.stderr.write('Please provide paths to your data sample')
        if 'test_only' not in data_samples:
            return self.stderr.write('Please provide a boolean test_only parameter to your data samples')

        # TODO add validation
        with open(datamanager['data_opener'], 'rb') as f:
            filename = path_leaf(datamanager['data_opener'])
            data_opener = ContentFile(f.read(), filename)

        with open(datamanager['description'], 'rb') as f:
            filename = path_leaf(datamanager['description'])
            description = ContentFile(f.read(), filename)

        pkhash = get_hash(data_opener)
        serializer = DataManagerSerializer(data={
            'pkhash': pkhash,
            'data_opener': data_opener,
            'description': description,
            'name': datamanager['name'],
        })

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            self.stderr.write(str(e))
        else:
            # create on db
            try:
                instance = serializer.save()
            except Exception as e:
                self.stderr.write(str(e))
            else:
                # init ledger serializer
                ledger_serializer = LedgerDataManagerSerializer(
                    data={'name': datamanager['name'],
                          'permissions': 'all', # forced, TODO changed when permissions are available
                          'type': datamanager['type'],
                          'objective_keys': datamanager.get('objective_keys', []),
                          'instance': instance})

                try:
                    ledger_serializer.is_valid()
                except Exception as e:
                    # delete instance
                    instance.delete()
                    self.stderr.write(str(e))
                else:
                    # create on ledger
                    res, st = ledger_serializer.create(
                        ledger_serializer.validated_data)

                    if st not in (status.HTTP_201_CREATED, status.HTTP_202_ACCEPTED, status.HTTP_408_REQUEST_TIMEOUT):
                        self.stderr.write(json.dumps(res, indent=2))
                    else:
                        d = dict(serializer.data)
                        d.update(res)
                        msg = f'Successfully added datamanager with status code {st} and result: {json.dumps(res, indent=4)}'
                        self.stdout.write(self.style.SUCCESS(msg))

        # Try to add data even if datamanager creation failed

        self.stdout.write('Will add data to this datamanager now')
        # Add data in bulk now
        data_samples.update({'data_manager_keys': [pkhash]})
        try:
            res, st = bulk_create_data_sample(data_samples)
        except LedgerException as e:
            if e.st == status.HTTP_408_REQUEST_TIMEOUT:
                self.stdout.write(self.style.WARNING(json.dumps(e.data, indent=2)))
            else:
                self.stderr.write(json.dumps(e.data, indent=2))
        except Exception as e:
            return self.stderr.write(str(e))
        else:
            msg = f'Successfully bulk added data samples with status code {st} and result: {json.dumps(res, indent=4)}'
            self.stdout.write(self.style.SUCCESS(msg))
