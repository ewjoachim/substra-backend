# Create your tasks here
from __future__ import absolute_import, unicode_literals


from substrapp.utils import invokeLedger


def createLedgerTesttuple(args, sync=False):
    options = {
        'args': '{"Args":["createTesttuple", ' + args + ']}'
    }
    return invokeLedger(options, sync)