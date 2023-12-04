#include <stddef.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slwpoint = *head;
    listint_t *fstpoint = *head;
    listint_t *revlist = NULL;
    listint_t *tem;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fstpoint != NULL && fstpoint->next != NULL)
    {
        fstpoint = fstpoint->next->next;

        tem = slwpoint->next;
        slwpoint->next = revlist;
        revlist = slwpoint;
        slwpoint = tem;
    }

    if (fstpoint != NULL)
        slwpoint = slwpoint->next;

    while (revlist != NULL && slwpoint != NULL)
    {
        if (revlist->n != slwpoint->n)
            return 0;
        revlist = revlist->next;
        slwpoint = slwpoint->next;
    }

    return (1);
}
