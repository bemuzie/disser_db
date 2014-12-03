def sensor_dump(locking_range, dump_strength, n):
    stacking = [1, .87, .57, .28, .105, .03]
    dumping = 1
    for i in range(n):
        print dumping * locking_range
        dumping *= 1 - dump_strength * stacking[i]
    return dumping * locking_range


print sensor_dump(50, 0.417, 4)
		
