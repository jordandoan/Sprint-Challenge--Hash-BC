#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length-1)
    for ticket in tickets:
        hash_table_insert(ht, ticket.destination, ticket.source)
    prev = hash_table_retrieve(ht, 'NONE')
    route[-1] = prev
    for i in range(len(route)-2, -1, -1):
        prev = hash_table_retrieve(ht, prev)
        route[i] = prev
    return route
