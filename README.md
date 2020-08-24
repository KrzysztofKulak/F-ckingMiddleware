# F-ckingMiddleware

F-ckingMiddleware is a Django middleware that alters the HTTP responses to insult both the user and the developer.

The insults will be added to errors and debug information:

![404 Not Found with swears](https://i.ibb.co/MMFtpPm/Annotation-2020-08-24-204546.png)

to generated views: 

![Hello world with swears](https://i.ibb.co/kgNpp6J/Annotation-2020-08-24-204802.png)

and in the JSON responses like:

`{"test_key": "test_value"}` into `{"test_key, you fucking idiot": "test_value, you fucking idiot"}`

### How to use

1. Copy `fuckingmiddleware.py` file into your middleware location.
1. Add the path of the copied file to the `MIDDLEWARE` array in settings file of your Django project.

### Swear word customization

The swear word used by default is `you fucking idiot`, but you can customize it by setting `FUCKING_MIDDLEWARE_SWEAR` variable in the settings file of your Django project to the desired phrase.

__IMPORTANT__: Don't use period sign nor `</h1>` tag in the phrase, because it will probably create infinite loop and crash your app (and, if we're lucky, create the black hole that will consume the universe).
