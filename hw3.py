# Q1
from functools import reduce
def convert_to_decimal(bits):
  exponents = range(len(bits)-1, -1, -1)
  nums = [b * pow(2, e) for b, e in zip(bits, exponents)]
  return reduce(lambda acc, num: acc + num, nums)

# Q2
# a
def parse_csv(lines):
  return [(entry.split(',')[0], int(entry.split(',')[1])) for entry in lines]

# b
def unique_characters(sentence):
  return {c for c in sentence}

# c
def squares_dict(lower_bound, upper_bound):
  return {n: pow(n, 2) for n in range(lower_bound, upper_bound + 1)}

# Q3
def strip_characters(sentence, chars_to_remove):
  return reduce(lambda acc, c: acc + c if c not in chars_to_remove else acc, sentence)

# Q4
"""
box's value attribute was mutated because python passes arguments by object-reference.
Effectively, calling a function creates a new variable that stores a pointer to the passed-in
object. In quintuple's case, num *= 5 creates a new object with value num * 5, and the
created argument variable, num, stops pointing to the original object and points to the new
created object. In box_quintuple's case, box.value *= 5 will refer to the original object 
pointed to by the box variable, and that objects value attribute will point to a new object
with a value of box.value * 5. Note that box still points to the original, passed-in object
and consequently the original object's value attribute was changed.
"""

# Q5
"""
Python utilizes duck typing. That is, you can call any method (e.q. foo()) as on any object
as obj.foo(). If obj has a foo method, no error will be thrown. Here the int object does not
define a __len__ method, so the appropriate TypeError is thrown when len executes the 
__len__ method of the passed in object.
"""

# Q6
class Duck:
  def __init__(self):
    pass

def is_duck_a(duck):
  try:
    duck.quack()
    return True
  except:
    return False
  
def is_duck_b(duck):
  return isinstance(duck, Duck)

# a
class DuckA:
  def __init__(self):
    pass

  def quack(self):
    print('do quack')

# b
class DuckB(Duck):
  def __init__(self):
    pass

# c
"""
is_duck_a is more pythonic. If something is expected to work--i.e. if a "duck" has a
quack method--pythonic thinking dictates that this quack method should be called regardless
of the "duck"'s actual type. Further, rather than first verifying that the duck is a valid
duck with a quack method, simply try to call the quack method and catch and handle any 
exceptions that may occur.
"""

# Q7
# a
def largest_sum(nums, k):
  if k < 0 or k > len(nums):
    raise ValueError
  elif k == 0:
    return 0
  
  max_sum = None
  for i in range(len(nums)-k):
    sum = 0
    for num in nums[i:i+k]:
      sum += num
    if not max_sum or sum > max_sum:
      max_sum = sum
  return max_sum

# b
def largest_sum(nums, k):
  if k < 0 or k > len(nums):
    raise ValueError
  elif k == 0:
    return 0

  sum = 0
  for num in nums[:k]:
    sum += num

  max_sum = sum
  for i in range(0, len(nums)-k-1):
    sum -= nums[i]
    sum += nums[i+k]
    max_sum = max(sum, max_sum)
  return max_sum

# Q8
# a
class Event:
  def __init__(self, start_time, end_time):
    if start_time >= end_time:
      raise ValueError
    self.start_time = start_time
    self.end_time = end_time

# b
class Calendar:
  def __init__(self):
    self._events = []
  
  def get_events(self):
    return self._events
  
  def add_event(self, event):
    if not isinstance(event, Event):
      raise TypeError
    self._events.append(event)

# c
class AdventCalendar(Calendar):
  def __init__(self, year):
    # super().__init__()
    # self._events = []
    self.year = year

"""
The AdventCalendar does not call the super class's constructor, so __events is
never initialized, and is never made a member variable of the Calendar instance.
Possible fixes are included in the comments of AdventCalendar.
"""

# Q9
def test_closures():
  a = "before"
  def test():
    print(a)
  a = "after"
  return test

def test_out_of_scope():
  test = test_closures()
  test()
  # prints "after"

"""
Python supports closures, as test is able to access the free variable, a, even when a
is out of scope. Unlike Haskell, Python closures do not capture the free variable's 
value, and will always reflect the variable's most recent value when called.
"""

# Q10
# a
"""
I expect C-Lang to be faster. Compiled languages are converted into more efficient
machine code at compile-time (i.e. before the program actually runs). In I-Lang, every
line of code must be read, analyzed, and exectued at run-time, which adds more overhead.
"""

# b
"""
I-Lang will likely run first, although it may operate more slowly. The C-Lang server
will have compilation overhead, which will take some time before the server can be run.
"""

# c
"""
Connie will be able to execute Jamie's script, but not Tim's executable. Tim's 
executable would have been compiled for a specific ISA, which would not be the same for
the N1 chip. Interpreted languages are converted to machine code at runtime, and therefore
Jamie's script can be executed on either architecture.
"""

# Q11
"""
NumPy is faster than Python for several reasons. NumPy arrays are a collection of homogeneous
data-types in contiguous memory locations, similar to C++. On the other hand, Python arrays
can consist of heterogeneous data types stored in non-contiguous memory locations. This
locality of reference and type uniformity leads to faster array calculations in NumPy.
Furthermore, NumPy operations are implemented in C, which avoids the inefficiencies of loops,
pointer indirection and per-element dynamic checking in Python.
"""
