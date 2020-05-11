Create .env file and add following setting

```
DEBUG=on
SECRET_KEY=your-secret-key
DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
SQLITE_URL=sqlite:///db.sqlite
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
```
