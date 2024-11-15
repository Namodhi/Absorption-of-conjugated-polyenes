#!/usr/bin/env python
# coding: utf-8

# # Calculate the Length of the Conjugated System
# 
# To calculate the length of the conjugated system, we use the formula:
# 
# $$
# L = \sqrt{\frac{h \cdot \lambda_{\text{max}} \cdot (2n_i + 1)}{8 \cdot m_e \cdot c}}$$
# 
# ### Variables:
# - $( h$): Planck's constant ($(6.626 \times 10^{-34}$) J·s)
# - $( \lambda_{\text{max}} $): Wavelength corresponding to maximum absorption (in meters)
# - $( n_i $): Quantum number (integer)
# - $( m_e $): Mass of the electron (\(9.109 \times 10^{-31}\) kg)
# - $( c $): Speed of light (\(3.00 \times 10^8\) m/s)
# 
# The calculated $( L $) is the length of the conjugated system (in meters).
# 

# In[1]:


import math

# Constants
h = 6.626e-34  # Planck's constant in Js
factor = 2 * 11 + 1  # (2 * 11 + 1)
me = 9.109e-31  # mass of electron in kg
c = 3e8  # speed of light in m/s

 # wavelength in meters
wavelength = 476e-9   #change this number with the measured wavelength for a given polyene

# Numerator
numerator = h * wavelength * factor

# Denominator
denominator = 8 * me * c

# Final calculation
L = math.sqrt(numerator / denominator)
print (L)


# ### To obtain the theoretical values 
# 
# $$L_{theory}=0.139 nm \times m$$
# - $( 0.139 nm$): Average C-C bond length
# - $( m$): number of bonds in the $\pi$-conjugated system
# 

# In[29]:


#Theoretical length
m=5
Lt = 0.139*m
print (Lt)


# ### For the comparison, calculate the percentage error with respect to the theoretical and reference values 
# 
# ### Percentage Reference Error Formula
# 
# The percentage error is calculated using the formula:
# 
# $$
# \text{Percentage Error} = \left| \frac{\text{Measured Value} - \text{Reference Value}}{\text{Reference Value}} \right| \times 100
# $$
# 
# ### Steps to Calculate:
# 1. Subtract the **Reference Value** from the **Measured Value**.
# 2. Take the absolute value of the result.
# 3. Divide the absolute difference by the **Reference Value**.
# 4. Multiply the result by 100 to get the percentage.
# 
# ### Percentage Theoretical Error Formula
# 
# $$
# \text{Theoretical Error} = \left| \frac{\text{Measured Value} - \text{Theoretical Value}}{\text{heoretical Value}} \right| \times 100
# $$
# 
# 

# In[37]:


def calculate_reference_percentage_error(measured, reference):
    return abs((measured - reference) / reference) * 100

# Example usage
measured = 0.751
reference =0.726
print(f"Percentage Reference Error: {calculate_reference_percentage_error(measured, reference):.2f}%")


# In[41]:


def calculate_percentage_theory_error(measured, reference):
    return abs((measured - theory) / theory) * 100

# Example usage
measured = 0.751
theory =0.695
print(f"Percentage Theoretical Error: {calculate_percentage_theory_error(measured, reference):.2f}%")


# In[ ]:




