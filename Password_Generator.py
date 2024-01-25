#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length < 7:
            print("Please enter a valid length greater than 6.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length as a number.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




