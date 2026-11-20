demo: ../../../templates/demo.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -std=c17 -Wall -Wextra -g -O0 $< $(LDFLAGS) -o $@

.PHONY: check
check: demo
	python3 ukur.py
