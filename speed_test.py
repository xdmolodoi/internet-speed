import time
import requests

URL = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"  # ~14 МБ
REQUESTS_COUNT = 10


def test_speed(url: str, count: int) -> None:
    total_bytes = 0
    total_time = 0.0
    successful = 0

    for i in range(1, count + 1):
        start = time.perf_counter()
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Запрос {i}: ошибка — {e}")
            continue
        elapsed = time.perf_counter() - start

        size = len(response.content)
        total_bytes += size
        total_time += elapsed
        successful += 1
        print(f"Запрос {i}: {size / 1_048_576:.2f} МБ за {elapsed:.2f} с")

    if successful == 0:
        print("Все запросы не удались.")
        return

    avg_time = total_time / successful
    total_mb = total_bytes / 1_048_576
    speed_mbps = total_mb / total_time

    print("\n--- Результат ---")
    print(f"Успешных запросов: {successful} из {count}")
    print(f"Среднее время запроса: {avg_time:.2f} с")
    print(f"Всего скачано: {total_mb:.2f} МБ")
    print(f"Скорость: {speed_mbps:.2f} МБ/с")


if __name__ == "__main__":
    test_speed(URL, REQUESTS_COUNT)
