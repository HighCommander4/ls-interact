.PHONY: bear
bear:
	bear -a make program

program: first.o second.o
	c++ $^ -o $@

%.o: ../src/%.cpp
	c++ -c $< -o $@ -g3 -O0 -DBUILD=2

.PHONY: clean
clean:
	rm -f *.o program compile_commands.json
