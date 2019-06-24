class HashMap: #constructor
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
#hash method
  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions
#compressor method
  def compressor(self, hash_code):
    return hash_code % self.array_size
#assign method
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
#if it's empty
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
#if the keys match
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return
#retrieve method
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
#if it's empty
    if possible_return_value is None:
        return None
#if the keys match
    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    if possible_return_value[0] != key:
      retrieval_collisions = 1
      while(possible_return_value[0] != key):
        
        new_hash_code = self.hash(key, retrieval_collisions)
        retrieving_array_index = self.compressor(new_hash_code)
        possible_return_value = self.array[retrieving_array_index]
        if possible_return_value == None:
          return None
        elif possible_return_value[0] != key:
          retrieval_collisions += 1
        else:
          return possible_return_value[1]
