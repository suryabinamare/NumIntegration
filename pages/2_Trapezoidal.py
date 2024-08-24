import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)



st.subheader('Trapezoidal Rule')
st.write('''To evaluate $\displaystyle \int_a^b f(x)\,dx$ using the __Trapezoidal rule__, we 
         approximate the integral by dividing the interval $[a,b]$ into $n$
         subintervals of equal width $\Delta x$. The trapezoidal Rule 
         uses trapezoids to estimate the area under the curve. The trapezoid in the subinterval
         $[x_i, x_j]$ has $f(x_i)$ and $f(x_j)$ as parallel sides. ''')
st.write('''
For example, the shaded region under the graph on the left graph represents the the value of the $\displaystyle \int_1^3\sin x\,dx$, 
         while the sum of area of two trapezoids on the right graph approximates the region under the graph.
''')



# Display an image from a local file
COL1, COL2 = st.columns(2)
with COL1:
    st.image('C:/Users/surya/OneDrive/Desktop/NumericalIntegration/pages/graph1.png', width= 300)
with COL2:
    st.image('C:/Users/surya/OneDrive/Desktop/NumericalIntegration/pages/trapezoidal.png', width= 300)

st.write('\n')
st.write('In general, we divide the interval $[a, b]$ into n subintervals as follows, ')
st.latex(r'''
 \begin{align*}
    & a = x_0 < x_1 <x_2< \dots < x_{n-1}<x_n = b, \quad \text{each with the width}\quad \Delta x= \frac{b-a}{n}\\\\
    & \text{The sum of area of trapezoids} = \frac{\Delta x}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n)\right] \\\\
    &\text{since the area of the trapezoid for the subinterval $[x_i, x_j]$} = \frac{\Delta x}{2}[f(x_i)+f(x_j)]\\\\

    & \text{Thus the integral according to trapezoidal rule can be approximated by;}\\\\
    & \displaystyle \int_a^bf(x)\,dx \approx \frac{\Delta x}{2}\left[f(x_0) + 2f(x_1) 
         + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n)\right]\\\\
    & \text{The coefficient 2 is due to trapezoids sharing the middle heights. }
\end{align*}
''')








#to produce numpy array of coefficients of trapezoidal rule: [1,2,2,...., 2,2,1]

def coeff(n):
    lst = np.ones(n+1)
    for i in range(1, n):
        lst[i] = 2
    return lst



def trapezoidal_rule(f, a, b, n, lst):
    delta = (b-a)/n
    points = [a + i*delta for i in range(n+1)]

    func = sp.lambdify(x,f,"numpy")
    A = func(np.array(points))
    values = A*lst*delta/2
    return np.sum(values)
    

st.markdown("<hr style='border: 2px solid black; width: 100%;'>", unsafe_allow_html=True)

st.write('\n')
st.write('__Practice Examples__:')
st.write('\n')

st.write('__Enter the values for $a, b$, and $n$.__ ')
#input parameters;
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('Enter the $a$: ', value = 0)
with col2:
    b = st.number_input('Enter the $b$: ', value = 4)
with col3:
    n = st.number_input('Enter the n: ', value = 6)



# Input function:
expr = st.text_input("Enter the function f(x) = ", "x**2 + 2*x + 2")
func = sp.sympify(expr)
x = sp.symbols('x')

st.latex('''f(x) = ''')
st.latex(func)

lst = coeff(n)
val = trapezoidal_rule(expr, a, b, n, lst)

C1, C2 = st.columns(2)
with C1:
    st.markdown('__The Trapezoidal value:__')
    st.write(f'$\displaystyle \int_a^bf(x)\,dx \ \\approx $ {val:.4f}')
with C2:
    Actual = sp.integrate(func, (x, a, b))
    st.markdown("__The actual value:__")
    st.write(f'$\displaystyle \int_a^bf(x)\,dx=$ {Actual.evalf():.4f}')
