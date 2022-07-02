import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Все карточки пропусков:', Passcard.objects.all())

    rand_number = random.randint(0, len(Passcard.objects.all()))
    some_passcard = Passcard.objects.all()[rand_number]
    print('owner_name:', some_passcard.owner_name)
    print('owner_name:', some_passcard.passcode)
    print('owner_name:', some_passcard.created_at)
    print('owner_name:', some_passcard.is_active)

    active_cards = []
    for card in Passcard.objects.all():
        if card.is_active:
            active_cards.append(card)
    print('Активных пропусков: ', len(active_cards))

    active_cards2 = Passcard.objects.filter(is_active=True)
    print('Активных пропусков: ', len(active_cards2))
