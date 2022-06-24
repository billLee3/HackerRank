candles = [4, 4, 1, 3, 4]

def birthdayCakeCandles(candles):
    candles.sort()

    candles_count = 0
    for i in candles:
        if i == candles[(len(candles)-1)]:
            candles_count += 1
    return candles_count

birthdayCakeCandles(candles)