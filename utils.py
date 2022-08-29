import numpy as np


classes = [['Диффузный индекс цен на выпускаемую продукцию, ожидаемые изменения ',
  'Диффузный индекс цен на покупаемую продукцию, ожидаемые изменения ',
  'Диффузный индекс заработной платы, ожидаемые изменения ',
  'Диффузный индекс занятости, ожидаемые изменения ',
  'Диффузный индекс портфеля заказов, ожидаемые изменения ',
  'Производство молока, тыс.тонн ',
  'Производство яиц, млн',
  'Грузооборот транспорта, млрд.т-км ',
  'Коммерческий грузооборот транспорта, млрд.т-км ',
  'Строительство, млрд. руб.',
  'Импорт товаров,  млрд. долл., index',
  'Экспорт товаров, СНГ, млрд. долл., index',
  'Импорт товаров, СНГ, млрд. долл., index',
  'Реальный оборот розничной торговли',
  'Реальный оборот розничной торговли, продукты',
  'Реальный оборот розничной торговли, непродовольственные',
  'Реальный объем платных услуг',
  'Средние цены производителей, мазут',
  'Ставка по краткосрочным кредитам, население',
  'Ставка по долгосрочным кредитам, фирмы'],
 ['Диффузный индекс выпуска, ожидаемые изменения ',
  'Диффузный индекс закупок оборудования, ожидаемые изменения ',
  'Диффузный индекс финансового состояния, ожидаемые изменения ',
  'Производство скота и птицы, тыс.тонн ',
  'Ж/д перевозки,  млн.тонн.',
  'Инвестиции, млрд. рублей',
  'Обеспеченность оборота розничной торговли запасами, дней',
  'MIACR',
  'Ставка по долгосрочным кредитам, население',
  'Ставка по краткосрочным кредитам, фирмы'],
 ['Диффузный индекс задолженности банкам, ожидаемые изменения ',
  'Реальные инвестиции, млрд. рублей',
  'Ввод в действие жилых домов, млн кв.м',
  'Дефицит бюджета, млрд.руб.'],
 ['Экспорт товаров,  млрд. долл., index',
  'Курс доллара',
  'Курс евро',
  'Оборот розничной торговли, млрд.руб.',
  'Оборот розничной торговли, непродовольственные, млрд.руб.',
  'Товарные запасы в организациях розничной торговли, млрд.руб.',
  'Средние цены производителей, нефть',
  'Средние цены производителей, газ',
  'Средние цены производителей, бензин',
  'Средние цены производителей, дизельное топливо',
  'Средние цены производителей, яйца',
  'Безработицв',
  'Потребность работодателей в работниках',
  'Нагрузка не занятого трудовой деятельностью населения',
  'Реальная зарплата',
  'Цена Urals, долл/бар'],
 ['Оборот розничной торговли, продукты, млрд.руб.',
  'Реальные товарные запасы в организациях розничной торговли',
  'Индекс потребительских цен',
  'Индекс потребительских цен, продукты',
  'Индекс потребительских цен, непродовольственные',
  'Индекс потребительских цен, услуги',
  'Средние цены производителей, уголь',
  'Средние цены производителей, животноводство',
  'Средние цены производителей, крупный рогатый скот',
  'Средние цены производителей, птица',
  'Средние цены производителей, молоко',
  'Средние цены производителей, инвестиционные товары',
  'Средние цены производителей, строительная продукция',
  'Индекс тарифов на грузоперевозки',
  'Среднемесячная зарплата, руб.',
  'Среднемесячная пенсия, руб.',
  'Реальная пенсия',
  'Краткосрочные кредиты и прочие средства нефинансовым организациям, млрд.руб',
  'Долгосрочные кредиты и прочие средства нефинансовым организациям, млрд.руб']]

classes_quart = [['ВВП, млрд',
  'ВВП C, млрд.руб.',
  'ВВП D, млрд.руб.',
  'ВВП G, млрд.руб.',
  'ВВП H, млрд.руб.',
  'ВВП I, млрд.руб.',
  'ВВП J, млрд.руб.',
  'ВВП K, млрд.руб.',
  'ВВП L, млрд.руб.',
  'ВВП M, млрд.руб.',
  'ВВП N, млрд.руб.',
  'ВВП O, млрд.руб.',
  'Налоги на продукты, млрд.руб.',
  'Реальный ВВП J'],
 ['Реальный ВВП',
  'ВВП B, млрд.руб.',
  'ВВП E, млрд.руб.',
  'ВВП F, млрд.руб.',
  'Реальный ВВП G',
  'Реальный ВВП I',
  'Реальный ВВП K',
  'Реальные налоги на продукты',
  'Реальные субсидии на продукты',
  'Инвестиции, собственные средства, млрд.руб.'],
 ['ВВП A, млрд.руб.',
  'Субсидии на продукты, млрд.руб.',
  'Реальный ВВП A',
  'Реальный ВВП C',
  'Реальный ВВП D',
  'Реальный ВВП H',
  'Реальный ВВП M',
  'Реальный ВВП N',
  'Реальный ВВП O',
  'Инвестиции, привлеченные средства, млрд.руб.',
  'Инвестиции, бюджетные средства, млрд.руб.'],
 ['Реальный ВВП B', 'Реальный ВВП E', 'Реальный ВВП F', 'Реальный ВВП L']]


def make_features_quart_reg(prev_data):
    """
    prev_data: list[1, 1.5, 1.2, 1.1, 1.7, ...]
    """
    prev_data = list(reversed(prev_data))
    prev_data = np.array(prev_data)
    fet = []

    fet.append([prev_data[x]-prev_data[x+1] for x in range(12)])
    
    years = [prev_data[x:x+4] for x in range(6)]
    fet.append([max(x) for x in years])
    fet.append([min(x) for x in years])
    fet.append([np.std(x) for x in years])
    fet.append([prev_data[0]-prev_data[-1], max(prev_data)-min(prev_data),
                np.mean([np.std(x) for x in years]), np.mean([np.max(x)-np.min(x) for x in years])])
    
    return np.concatenate(fet)


def make_features_quart_clas(prev_data):
    prev_data = list(reversed(prev_data))
    prev_data = np.array(prev_data)
    fet = []

    fet.append([prev_data[x]-prev_data[x+1] for x in range(24)])
    
    years = [prev_data[x:x+4] for x in range(6)]
    fet.append([max(x) for x in years])
    fet.append([min(x) for x in years])
    fet.append([np.std(x) for x in years])
    fet.append([prev_data[0]-prev_data[-1], max(prev_data)-min(prev_data),
                np.mean([np.std(x) for x in years]), np.mean([np.max(x)-np.min(x) for x in years])])
    
    return np.concatenate(fet)


def make_features_month_clas(prev_data):
    prev_data = list(reversed(prev_data))
    prev_data = np.array(prev_data)
    fet = []

    fet.append([prev_data[x]-prev_data[x+1] for x in range(36)])
    
    fet.append([
                np.min(prev_data[:11])-prev_data[-1], np.max(prev_data[:11])-prev_data[-1],
                prev_data[11]-prev_data[35], prev_data[11]-prev_data[35]
                ])
    
    years = [prev_data[x:x+12] for x in range(3)]
    fet.append([max(x) for x in years])
    fet.append([min(x) for x in years])
    fet.append([np.std(x) for x in years])
    fet.append([prev_data[0]-prev_data[-1], max(prev_data)-prev_data[0]])
    
    return np.concatenate(fet)


def make_features_month_reg(prev_data):
    prev_data = list(reversed(prev_data))
    prev_data = np.array(prev_data)
    fet = []

    fet.append([prev_data[11]-prev_data[x*12+11] for x in range(1, 3)])
    
    years = [prev_data[x:x+12] for x in range(3)]
    fet.append([max(x) - prev_data[0] for x in years])
    fet.append([prev_data[0] - min(x) for x in years])
    fet.append([np.std(x) for x in years])
    
    
    fet.append([prev_data[x]-prev_data[x+1] for x in range(12)])
    fet.append([prev_data[x]-prev_data[0] for x in range(1, 13)])
    
    fet.append([prev_data[11+x*12]-prev_data[12+x*12] for x in range(3)])
    
    fet.append([
                np.min(prev_data[:11])-prev_data[0], np.max(prev_data[:11])-prev_data[0],
                prev_data[11]-prev_data[35], prev_data[11]-prev_data[35]
                ])
    fet.append([max(x) for x in years])
    fet.append([min(x) for x in years])
    fet.append([np.std(x) for x in years])
    fet.append([prev_data[0]-prev_data[-1], max(prev_data)-min(prev_data),
                np.mean([np.std(x) for x in years]), np.mean([np.max(x)-np.min(x) for x in years])])
    fet.append([np.mean(years[0])-np.mean(years[1]), np.mean(years[0])-np.mean(years[2])])
    
    fet.append([prev_data[11]*2-prev_data[23]-prev_data[0]])

    return np.concatenate(fet)
