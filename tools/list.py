def join_list_items(list, glue = ''):
  return glue.join(list)

def add_to_list(list, item):
  list.append(item)

def reshape_list(list, width):
  list_as_string = join_list_items(list)

  shaped_list = []
  for index in range(0, len(list_as_string), width):
      list_row = list_as_string[index: index + width]
      add_to_list(shaped_list, list_row)

  shaped_string = join_list_items(shaped_list, "\n")

  return shaped_string
