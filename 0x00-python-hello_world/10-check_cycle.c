#include "lists.h"
/**
 * check_cycle -fnction.
 *Description: Function checks if a singly linked list has a cycle in it.
 * @list: pointer of type listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	/* slow = +1*/
	/* fast = +2*/
	while ((slow && fast != NULL) && (fast->next != NULL))
	{
		slow = slow->next;
		fast = fast->next->next;
		/*slow = fast -> means they're in a cycle*/
		if (slow == fast)
			return (1);
	}
	/*slow != fast -> list have no cycle*/
	return (0);
}
