<h1 style="text-align: center;">Simple ToDo App</b></h1>
<h2 style="text-align: center; margin-bottom: 20px;">powered by <i>(Django 3, Vue.js, Axios and Bootstrap4)</i></h2>

<h3><b>О проекте:</b></h3>
<p>Простая реализация мини-приложения ToDo (без использования DRF).</p>
<p>Данное приложение позволяет создавать список задач, автоматически сортирующийся по созданию, помечать выполненные задания кликом, тем самым зачеркивая их, а также удалять созданные созданные задачи.</p>

<h3><b>Отработанные навыки:</b></h3>
<ul>
    <li>Основы Vue.js</li>
    <li>Отправка ajax-запросов с помощью Axios</li>
    <li>Обработка ajax-запросов в Django</li>
    <li>Bootsrap4</li>
</ul>

<h3><b>Установка:</b></h3>
<ol>
<li>Создание директории проекта:</li>

    mkdir VueToDo
    cd VueToDo
    git clone https://github.com/StepanovSerjant/Simple-ToDo-.git

<li>Создание и активация виртуального окружения:</li>

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pip list

<li>Запуск проекта

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

</li>
<p>Vue.js и Axios подключены в html файле через средства CDN, поэтому никаких дополнительных установок не требуется.</p>
<hr>
<p>Затем скопируйте адрес локального хостинга из командной строки и добавтьте к нему "/tasks".</p>
<p>По полученному в итоге адресу, например (http://127.0.0.1:8000/tasks), будет находится данное приложение.</p>
</ol>



