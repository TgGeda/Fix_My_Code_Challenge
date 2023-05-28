#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - Prints a doubly linked list of integers
 *
 * @h: A pointer to the first element of the list
 *
 * Return: The number of elements printed
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t n = 0; // Initialize variable 'n' to 0
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		n++; // Increment variable 'n' by 1
	}
	return (n);
}

// The code was missing the initialization of the variable 'n' and it was not incrementing the variable 'n' inside the while loop. 
// I fixed the code by initializing variable 'n' to 0 and incrementing it by 1 inside the while loop. 
// I also added comments to explain the purpose of the code.
