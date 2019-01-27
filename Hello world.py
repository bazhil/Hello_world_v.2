import logging
import datetime
print('write something. For example \'hello world\'')

text = input()

def text_print(text):
    """
    Бессмысленная функция в которой используются некоторые методы строк и действия пользователя логируются. Всяко лучше, чем просто print('Hello world')!
    :param text: текст, который вводит пользователь
    :return:
    """
    logging.basicConfig(filename='hello_world_log.log', level=logging.INFO)
    logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь запустил код \'Hello world\'')

    if len(text) == 0:
        try:
            print('Message cannot be empty!')
            logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь ввел пустую строку')
        except:
            pass
    elif text.find('i like python 3') > -1:
        try:
            print('It\'s so great!')
            logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь любит язык программирования Python 3')
        except:
            pass
    elif text.rfind('wow') > -1:
        print('Future will be greatest!')
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь удивлен')
    elif 'good' in text:
        try:
            text_words = text.split(' ')
            print('слово good стоит на', text_words.index('good') + 1, 'месте в предложении')
            logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь ввел текст со словом \'good\'')
        except:
            print('в строке 40-41 что-то не работает')
            pass
    elif 'i hate python 3' in text:
        print(text.replace('hate', 'love'))
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь хотел сказать что ненавидит Python')
    elif 'fuck python 3' in text:
        print(text.replace('fuck', 'love'))
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь хотел сказать что-то плохое про Python')
    elif text.lower() == 'hello world':
        print('Hello!')
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь написал \'hello world\'')
    elif text.isdigit() or text.replace(' ', '').isdigit():
        print('Human language please')
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь ввел какие-то цифры')
    else:
        print('Привет, Мир!')
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь осуществил произвольный ввод на который установлен ответ по умолчанию')
    print('Попробовал методы строк? То ли еще будет!')
    logging.info(str(datetime.datetime.today()) + ' ' + 'Код \'Hello world\' завершил свою работу')

text_print(text)