from pprint import pprint
from quadtree import make_space, insert, find_entities_at_point

# TODO: true unit tests

# setup the root space with it's min and max 2D bound
root_space = make_space(((0,0), (2,2)))

# insert things with bounding box in the space
insert({'name':'a','aabb': ((0.2, 0.4), (0.3,0.6))}, root_space, lambda e: e['aabb'])
insert({'name':'b', 'aabb': ((0.5,1.2), (1.5, 1.99))}, root_space, lambda e: e['aabb'])
insert({'name':'c', 'aabb': ((0.1, 0.15), (0.2,0.21))}, root_space, lambda e: e['aabb'])


in_a = (0.25, 0.5)
in_c = (0.15, 0.2)
in_b = (0.8, 1.4)
in_0 = (1.6, 0.2)

pprint(root_space)

# point intersection check
print('in a')
pprint(find_entities_at_point(in_a, root_space))

print('in b')
pprint(find_entities_at_point(in_b, root_space))

print('in c')
pprint(find_entities_at_point(in_c, root_space))

print('in none')
pprint(find_entities_at_point(in_0, root_space))