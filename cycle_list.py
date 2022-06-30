def cycle_list(object, times=None):
    # repeat([10,4], 3) --> 10 4 10 4 10 4
    length = len(object)
    if times is None:
        for i in count(0):
            yield object[i%length]
    else:
        for i in xrange(times):
            for j in range(length):
                yield object[j]