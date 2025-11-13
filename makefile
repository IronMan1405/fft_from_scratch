CC=clang
FLAGS=-Wall -std=c23 -O3

DEPENDENCIES := obj/main.o

fft_c_test: $(DEPENDENCIES)
	$(CC) $(FLAGS) -lm $(DEPENDENCIES) -o fft_c_test

# Object files.
obj/main.o: src/main.c
	$(CC) -c $(FLAGS) src/main.c -o obj/main.o

# Clean
clean:
	rm -rf obj fft_c_test

$(shell mkdir -p obj)
