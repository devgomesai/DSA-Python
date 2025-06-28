def recursive_call(counter=1):
    if counter == 10:
        return
    else:
        print(counter)
        recursive_call(counter=counter + 1)
recursive_call()