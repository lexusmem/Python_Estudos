def countApplesAndOranges(s, t, a, b, apples, oranges):

    # inicio_samhouse = s
    # fim_samhouse = t
    # local_appletree = a
    # local_orangetree = b
    # locais_apples = apples
    # locais_oranges = oranges

    conta_apples = 0
    conta_oranges = 0

    for apple in apples:
        local = (a + (apple))
        if local >= s and local <= t:
            conta_apples += 1

    for orange in oranges:
        local = (b + (orange))
        if local >= s and local <= t:
            conta_oranges += 1

    return print(conta_apples), print(conta_oranges)


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
