from dataclasses import dataclass


@dataclass
class Messages:
    ONE_TIME = 'one-time'
    REGULAR = 'regular'
    THREE_HUNDRED_MESSAGE = '300 рублей'
    ONE_TIME_DONATION_WARNING = 'Вы выбрали разовое пожертвование'
    REGULAR_DONATION_WARNING = 'Вы выбрали регулярные пожертвования'
    THREE_HUNDRED_MESSAGE = '300 рублей'
    SEVEN_HUNDRED_MESSAGE = '700 рублей'
    ONE_THOUSAND_MESSAGE = '1 000 рублей'
    THREE_THOUSAND_MESSAGE = '3 000 рублей'
