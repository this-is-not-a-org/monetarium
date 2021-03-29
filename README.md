# monetarium

## How to start:

- install dependences:
```pipenv install --dev```

- create .env file with:
```python contrib/make_env.py```

- .env variables:
| name | default | type |
| ---- | ------- | ---- |
| SECRET_KEY | generate random string | string |
| DEBUG | False | boolean |
| DEVELOPMENT | False | boolean |
| ADMIN_ENABLED | False | boolean |
| DATABASE_URL | postgres://username:password@address:port/monetarium | string |
| LANGUAGE_CODE | pt-br | string |
| TIME_ZONE | UTC | string |
| USE_I18N | True | boolean |
| USE_L10N | True | boolean |
| ALLOWED_HOSTS | localhost, 0.0.0.0, 127.0.0.1 | string |

