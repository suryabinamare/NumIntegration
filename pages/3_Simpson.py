import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

def coeff(n):
    A = np.ones(n+1)
    if n%2 == 0:
        b = int(n/2 + 1)
        for i in range(1, b, 1):
            A[2*i-1] = 4  
            A[2*i]= 2
            A[-1]=1
        return np.array(A)
    else:
        print('Error! n should be positive even integer')


def simpson_value(f, a, b, n, coef):
    # Calculate the width of each subinterval

    if n%2 ==0:
        width = (b - a) / n   
        # Generate the endpoints of the subintervals
        endpoints = [a + i * width for i in range(n + 1)]

        func = sp.lambdify(x,f,"numpy")
        A = func(np.array(endpoints))
        values = A*coef*width/3
        return values, np.sum(values)
    else:
        print('Error! n should be positive even integer greater than 2')



#function to generate function values
def func_values(f,a,b,n):
    x_value = np.linspace(a,b,200)
    width = (b - a) / n   
        # Generate the endpoints of the subintervals
    endpoints = [a + i * width for i in range(n + 1)]
    B = np.array(endpoints)

    func = sp.lambdify(x,f,"numpy")
    y_value = func(x_value)
    A = func(np.array(endpoints)).tolist()
    values = [[endpoints[i],A[i]] for i in range(n+1)]
    pairs = np.array(values)
    return pairs, x_value, y_value



#fit the parabolas to given three points and returns function vlaues 
def parabola(A):
    x_points = A[:,0]
    y_points = A[:,1]
    coeff = np.polyfit(x_points, y_points, 2)
    parab = np.poly1d(coeff)
    x_values = np.linspace(min(x_points), max(x_points), 100)
    y_values = parab(x_values)
    return x_values, y_values




def graph_parabola(A, n, x, y):
    fig, ax = plt.subplots()
    for j in range(int(n/2)):
        B = A[2*j:2*j+3, :]
        C,D = parabola(B)
        ax.plot(C,D, label = 'The Parabola')
        ax.fill_between(C,D, alpha = 0.2)
        ax.scatter(B[:,0], B[:,1], color = 'r')
    ax.plot(x,y, color = 'b', label = 'Function f(x)')
    #ax.fill_between(x, y, color='skyblue', alpha=0.3)
    ax.set_title("Function and Parabolas")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid()
    ax.legend()
    return st.pyplot(fig)


st.subheader('Simpson Rule')
st.write('''To evaluate $\displaystyle \int_a^b f(x)\,dx$ using the __Simpson rule__, we 
         approximate the integral by dividing the interval [a,b] into $n$
         subintervals of equal width $\Delta x$. The Simpson's Rule 
         uses parabolas to estimate the area under the curve. ''')
st.write('''
For example, the shaded region under the graph on the left represents the the value of the $\displaystyle \int_1^3\sin x\,dx$, 
The graph on the right shows the graph of $y = \sin(x)$ is approximated by a parabola whose equation 
         is $y = -0.42x^2+1.32x -0.06$. Note that there exists a unique 
         parabola that passes through three non-colinear points. The parabola in the graph passes through 
         $A(1, \sin(1)), B(2, \sin(2)),$ and $C(3,\sin(3))$. \n
''')






# Display an image from a local file
COL1, COL2 = st.columns(2, gap = 'medium', vertical_alignment= 'center')
with COL1:
    st.image('pages/graph1.png', width= 300)
with COL2:
    st.image('pages/simpson.png', width= 300)

st.write('\n')
st.write('\n')
R1, R2 = st.columns(2, gap = 'large')
with R1:
    st.write('''Suppose that the parabola $p(x) = ax^2 + bx + c$ that passes through three points $(x_{i-1}, p(x_{i-1}), (x_i, p(x_i))$, and 
             $(x_{i+1}, p(x_{i+1}))$ (A parabola over two subintervals, $[x_{i-1},x_i], [x_i, x_{i+1}]$). 
             After lengthy algebraic calculation (ommitted here), we can prove that \n''')
    st.latex(r'''\displaystyle \int_{x_{i-1}}^{x_{i+1}}p(x)\,dx = \frac{\Delta x}{3} \left[ p(x_{i-1}) + 4p(x_i)
                       + p(x_{i+1})\right]''')

with R2:
    st.image('pages/simpson1.png', width= 250)

st.write('\n')
st.write('\n')


st.markdown('''In general, we divide the interval $[a, b]$ into n subintervals as follows. We approximate the curve by a number of 
         parabolas, (a parabola over two subintervals). This means that $n$ should be even, and the number of 
         parabolas would be $\\frac{n}{2}$. Taking the sum of integral of all parabolas, we get''')
st.latex(r'''
 \begin{align*}
    & a = x_0 < x_1 <x_2< \dots < x_{n-1}<x_n = b, \quad \text{each with the width}\quad \Delta x= \frac{b-a}{n}\\\\
    & \displaystyle \int_a^bf(x)\,dx \approx \frac{\Delta x}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \dots + 2f(x_{n-2}) +
         4f(x_{n-1}) + f(x_n)\right] \\\\   
\end{align*}
''')


st.markdown("<hr style='border: 2px solid black; width: 100%;'>", unsafe_allow_html=True)

st.write('\n')
st.write('__Practice Examples__:')
st.write('\n')


# Input function:
expr = st.text_input("Enter the function f(x) = ", "x**2 + 2*x + 2")
func = sp.sympify(expr)
x = sp.symbols('x')

st.latex('''f(x) = ''')
st.latex(func)


st.write('__Enter the values for $a, b$, and $n$.__ ')

#input parameters;
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('Enter the $a$: ', value = 0)
with col2:
    b = st.number_input('Enter the $b$: ', value = 4)
with col3:
    n = st.number_input('Enter the n: ', value = 6)





A = coeff(n)
S, V = simpson_value(expr, a, b, n, A)






C1, C2 = st.columns(2)
with C1:
    st.markdown('__The Simpson value:__')
    st.write(f'$\displaystyle \int_a^bf(x)\,dx \ \\approx $ {V:.6f}')
with C2:
    Actual = sp.integrate(func, (x, a, b))
    st.markdown("__The actual value:__")
    st.write(f'$\displaystyle \int_a^bf(x)\,dx=$ {Actual.evalf():.6f}')




st.markdown("<hr style='border: 2px solid black; width: 100%;'>", unsafe_allow_html=True)
matrix, x_value, y_value = func_values(func,a, b,n)
graph_parabola(matrix, n, x_value, y_value)









