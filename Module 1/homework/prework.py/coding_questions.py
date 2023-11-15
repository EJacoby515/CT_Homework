# -------- Q1 --------
def hello_name(user_name):
    print("Hello " + user_name + "!")

hello_name("Eric")

# -------- Q2 --------
def first_odds():
   for num in range(1,101,2):
       print (num)
first_odds()

# -------- Q3 --------
def max_num_in_list(a_list):
    return max(a_list)

my_list = [666, 999, 333, 678, 14]
tired= max_num_in_list(my_list)

print("The Max number is: ", tired)

# -------- Q4 --------
def is_leap_year(a_year):
    return(a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)   

checker = 1985
very_tired = is_leap_year(checker)

print("is", checker ,very_tired)

# -------- Q5 --------

def is_consecutive(a_list):
    return all(a_list[i] + 1  == a_list[i + 1] for i  in range(len(a_list) -1))

consecutive_list =  [3,4,5,6,7,8]
non_consecutive_list  = [3,7,2,5]

result_consecutive = is_consecutive(consecutive_list)
result_non_consecutive = is_consecutive(non_consecutive_list)

print(result_consecutive)
print(result_non_consecutive)