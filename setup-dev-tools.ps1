function Write-File {
    param (
        [string]$Path,
        [string]$Content
    )
    $Content | Set-Content -Encoding UTF8 $Path
    Write-Host "✅ $Path создан"
}

Write-Host "`n🚀 Настройка линтеров и форматтеров для Python-проекта..."

# .flake8
$flake8 = @"
[flake8]
max-line-length = 100
exclude = 
    venv,
    __pycache__,
    .git,
    .pytest_cache
"@
Write-File ".flake8" $flake8

# pyproject.toml
$pyproject = @"
[tool.black]
line-length = 100
target-version = ['py39']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | venv
  | __pycache__
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
line_length = 100
known_first_party = ["tests"]
skip = ["venv"]
"@
Write-File "pyproject.toml" $pyproject

# requirements-dev.txt
$requirements = @"
flake8
black
isort
pytest
pre-commit
"@
Write-File "requirements-dev.txt" $requirements

# .pre-commit-config.yaml
$precommit = @"
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
"@
Write-File ".pre-commit-config.yaml" $precommit

# Установка зависимостей
Write-Host "`n📦 Устанавливаем зависимости..."
pip install -r requirements-dev.txt

# Установка хуков
Write-Host "`n🪝 Устанавливаем git pre-commit hook..."
pre-commit install

Write-Host "`n🎉 Всё готово! Теперь при коммите твой код будет автоматически проверяться и форматироваться."