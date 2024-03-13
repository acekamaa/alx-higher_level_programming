#include "lists.h"

/**
 * check_cycle - check whether a linked list has cycles or not
 * @list: linked list to check cycles
 *
 * Return: 1 if the list has a cycle, 0 if it doesnt
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
