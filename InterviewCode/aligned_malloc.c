// Jun 18th, 2022 with Apple, Embedded SWE, with Jung-Hoon Shin

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//  |.      |.      |.      |.      |
/// |    |. |void * |

void *mem_align_alloc(int mem_size, int align_size) {
  // malloc()
      void * raw_ptr;
      void * real_ptr;

      raw_ptr = malloc(mem_size + sizeof(void *) + align_size);

      int align = (long)(raw_ptr) % align_size;

      real_ptr = (raw_ptr + (align_size - align)) + sizeof(void *);
      memcpy((raw_ptr + (align_size - align)), &real_ptr, sizeof(void *));

      return real_ptr;
}

void mem_align_free(void *ptr) {

    void * raw;
    memcpy(&raw, ((void *)(ptr - sizeof(void *))), sizeof(void *));
    free(raw);
}

// Main function
int main()
{
    /* 123 bytes memory allocation aligned with 32 bytes. */
    char *ptr = mem_align_alloc(123, 32);

    strcpy(ptr, "I love my work!");
    printf("%p: %s\n", ptr, ptr);

    mem_align_free(ptr);

    return 0;
}