# Mozhna — Privacy Policy

_Last updated: November 10, 2026_

Mozhna ("the app", "we") answers one question: how much money you can safely spend until your next income. This policy explains what data the app handles and why.

In short: **without an account, everything stays on your phone.** An account is optional. You need one only for the AI that reads your phrases and for sync between your phones. You can delete it in the app at any time.

## Without an account
The app works fully offline. On the device, in a local database, it keeps:

- your accounts (name, type, currency, opening balance) and transactions (amount, date, merchant, note, category);
- regular payments and savings goals;
- settings (simple or full mode, guidance, language, theme, main currency);
- a random local identifier. It is not linked to you and is not sent anywhere.

Nothing of this leaves the phone, unless you back up your phone with Apple or Google.

## With an account (optional)
You can sign in with Apple, with Google or with an e-mail and password. Sign-in is handled by **Google Firebase Authentication**.

**What we store:**
- your e-mail address;
- your name, if Apple or Google passes it;
- a user ID.

If you use Sign in with Apple and hide your e-mail, we only get Apple's relay address.

**Sync.** While you are signed in, your records (accounts, transactions, categories, regular payments, goals, limits and the settings named above) are copied to our server, so they are the same on all your phones. The server is run by the developer for this app only.

**AI ("Parse with AI").** When you tap this button, the phrase you typed is sent to our server, for example "coffee 85 and cake 40". With it go today's date, the language, your main currency and the names of your categories. Our server passes them to **Google Gemini**, which returns the amount, merchant and category, and you check the result before saving.

Your e-mail and user ID are not sent to Google with the phrase. Our server keeps a daily count of AI requests per account, to keep costs within limits. We do not keep the phrases themselves after answering. Google processes them under the [Gemini API terms](https://ai.google.dev/gemini-api/terms) and, on our paid plan, does not use them to improve its models.

## Bank import (optional, monobank)
If you connect monobank, the app uses the personal token you create at api.monobank.ua. It loads your statement **directly from monobank to your phone**, read-only: the app cannot move money.

The token stays only on your phone, in the system keychain, and is never sent to our server. If you are signed in, the imported transactions sync like the ones you type.

## What the app does not do
- No ads, no analytics, no crash reporting, no advertising identifiers
- No tracking across other apps or websites
- We do not sell or share your data. Others receive data only to provide the features above: Google Firebase (sign-in), Google Gemini (only the phrases you send to AI), monobank (only when you connect it).
- No access to contacts, location, microphone or camera in this version

## Deleting your data
- **Without an account:** delete any record in the app, or delete the app.
- **With an account:** Profile → "Delete account". This deletes everything the account keeps on our server and the account itself; for Sign in with Apple, the app also revokes its Apple sign-in. You can also remove the records from the phone in the same step.
- Signing out keeps the records on the phone and on the server.

You can also write to us and we will delete your account by hand.

## Children
Mozhna is not directed at children under 13, and we do not knowingly collect personal information from them.

## Financial information
The app shows a calculation based on the numbers you enter or import. It is not financial advice.

## Changes
This policy may change. The date at the top shows the current version. We will update it before a new feature sends data anywhere new.

## Contact
mobile.support@zhukovskyi.space

---

# Можна — Політика конфіденційності

_Остання зміна: 10 листопада 2026_

«Можна» відповідає на одне питання: скільки грошей можна безпечно витратити до наступного доходу. Тут пояснено, з якими даними працює застосунок і навіщо.

Коротко: **без акаунта все залишається на вашому телефоні.** Акаунт не обов'язковий. Він потрібен лише для ШІ, який розбирає ваші фрази, і для синхронізації між вашими телефонами. Видалити його можна будь-коли в застосунку.

## Без акаунта
Застосунок повністю працює без інтернету. На пристрої, у локальній базі даних, зберігаються:

- ваші рахунки (назва, тип, валюта, початковий баланс) і операції (сума, дата, назва, нотатка, категорія);
- регулярні платежі й цілі;
- налаштування (простий чи повний режим, підказки, мова, тема, основна валюта);
- випадковий локальний ідентифікатор. Він не пов'язаний з вами і нікуди не передається.

Ніщо з цього не залишає телефон, хіба що ви робите резервну копію телефона в Apple чи Google.

## З акаунтом (за бажанням)
Увійти можна через Apple, через Google або поштою з паролем. Вхід забезпечує **Google Firebase Authentication**.

**Що ми зберігаємо:**
- адресу пошти;
- ім'я, якщо його передасть Apple чи Google;
- ідентифікатор користувача.

Якщо через Apple ви приховали пошту, ми бачимо лише адресу-посередника Apple.

**Синхронізація.** Поки ви в акаунті, ваші записи (рахунки, операції, категорії, регулярні платежі, цілі, ліміти й названі вище налаштування) копіюються на наш сервер, щоб вони були однакові на всіх ваших телефонах. Сервер веде розробник лише для цього застосунку.

**ШІ («Розібрати з ШІ»).** Коли ви натискаєте цю кнопку, введена фраза йде на наш сервер, наприклад «кава 85 і тортик 40». Разом із нею йдуть сьогоднішня дата, мова, основна валюта й назви ваших категорій. Наш сервер передає їх **Google Gemini**, який повертає суму, назву й категорію, а ви перевіряєте результат перед збереженням.

Вашу пошту й ідентифікатор разом із фразою в Google не передаємо. Наш сервер рахує кількість запитів до ШІ за день для кожного акаунта, щоб тримати витрати в межах. Самі фрази після відповіді ми не зберігаємо. Google обробляє їх за [умовами Gemini API](https://ai.google.dev/gemini-api/terms) і на нашому платному тарифі не використовує їх для покращення своїх моделей.

## Імпорт з банку (за бажанням, monobank)
Якщо ви підключаєте monobank, застосунок використовує особистий токен, який ви створюєте на api.monobank.ua. Він завантажує виписку **напряму з monobank на ваш телефон** і лише читає її: рухати гроші застосунок не може.

Токен лишається тільки на телефоні, у системному сховищі ключів, і ніколи не йде на наш сервер. Якщо ви в акаунті, завантажені операції синхронізуються, як і ті, що ви вносите самі.

## Чого застосунок не робить
- Немає реклами, аналітики, звітів про збої, рекламних ідентифікаторів
- Немає відстеження в інших застосунках чи на сайтах
- Ми не продаємо й не передаємо ваші дані. Інші отримують дані лише для роботи описаних вище функцій: Google Firebase (вхід), Google Gemini (тільки фрази, які ви надсилаєте ШІ), monobank (тільки коли ви його підключили).
- У цій версії немає доступу до контактів, геолокації, мікрофона чи камери

## Видалення даних
- **Без акаунта:** видаліть будь-який запис у застосунку або сам застосунок.
- **З акаунтом:** Профіль → «Видалити акаунт». Це видаляє все, що акаунт зберігає на нашому сервері, і сам акаунт; для входу через Apple застосунок також відкликає вхід в Apple. Тим самим кроком можна стерти й записи з телефону.
- Вихід з акаунта залишає записи і на телефоні, і на сервері.

Також можна написати нам, і ми видалимо акаунт вручну.

## Діти
Застосунок не призначений для дітей до 13 років, і ми свідомо не збираємо їхніх персональних даних.

## Фінансова інформація
Застосунок показує розрахунок на основі чисел, які ви ввели або завантажили. Це не фінансова порада.

## Зміни
Політика може оновлюватись. Дата вгорі показує актуальну версію. Ми оновимо її до того, як нова функція почне кудись передавати дані.

## Контакт
mobile.support@zhukovskyi.space
