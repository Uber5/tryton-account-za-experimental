from trytond.pool import Pool

__all__ = ['register']


def register():
    Pool.register(
        module='account_za_experimental', type_='model')
    Pool.register(
        module='account_za_experimental', type_='wizard')
    Pool.register(
        module='account_za_experimental', type_='report')
