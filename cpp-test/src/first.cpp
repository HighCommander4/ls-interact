#include "first.h"
#include "second.h"

#if BUILD == 1
#warning "This is build 1"
#elif BUILD == 2
#warning "This is build 2"
#endif


static void foo()
{
  bob();
}

int main()
{
  bar();
  foo();
}

struct Base {};
struct Derived : Base {};

// Test clang-tidy integration.
void clangTidyTest(int i) {
  // Should trigger 'bugprone-integer-division'.
  double d = 32 * 8 / (2 + i);
}
