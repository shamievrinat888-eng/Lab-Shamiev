import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    filename='deposit.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Ввод данных
    deposit = float(input("Введите сумму вклада: "))
    rate = float(input("Введите годовую ставку (%): "))
    years = int(input("Введите срок вклада (в годах): "))

    # Проверка корректности
    if deposit <= 0 or rate <= 0 or years <= 0:
        raise ValueError("Все значения должны быть положительными.")

    # Расчёт сложных процентов
    final_amount = deposit * ((1 + rate / 100) ** years)

    # Вывод результата
    print(f"\nИтоговая сумма через {years} лет: {final_amount:.2f} тенге")
    print("Работа программы завершена.\n")

    print(f"Вклад: {deposit:.0f} тг")
    print(f"Ставка: {rate:.1f}%")
    print(f"Срок: {years} лет")
    print(f"Итоговая сумма: {final_amount:.2f} тг\n")

except ValueError as e:
    logging.error(f"Ошибка при расчете: {e}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]} - ERROR - Ошибка при расчете: {e}")
