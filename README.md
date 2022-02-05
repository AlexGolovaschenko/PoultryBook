# PoultryBook
### A web-service for collect data about poultry livestock on the farm

---

#### Сервис для внесения и хранения данных о процессе выращивания птицы.

#### ПОЛЬЗОВАТЕЛИ И ФУНКЦИИ СЕРВИСА
Пользователи: Птичевод, Зоотехник, Инженер КИП, Бригадир площадки, Ветеринар.
Пользователи могут вносить следующую информацию:
- номер птичника, для которого относятся вносимые данные
- информация о изменении численности птицы (поголовье, падеж, изьятие или добавление птицы)
- информация о поголовьи (средний вес, однородность)
- информация о потреблении воды, корма
- информация о микроклимате (температура, влажность в помещении, концентрация СО2, NH3)
- информация о выполнении ремонтных работ на площадке (осмотр, замена, ремонт оборудования)
- информация о выполнении ветеринарных процедур (выпойка, вакцинация, выявленные болезни, лечение)

Так же пользователи имеют возможность просмотра ранее внесенной информации, и редоктирования её.

#### ИНФОРМАЦИЯ О ПРОЕКТЕ DJANGO
Структура проекта Djungo:
- модуль base содержит основные стили и шаблоны html-страниц, и страницы общего назначения (главная, справка, контакты и т.п.)
- модуль poultry_statistics содержит модели и вью для внесения и обработки данных о птице и микроклимте
- модуль service_statistics содержит модели и вью для внесения и обработки данных о выполнении ремонтных работ на площадке
- модуль vet_statistics содержит модули и вью для внесения и обработки данных о выполнении ветеринарных процедур
- модуль logbook содержит модели для организации записей о внесенной пользователями информации
