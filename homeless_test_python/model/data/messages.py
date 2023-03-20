from enum import Enum


class Messages(Enum):
    ONE_TIME_DONATION_WARNING = 'Вы выбрали разовое пожертвование'
    REGULAR_DONATION_WARNING = 'Вы выбрали регулярные пожертвования'

    THREE_HUNDRED_MESSAGE = '300 рублей'
    SEVEN_HUNDRED_MESSAGE = '700 рублей'
    ONE_THOUSAND_MESSAGE = '1000 рублей'
    THREE_THOUSAND_MESSAGE = '3000 рублей'