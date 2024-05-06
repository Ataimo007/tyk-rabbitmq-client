from __future__ import absolute_import, unicode_literals

import datetime

from kombu import Connection

conn, q = None, None

queueName = 'tyk'
connectionString = 'amqp://ataimo@tyk.io:alex1234.@rabbitmq:5672//'

def setup():
    global conn, q
    conn = Connection(connectionString)
    conn.connect()
    q = conn.SimpleQueue(queueName)

def put(message):
    q.put(message)
