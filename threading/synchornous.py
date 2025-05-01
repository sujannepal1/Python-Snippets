import time

start = time.perf_counter()


def do_sth():
    print("Sleeping")
    time.sleep(1)
    print("Done Sleeping...")


do_sth()
do_sth()


finish = time.perf_counter()

print(f"Finished in {round(finish - start)}")
