from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
PAYMENT_TOKEN = env.str("PAYMENT_TOKEN")
currency = env.str("currency")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
dbUSER = env.str("dbUSER")
dbPASSWORD = env.str("dbPASSWORD")
DATABASE = env.str("DATABASE")

works = {"Курсовая": {
    "description": "Информация о курсовой\n Цена от 3000 р.",
    "template": "Шаблон для курсовой\n***********\n*************\n**********\nНапишите вашу заявку соответственно шаблону:"
},
    "Дипломная": {
        "description": "Информация о дипломной работе\n Цена от 2000 р.",
        "template": "Шаблон для дипломной\n***********\n*************\n**********\nНапишите вашу заявку соответственно шаблону:"
    },
    "Печать":
        {
            "description": "Описание для печать\nЦена от 1000 р.",
            "template": "Шаблон для печати работ\n***********\n*************\n**********\nНапишите вашу заявку соответственно шаблону:"
        }
}

message = {
    "About_Us": "Текст для информации \"о нас\"",
    "Product_Menu": "Товары",
    "Main_Menu": "Главное меню",
    "Welcome_Menu": "Тут сообщение приветствия",
    "product_info": "Предмет: {item_name}\nОписание: {description}\nЦена: {price}",
    "code_missing": "Данного промокода нет",
    "comment_order": "Оставьте коментарий к заказу: ",
    "comment_documentCheck": "Есть дополнительный файл?",
    "comment_document": "Прикрепите файл, если у вас несколько файлов добавьте архив:",
    "comment_promoCodeCheck": "У вас есть промокод?",
    "comment_promoCode": "Введите промокод:",
    "promoCode_confirmation": "Ваш промокод:\nНазвание: {name}\nСкидка: {discount}",
    "document_confirmation": "Ваш документ:\n{text}",
    "comment_confirmation": "Ваш текст:\n{text}",
    "comment_confirmation_yes": "<b>Оплата прошла</b>, ваша заявка отправлена на выполнения, ожидайте",
    "comment_confirmation_no": "Повторите:",
    "product_missing": "Извените, но данный товар больше нельзя заказать",
    "message_sent": "Сообщение отправллено администрации",
    "message_no": "Напишите свое сообщение ещё раз: ",
    "message_cancel": "Отправка сообщения администрации отменена.",
    "order_complete": "<b>Вам сообщение от администратора</b> по поводу вашего заказа:",
    "order_close": "Ваш <b>заказ был выполнен</b> и закрыт"
}

adminMessage = {
    "help": "/orderspr - Все заявки в расмотрение\n/infopr orderProID - Подробная информация о заказе на рассмотрении\n/sendr orderProID - отправить форму оплаты\n/closer orderProID - Отказать в заказе"
            "/orders - Выведет все заказы\n/info orderID - Информация о заказе\n/orderClose orderID - Закрыт заказ\n/send orderID - Начать ввод сообщений для отправки заказчику\n"
            "/codeList - Список всех промокодов\n/codeAdd - Начать создание новго промокода\n/codeEdit codeID - Изменить промокод\n/ordermes or /allmes - Просмотреть все входящие сообщения\n"
            "/mesinfo mesID - Информаци о входящем сообщение\n/usend mesID - Отправить сообщение в ответ",
    "ordersPR_main": "Список заказов:\n{text}\n/infopr orderProID - Подробная информация о заказе на рассмотрении\n/sendr orderProID - отправить форму оплаты\n/closer orderProID - Отказать в заказе",
    "orders_main": "Список заказов:\n{text}\n/info orderID - Информация о заказе\n/orderClose orderID - Закрыт заказ\n/send orderID - Начать ввод сообщений для отправки заказчику",
    "orders_missing": "Заказов нет",
    "order_missing": "Данного заказа нет",
    "order_completed": "Данный заказ уже выполнен",
    "order_confirm": "Закрыть заказ?\n(Отправить ответ на заказ надо перед закрытием)",
    "order_confirm_no": "Закрытие заказа отменено",
    "order_close": "Закак с ID <b>{id}</b> был закрыт",
    "order_info": "{num}. Номер заказа <b>{orderID}</b> от {date}\n",
    "order_detailed_info": "Номер заказа <b>{orderID}</b>\nОплата: {price}\nКоментарий к заказу: {description}\nДата заказа: {date}\n",
    "order_close_text": "Напишите текст для отказа:",
    "order_close_confirm": "Отправить отказ?",

    "message_send": "Напишите сообщение для пользователя",
    "message_send_confirmation": "Проверить сообщение /mesCheck\nОтправить сообщение?",
    "message_yes_send": "Сообщение успешно отправленно пользователю",
    "message_not_send": "Отправка сообщения отменена",
    "price_send": "Напишите сумму оплаты",
    "document_add": "Документ добавлен",
    "img_add": "Изображение добавлено",
    "mes_add": "Сообщение добавлено",

    "code_main": "Список промокодов:\n{text}\n/codeAdd - Начать создание новго промокода\n/codeEdit codeID - Изменить промокод",
    "codes_missing": "Промокодов нет",
    "code_missing": "Данного промокода нет",
    "code_info": "{num}. ID прмокода <b>{id}</b>\nНазвание: {name}\nСкидка: {discount}\n\n",
    "code_edit": "/name: {name}\n/code: {code}\n/type: {typeD}\n/discount: {discount}\nУдалить промокод /delete\nОтменить изменения /back\n",
    "code_add_name": "Укажите название:",
    "code_add_code": "Напишете промокод:",
    "code_add_percent": "Скидка в процентах или суммой(1-сумма,2-процент):",
    "code_add_discount": "Укажите скидку(число):",
    "code_add_confirmation": "Правильно?",
    "code_add_repeat": "Повторите: ",
    "code_add_cancel": "Создание промокода отменено",
    "code_edit_back": "Меню изменений промокода закрыто",
    "code_del_yes": "Промокод удален",
    "code_del_no": "Удаление прмокода отменено",

    "messages_missing": "Сообщений нет",
    "message_missing": "Данного сообщения нет",
    "messages_info": "{num}. Номер сообщения <b>{id}</b> от {date}\n",
    "message_detailed_info": "Номер сообщения <b>{id}</b>\nТекст: {text}\nДата отправки: {date}\n",
    "message_completed": "На данное сообщение уже ответили",
    "message_cancel": "Отправка сообщения пользователю отменена",
    "messages_main_order": "Список сообщений от покупателей:\n",
    "messages_main_all": "Список сообщений от обычныйх пользователей:\n",

    "order_pr_detailed_info": "Номер заказа <b>{orderID}</b>\nТекст заявки:\n{text}\nСкидка: {discount}\nДата заказа: {date}\n",
    "price_confirmation": "Отправить форму оплаты?",
    "admin_mes_order_provisional": "<b>Новый</b> заказ, нужно его рассмотреть и дать хорошую цену ; )\n/orderspr",
    "admin_mes_order_paid": "<b>Оплачен</b> новый заказа, надо бы его сделать\n/orders",

    "departments_missing": "Отделов нет",
    "department_missing": "Данный отдел не существует",
    "departments_main": "Отделы:\n{text}\nКоманды:",
    "department_info": "{num}. Название отдела: {name}\nТэг: @{tag}\nКоличество сотрудников: {count_staff}\n\n",
    "department_detailed_info": "Название отдела: {name}\nТэг: @{tag}\nСотрудники: {count_staff}",
    "department_add_name": "Укажите название отдела",
    "department_add_tag": "Укажите тэг для отдела(Пример: admin)",
    "department_add_user": "Укажите ID пользователя что добавить его",
    "department_del_user": "Укажите ID пользователя что удалить его",
    "department_edit": "/name: {name}\n/tag: @{tag}\n/add_user Добавить сотрудника\n/del_user Удалить сотрудника\nУдалить отдел /delete\nОтменить изменения /back\n",
    "department_edit_no": "Изменение отменено",
    "department_edit_back": "Меню изменений отдела закрыто",
    "department_del_yes": "Отдел удален",
    "department_del_no": "Удаление отдела отменено",
}

payMessage = {
    "title": "Заказ услуги",
    "description": "Тут нужно будет прописать описание"
}

errorMessage = {
    "not_add_photo": "Если вы хотете прикрепить фото добавьте его например в архив и отправтье",
    "exceeded_time_pay": "Вы пытаетесь оплатить старый товар. Для вашей же безопасности повторите заказ.",
    "payment_missing": "Произашла ошибка, ваш заказ скорее всего потерян. Свяжитесь с администрацией бота /ames"
}
