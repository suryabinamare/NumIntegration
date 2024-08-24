import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)



st.subheader('Midpoint Rule')
st.write('''To evaluate $\displaystyle \int_a^b f(x)\,dx$ by Midpoint rule, we divide the interval [a,b] into $n$ subintervals
         each of equal width, $\Delta x$. We approximate the region under the graph with considering the sum of 
         areas of rectangles, each with width of $\Delta x$ and height the y-value at the midpoint of 
         the subinterval.''')
st.write('''
For example, the graph on the left represents the the value of the $\displaystyle \int_1^3\sin x\,dx$, while the graph on the right shows that 
         the integral is approximated with areas of two rectangles. Note the heights of rectangles are the $\sin(1.5)$ and 
         $\sin(2.5)$. The subintervals are [1,2] and [2,3]
''')



# Display an image from a local file
COL1, COL2 = st.columns(2)
with COL1:
    st.image('C:/Users/surya/OneDrive/Desktop/NumericalIntegration/pages/graph1.png', width= 300)
with COL2:
    st.image('C:/Users/surya/OneDrive/Desktop/NumericalIntegration/pages/midpoint.png', width= 400)

st.write('\n')

st.write('In general, we divide the interval $[a,b]$ into $n$ subintervals as follows.')
st.latex(r'''
 \begin{align*}
    & a = x_0 < x_1 <x_2< \dots < x_{n-1}<x_n = b \qquad \Delta x= \frac{b-a}{n}  (\text{width of a subinterval})\\
    & \text{Then, according to the trapezoidal rule the integral is approximated by}\\\\
    & \int_a^bf(x)\,dx \approx \left[ \text{the sum of areas of rectangles} \right]\\\\
    & \int_a^bf(x)\,dx \approx \left[\Delta xf\left(\frac{x_0+x_1}{2}\right)+ \Delta xf\left(\frac{x_1+x_2}{2}\right) 
          + \Delta xf\left(\frac{x_2+x_3}{2}\right)
          + \dots + \Delta xf\left(\frac{x_{n-1}+x_n}{2}\right)\right]     \\\\
    & \int_a^bf(x)\,dx \approx \Delta x \left[f\left(\frac{x_0+x_1}{2}\right)+ f\left(\frac{x_1+x_2}{2}\right) 
          + f\left(\frac{x_2+x_3}{2}\right)
          + \dots + f\left(\frac{x_{n-1}+x_n}{2}\right)\right]   
\end{align*}
''')

def midpoint_rule(f, a, b, n):
    delta = (b-a)/n
    midpoints = [a+delta/2 + i*delta for i in range(n)]

    func = sp.lambdify(x,f,"numpy")
    A = func(np.array(midpoints))
    values = A*delta
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

val = midpoint_rule(expr, a, b, n)

C1, C2 = st.columns(2)
with C1:
    st.markdown('__The Midpoint value:__')
    st.write(f'$\displaystyle \int_a^bf(x)\,dx \ \\approx $ {val:.4f}')
with C2:
    Actual = sp.integrate(func, (x, a, b))
    st.markdown("__The actual value:__")
    st.write(f'$\displaystyle \int_a^bf(x)\,dx=$ {Actual.evalf():.4f}')
