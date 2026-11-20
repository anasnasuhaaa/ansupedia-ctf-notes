CFLAGS += -std=c17 -g -O0 -fno-omit-frame-pointer -Wall -Wextra
SOURCE ?= program.c
CASES ?= kasus.json

program: $(SOURCE)
	$(CC) $(CPPFLAGS) $(CFLAGS) $< $(LDFLAGS) -o $@

.PHONY: check
check: program
	python3 ../../periksa.py $(CASES)
