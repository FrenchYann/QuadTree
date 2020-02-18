def make_space(aabb):
  return {'aabb':aabb, 'content':[]}

def make_sub_spaces(space):
  """
  divide a space into 4 equal spaces
  """
  space_min, space_max = space['aabb']
  space_min_x, space_min_y = space_min
  space_max_x, space_max_y = space_max
  mid_x = (space_min_x + (space_max_x - space_min_x) * 0.5)
  mid_y = (space_min_y + (space_max_y - space_min_y) * 0.5)
  mid = (mid_x, mid_y)
  return [
      make_space((space_min           , mid)),
      make_space(((mid_x, space_min_y), (space_max_x, mid_y))),
      make_space(((space_min_x, mid_y), (mid_x, space_max_y))),
      make_space((mid                 , space_max)),
    ]

def is_aabb_in_space(aabb, space):
  """
  return True if aabb is entirely contained in space
  """
  (aabb_min_x, aabb_min_y), (aabb_max_x, aabb_max_y) = aabb
  (space_min_x, space_min_y), (space_max_x, space_max_y) = space['aabb']
  return aabb_min_x >= space_min_x and \
         aabb_min_y >= space_min_y and \
         aabb_max_x <  space_max_x and \
         aabb_max_y <  space_max_y

def is_point_in_aabb(point, aabb):
  """
  return True if point is in aabb
  """
  px, py = point
  (min_x, min_y), (max_x, max_y) = aabb
  return px >= min_x and px < max_x and py >= min_y and py < max_y


ident = lambda x: x

def insert(entity, space, get_aabb=ident):
  """
  insert entity in space using get_aabb to produce an aabb from the entity
  get_aabb: entity -> ((min_x, min_y), (max_x, max_y))
  """
  sub_spaces = space.get('sub_spaces', make_sub_spaces(space))
  for sub_space in sub_spaces:
    if is_aabb_in_space(get_aabb(entity), sub_space):
      space['sub_spaces'] = sub_spaces
      insert(entity, sub_space, get_aabb)
      break
  else:
    space['content'].append((entity, get_aabb))
  return space

def find_entities_at_point(point, space):
  """
  return all entities in space whose aabb contain point
  """
  res = []
  for entity, get_aabb in space['content']:
    if is_point_in_aabb(point, get_aabb(entity)):
      res.append(entity)
  for sub_space in space.get('sub_spaces',[]):
    if is_point_in_aabb(point, sub_space['aabb']):
      res += find_entities_at_point(point, sub_space)
      break
  return res
