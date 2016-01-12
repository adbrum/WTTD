import string

from django.db import models
from hashlib import sha1
from random import SystemRandom
from uuid import uuid4

CHAR = string.ascii_lowercase + string.digits + string.ascii_uppercase


def hash_(size=15, chars=CHAR):
    word = ''.join(SystemRandom().choice(chars) for _ in range(size))
    '''uuid is used to generate a random number'''
    salt = uuid4().hex
    key_hash = sha1(salt.encode() + word.encode()).hexdigest()
    return key_hash


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)
    key_hash = models.CharField('hash', max_length=40, default=hash_)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
