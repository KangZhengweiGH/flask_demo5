broker_url = 'redis://localhost:6379'
result_backend = 'redis://localhost:6379'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
imports = ("app.main.task",)
