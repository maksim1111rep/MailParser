if [ ! -d "inbox" ]; then
    echo "Ошибка: папка с письмами не найдена"
    exit 1
fi
echo "Запуск приложения"
python3 -m MailParser -i inbox -o output -st
if [ $? -eq 0 ]; then
    echo "Приложение успешно завершило работу"
else
    echo "Что-то пошло не так"
fi