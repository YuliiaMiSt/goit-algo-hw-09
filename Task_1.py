import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """Жадібний алгоритм для видачі решти"""
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    """Алгоритм динамічного програмування для мінімізації кількості монет"""
    # Ініціалізуємо масив для збереження мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Збережемо використовувані номінали для формування суми
    coin_used = [0] * (amount + 1)

    # Заповнюємо dp-масив
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Якщо мінімальна кількість монет для потрібної суми — нескінченність, видача неможлива
    if dp[amount] == float('inf'):
        return None

    # Формуємо результат на основі масиву використаних монет
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Тестування функцій
amount = 113

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print("Жадібний алгоритм:", greedy_result, f"Час виконання: {greedy_time:.6f} секунд")
print("Алгоритм динамічного програмування:", dp_result, f"Час виконання: {dp_time:.6f} секунд")
