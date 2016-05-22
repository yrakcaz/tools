CXX=g++
CXXFLAGS=-Wall -Wextra -Werror -pedantic -std=c++14 -fPIC
LDFLAGS=-shared
ARFLAGS=rcs

SRC=args.cc
OBJ=$(SRC:.cc=.o)

LIBS=libargs.a libargs.so
INCS=args.hh
PREFIX=/usr/local

CP=cp

all: $(LIBS)
.PHONY: all

libargs.a: $(OBJ)
	$(AR) $(ARFLAGS) $@ $^

libargs.so: $(OBJ)
	$(CXX) $(LDFLAGS) $^ -o $@

%.o: %.cc
	$(CXX) $(CXXFLAGS) -c -o $@ $<

install:
	$(CP) $(LIBS) $(PREFIX)/lib
	$(CP) $(INCS) $(PREFIX)/include
.PHONY: install

uninstall:
	$(foreach lib,$(LIBS),$(RM) $(PREFIX)/lib/$(lib))
	$(foreach inc,$(INCS),$(RM) $(PREFIX)/include/$(inc))
.PHONY: uninstall

clean:
	$(RM) -f *.o *.a *.so
.PHONY: clean
