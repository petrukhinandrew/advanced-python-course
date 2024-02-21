# ДЗ 1. 3/3. 

Решения находятся в файлах `nl.py`, `tail.py`, `wc.py` соответственно. 

## Формат артефактов 

```text
[cmd]
[stdout]
```
где `[cmd]` - команда для запуска, `[stdout]` - вывод программы 

Если программа запускалась без файлов (с `stdin`), артефакты (заканчиваются на `_stdin.txt` соответственно) будут иметь вид 
```text
[cmd]
[stdout]
with input:
[stdin]
```
где `[stdin]` - stdin соответственно

## Генерация артефактов

По сути, прокси для запуска решений. Для запуска `artifacts_gen.py`: `python3 artifacts_gen.py [out_spec] [task_name] [task_args]`, где 
- `[out_spec]` - это добавка к названию артефакта 
- `[task_name]` - одно из `nl.py`, `tail.py`, `wc.py`
- `[task_args]` - аргументы, с которым будет запущен `[task_name]`

**Пример**: 
```bash
python3 artifacts_gen.py test01 wc.py test_files/test1.txt
``` 
**Вывод `artifacts/wc_test01.txt`**: 
```text 
python3 .\wc.py .\test_files\test1.txt .\test_files\test1.txt
3 6 6 .\test_files\test1.txt
3 6 6 .\test_files\test1.txt
6 12 12 total
```