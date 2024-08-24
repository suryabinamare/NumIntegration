import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
)

st.subheader("Numerical Integration:")
st.markdown("""
 Numerical integration is used to approximate the integral of a function when an exact analytical
solution is either impractical or impossible to obtain due to their complexities or the nature of the 
            functions involved. The core idea behind numerical integration is to approximate the area 
            under a curve by summing the areas of simpler shapes, typically rectangles or trapezoids or 
            parabolas, which can be computed more easily.  """)
st.markdown("""While numerical integration methods provide powerful tools for approximation
            , they come up with challenges. The nature of functions being integrated and type of 
            numerical integration methods may significantly affect the accuracy of the solution. 
            For functions with discontinuities, singularities, or rapid oscillations  that degrade the 
            quality of the solution may require other special techniques or adaptive methods.""")
st.markdown("""
Several methods have been used to achieve numerical integration, each with its advantages and trade-offs. 
            Some of the prominent methods include; Midpoint Rule, Trapezoidal Rule, Simpson's Rule, 
            , Gaussian Quadratures, etc. We include only first three metheds as part of our discussion. 
""")
