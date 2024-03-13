#include "lists.h"

/**
 * insert_node - inserts a node to a list
 * @head: A pointer to the head of list
 * @number: the number to insert
 * Return: 0 or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;
	return (new);
}
