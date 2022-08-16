#include <stdio.h>
#include <stddef.h>

typedef struct __LinkedList__{
  unsigned int value;
  void * next;
} LinkedList;
// To execute C, please define "int main()"

void print_linkedlist(LinkedList * head)
{

  while (head) {

    printf("%d -> ", head->value);
    head = head->next;

  }

  printf("NULL\n");

}

void reorder(LinkedList ** head)
{
    LinkedList * temp = *head;

    if ( temp == NULL || temp->next == NULL) {
      return;
    }

    LinkedList dummy_odd;
    LinkedList dummy_even;

    LinkedList * dummy_odd_tail = &dummy_odd;
    LinkedList * dummy_even_tail = &dummy_even;

    while (temp)
    {
      // Check even number w/o using division
      if ((temp->value >> 1) << 1 == temp->value)
      //if (temp->value % 2 == 0)
      {
        dummy_even_tail->next = temp;
        dummy_even_tail = dummy_even_tail->next;
      }
      else
      {
        dummy_odd_tail->next = temp;
        dummy_odd_tail = dummy_odd_tail->next;
      }

      temp = temp->next;
    }

    dummy_odd_tail->next = NULL;
    dummy_even_tail->next = NULL;

    //print_linkedlist(dummy_odd.next);
    //print_linkedlist(dummy_even.next);

    dummy_even_tail->next = dummy_odd.next;

    //print_linkedlist(dummy_even.next);


    *head = (void *)dummy_even.next;

}



int main() {
  LinkedList n0;
  LinkedList n1;
  LinkedList n2;
  LinkedList n3;
  LinkedList n4;
  LinkedList n5;

  n0.next = &n1;
  n1.next = &n2;
  n2.next = &n3;
  n3.next = &n4;
  n4.next = &n5;
  n5.next = NULL;

  n0.value = 3;
  n1.value = 6;
  n2.value = 1;
  n3.value = 5;
  n4.value = 4;
  n5.value = 11;

  print_linkedlist(&n0);

  LinkedList * head = &n0;

  reorder(&head);

  print_linkedlist(head);


  return 0;
}

// Your previous Plain Text content is preserved below:

// Sort linked list

// You are given a linked list of integers. Each entry contains an integer. For example,
// Input List: 3 -> 6 -> 1 -> 5 -> 4 -> 11

// The goal is to sort the list such that all even numbers are at front, and all odd numbers are at back. For even/odd number portion the original order must be preserved. So,
// Output List; 6 -> 4 -> 3 -> 1 -> 5 -> 11