import GPUtil
from tabulate import tabulate
import time
import os

while True:
    # Универсальная очистка экрана для Windows и Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

    gpus = GPUtil.getGPUs()
    list_gpus = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} C"
        gpu_uuid = gpu.uuid

        list_gpus.append(
            (gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature, gpu_uuid))

    print(tabulate(list_gpus,
                   headers=["ID", "Название", "Загрузка", "Свободная память", "Используемая память", "Общая память",
                            "Температура", "UUID"]))

    time.sleep(2)  # Обновление каждые 2 секунды