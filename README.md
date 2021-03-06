# Практические задания на Midterm

> **Disclaimer:**
>
> Если вы не прочитаете этот файл целиком, а потом окажется, что из-за этого у вас меньше баллов, чем вы ожидали,
> вы сами виноваты, ничего не поделать :(
>
> Я надеюсь, что задания адекватные по сложности... Можно пользоваться интернет-ресурсами, документацией питона,
> чем-нибудь еще, только не надо решать вместе в этот раз, мы честно хотим понять насколько у всех все хорошо или плохо
> с такими заданиями.
>
> Всем удачи!

## Правила

1. Всего можно набрать до *10 баллов*. Баллы свыше набранных десяти учитываться как бонус не будут

2. Каждое задание блока [`easy`](easy) по умолчанию стоит *2 балла*, каждое задание блока [`hard`](hard) &ndash; *5
   баллов*

3. &laquo;Простыми&raquo; заданиями можно набрать не более *8 баллов*. То есть на оценку хотя бы 9/10 надо сделать хотя
   бы одно &laquo;сложное&raquo;

4. **Спустя час** после создания репозитория **стоимость заданий уменьшается в 2 раза**

5. **Спустя два часа** после создания репозитория **стоимость заданий падает до 0**

---

Вам выдается ваш личный _вариант_ задания. Это означает следующее &ndash; _задания вашего варианта стоят свой полный
балл_, задания вне вашего варианта стоят ровно половину: `easy` &ndash; _1 баллл_, `hard` &ndash; _2.5 балла_.

Сгенерируйте свой вариант. Перед этим убедитесь, что корневая папка вашего проекта называется
`assignment-midterm-ваш-никнейм`, иначе у нас с вами будут разные представления о вариантах.

Для этого запустите файл `init.py`, который лежит в корне этого проекта. Сам вариант будет лежать в
файле [`.variant`](.variant).

## Сдача

Процесс сдачи заданий ничем не отличается от первой практики, только еще и не надо со.

Протестировать свой код локально можно, просто запустив файл с заданием (`Ctrl + Shift + F10`), либо вызывав `pytest` из
консоли:

```shell
pytest easy/TASKNAME
  [или]
pytest hard/TASKNAME
```

Если все тесты пройдены, можно спокойно запушить сделанное задание на GitHub. Пушьте задания как только их решаете,
потому что спустя час их стоимость падает в два раза (см. правила)!

```shell
git add .
git commit -m "<напишите здесь что-нибудь осмысленное>"
git push origin main
```

Было подключено обратно автоматическое тестирование на GitHub. Проверьте, что после команды `git push` во
вкладке `Actions` на GitHub запустились тесты ровно к тем заданиям, которые вы сделали. Тестироваться на GitHub после
каждого пуша будут только те задания, файлы с которыми были изменены.

# FAQ

> Q: _Не могу запушить, что делать?_
>
> A: Включить обратно интернет, в этом репозитории не должно быть других проблем с доступом.

> Q: _Где я могу посмотреть свои набранные баллы с учтом варианта?_
>
> A: Нигде :) Потом проставятся в табличку, пока считайте сами, вроде должно быть не так уж сложно.

> Q: _Достался сложный вариант, это нечестно_
>
> A: Варианты похожи на билеты на экзамене &ndash; чистая случайность, только в этот раз зависящая от имени. Плюсы
> относительно билетов на экзамене: можно за частичный балл сдавать и остальные задания, так что не жалуйтесь,
> пожалуйста, я старался сделать систему лайтовой :(
