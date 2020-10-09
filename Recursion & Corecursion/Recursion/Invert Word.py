def rec_func(input_value):
  item = input_value[0]
  if len(input_value) == 1:
    return item
  else:
    return rec_func(input_value[1:]) + item
  #endif
  stack.pop(len(stack)-1)
  print(stack)
#end function

print("Star:")
print(rec_func('star'))

print("\nNumbers:")
print(rec_func((1,2,3,4)))

