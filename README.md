# yandex_disk

## Методы и написанные на них тесты:

1. GET v1/disk/resources
   - Happy Path - 200
   - Не удалось найти запрошенный ресурс - 404
   - Неавторизованный пользователь - 401
2. POST v1/disk/recources/copy
   - Happy Path non async - 201
   - Happy Path async - 202
   - Копирование несуществующего файла - 404
   - Копия файла уже существует - 409
3. PUT v1/disk/recources
   - Happy Path - 201
   - Создание папки с существущим именем - 409
4. DELETE v1/disk/recources
   - Happy Path - 204
   - Happy Path async - 202
   - Happy Path с параметром permanently=true - 204
   - Удаление несуществующей директории - 404
5. PATCH v1/disk/resources
   - Happy Path - 200
   - InternalServerError - 500

## Что реализовано

1. Модульная структура: тесты, вспомогательные классы, конфигурация живут по-отдельности (возможность для масштабирования)
2. Используется фреймворк pytest и библиотека requests
3. Используется Allure: настроена генерация отвечтов и логирование запросов и ответов
4. Конфигурация окружения вынесена в переменные окружения (OAuth-token, base URL и др.), чувствительные данные не хранятся в репозитории
5. Атентификация реализована через OAuth-токен
6. Используется подход, аналогичный Page Object: поверх базового клиента выделены endpoint‑классы, инкапсулирующие логику работы с конкретными методами
7. Тесты, покрывающие статусы 2xx/4xx/5xx, корректное поведение при ошибках; проверка тела ответа: ключевые поля, типы, значения; негативные кейсы: невалидные параметры, отсутствующий ресурс, неверный токен; авторизация/аутентификация: с/без токена

## Что можно улучшить

1. Добавить мокирование данных с помощью unittest.mock или requests-mock для изоляции логики от внешнего сервиса в отдельных тестах
2. Добавить @pytest.mark.parametrize для проверки одного endpoint на множестве наборов данных (валидных и невалидных)
3. Добавить шаги в Allure по необходимости
4. Добавить валидацию структуры JSON (ключи, обязательные поля) с помощью pydantic/jsonschema

## Как запустить

```bash
1. Создать файл config/.env с содержимым:

API_TOKEN=<ваш OAuth-токен>

2. Установка

pip install -r requirements.txt

3. Запуск тестов

pytest

4. Запуск отчета

allure serve allure-results

```

## Результаты тестов локально

```bash
tests/v1_disk_recources/test_delete_sources.py::test_delete_file_to_trash_sync PASSED                                    [  6%]
tests/v1_disk_recources/test_delete_sources.py::test_delete_file_async PASSED                                            [ 13%]
tests/v1_disk_recources/test_delete_sources.py::test_delete_file_permanently PASSED                                      [ 20%]
tests/v1_disk_recources/test_delete_sources.py::test_delete_non_existing_resource PASSED                                 [ 26%]
tests/v1_disk_recources/test_get_disk_info.py::test_get_disk_info PASSED                                                 [ 33%]
tests/v1_disk_recources/test_get_disk_info.py::test_get_non_existing_resource PASSED                                     [ 40%]
tests/v1_disk_recources/test_get_disk_info.py::test_get_resource_unauthorized PASSED                                     [ 46%]
tests/v1_disk_recources/test_patch_sources.py::test_patch_source PASSED                                                  [ 53%]
tests/v1_disk_recources/test_patch_sources.py::test_patch_source_invalid_body PASSED                                     [ 60%]
tests/v1_disk_recources/test_post_copy.py::test_copy_file_async_success PASSED                                           [ 66%]
tests/v1_disk_recources/test_post_copy.py::test_copy_file_sync_success PASSED                                            [ 73%]
tests/v1_disk_recources/test_post_copy.py::test_copy_non_existing_source PASSED                                          [ 80%]
tests/v1_disk_recources/test_post_copy.py::test_copy_existing_destination PASSED                                         [ 86%]
tests/v1_disk_recources/test_put_folder.py::test_create_folder_success PASSED                                            [ 93%]
tests/v1_disk_recources/test_put_folder.py::test_create_existing_folder PASSED                                           [100%]

===================================================== 15 passed in 17.82s =====================================================
```

## Результаты Allure report локально

![allure report](/allure-report/allure.png)
