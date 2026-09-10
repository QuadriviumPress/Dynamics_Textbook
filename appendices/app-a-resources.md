(app-a)=
# A. Resources

<!-- Source PDF page 277; printed label 268. -->

This Appendix contains various formulas and constants that may be used throughout this text or needed to solve problems.

(sec-A-1)=
## A.1 Constants

| Quantity | Symbol | Value |
| --- | --- | --- |
| Acceleration due to gravity at Earth’s surface | $g$ | $9.81\,\mathrm{m\,s^{-2}}$ |
| Gravitational constant | $G$ | $6.674\times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$ |
| Speed of light (vacuum) | $c$ | $2.998\times 10^8\,\mathrm{m\,s^{-1}}$ |
| Speed of sound in air at $20\,{}^\circ\mathrm{C}$ | $c_s$ | $343\,\mathrm{m\,s^{-1}}$ |
| Mass of Earth | $M_E$ | $5.98\times 10^{24}\,\mathrm{kg}$ |
| Mass of Sun | $M_S$ | $1.99\times 10^{30}\,\mathrm{kg}$ |
| Mass of Moon | $M_M$ | $7.36\times 10^{22}\,\mathrm{kg}$ |
| Mean Earth orbit (astronomical unit) | $r_E$ | $1.50\times 10^{11}\,\mathrm{m}$ |
| Earth radius | $R_E$ | $6.37\times 10^6\,\mathrm{m}$ |
| Sun radius | $R_S$ | $6.96\times 10^8\,\mathrm{m}$ |
| Moon radius | $R_M$ | $1.74\times 10^6\,\mathrm{m}$ |
| Planck constant | $h$ | $6.63\times 10^{-34}\,\mathrm{J\,s}$ |
| Boltzmann constant | $k_B$ | $1.38\times 10^{-23}\,\mathrm{J\,K^{-1}}$ |
| Permittivity of Free Space | $\epsilon_0$ | $8.854\times 10^{-12}\,\mathrm{C\,V^{-1}\,m^{-1}}$ |
| Permeability of Free Space | $\mu_0$ | $4\pi\times 10^{-7}\,\mathrm{T\,m\,A^{-1}}$ |
| Elementary charge | $\lvert e\rvert$ | $1.6\times 10^{-19}\,\mathrm{C}$ |
| Electron mass | $m_e$ | $9.11\times 10^{-31}\,\mathrm{kg}$ |
| Proton mass | $m_p$ | $1.67\times 10^{-27}\,\mathrm{kg}$ |
| Coulomb constant | $k=\frac{1}{4\pi\epsilon_0}$ | $8.99\times 10^9\,\mathrm{N\,m^2\,C^{-2}}$ |

Numerical values may also be presented with prefixes. For example, km corresponds to kilometer or 1000 m.

| Factor | Prefix | Symbol | Factor | Prefix | Symbol |
| --- | --- | --- | --- | --- | --- |
| $10^{-3}$ | milli | m | $10^3$ | kilo | k |
| $10^{-6}$ | micro | $\mu$ | $10^6$ | mega | M |
| $10^{-9}$ | nano | n | $10^9$ | giga | G |
| $10^{-12}$ | pico | p | $10^{12}$ | tera | T |

<!-- Source PDF page 278; printed label 269. -->

(sec-A-2)=
## A.2 Math Identities

$$
\vec{a} \cdot \vec{b} = ab\cos \theta = a_{x}b_{x}+ a_{y}b_{y}+ a_{z}b_{z}
$$

$$
\vec{a} \times \vec{b} = (a_{y}b_{z}- a_{z}b_{y})\hat{\imath} + (a_{z}b_{x}- a_{x}b_{z})\hat{\jmath} + (a_{x}b_{y}- a_{y}b_{x})\hat{k}, |\vec{a} \times \vec{b}| = ab\sin \varphi
$$

$$
\int \frac{\mathrm{d}x}{(x^{2}+ a^{2})^{3/2}} = \frac{1}{a^{2}} \frac{x}{\sqrt{x^{2}+ a^{2}}}, \int \frac{\mathrm{d}x}{x^{2}+ a^{2}} = \frac{1}{a} \tan ^{-1}\bigg(\frac{x}{a} \bigg), \int \frac{\mathrm{d}x}{\sqrt{a^{2}- x^{2}}} = \sin ^{-1}\bigg(\frac{x}{a} \bigg)
$$

:::{image} ../images/math/p278-d79919ffc2b8.svg
:alt: Mathematical expression from source PDF page 278
:class: source-equation
:align: center
:::

$\sin (\theta \pm \gamma) = \sin \theta \cos \gamma \pm \cos \theta \sin \gamma, \cos (\theta \pm \gamma) = \cos \theta \cos \gamma \mp \sin \theta \sin \gamma$

$$
\sin \alpha \pm \sin \beta = 2\sin \Bigg(\frac{\alpha \pm \beta}{2} \Bigg)\cos \Bigg(\frac{\alpha \mp \beta}{2} \Bigg)
$$

$$
\cos \alpha + \cos \beta = 2\cos \Bigg(\frac{\alpha + \beta}{2} \Bigg)\cos \Bigg(\frac{\alpha - \beta}{2} \Bigg)
$$

$$
\cos \alpha - \cos \beta = -2\sin \Bigg(\frac{\alpha + \beta}{2} \Bigg)\sin \Bigg(\frac{\alpha - \beta}{2} \Bigg)
$$

$$
\ln (ab) = \ln (a) + \ln (b), \ln \bigg(\frac{a}{b} \bigg) = \ln (a) - \ln (b)
$$

(sec-A-3)=
## A.3 Common Approximations

See [Chapter 1.6](#sec-1-6) and [Appendix B](#app-b) for details on how functions can be approximated.

Common Taylor Series approximations for values around $x \approx 0$. Note that angles must be in units of radians for these approximations to be applicable:

$$
\begin{aligned}
\sin x &= x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \cdot \cdot \cdot \\
\cos x &= 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \cdot \cdot \cdot \\
e^{x}&= 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdot \cdot \cdot \\
\ln (1 + x) &= x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \frac{x^{4}}{4} + \cdot \cdot \cdot \\
\frac{1}{1 - x} &= 1 + x + x^{2}+ x^{3}+ \cdot \cdot \cdot \\
\frac{1}{1 + x} &= 1 - x + x^{2}- x^{3}+ \cdot \cdot \cdot \\
\frac{1}{1 - x^{2}} &= 1 + x^{2}+ x^{4}+ x^{6}+ \cdot \cdot \cdot \\
\frac{1}{1 + x^{2}} &= 1 - x^{2}+ x^{4}- x^{6}+ \cdot \cdot \cdot \\
\frac{1}{(1 - x)^{2}} &= 1 + 2x + 3x^{2}+ 4x^{3}+ \cdot \cdot \cdot \\
\frac{1}{(1 + x)^{2}} &= 1 - 2x + 3x^{2}- 4x^{3}+ \cdot \cdot \cdot
\end{aligned}
$$

$$
\begin{aligned}
\frac{1}{\sqrt{1 - x}} &= 1 + \frac{x}{2} + \frac{3x^{2}}{8} + \frac{5x^{3}}{16} + \cdot \cdot \cdot \\
\frac{1}{\sqrt{1 + x}} &= 1 - \frac{x}{2} + \frac{3x^{2}}{8} - \frac{5x^{3}}{16} + \cdot \cdot \cdot
\end{aligned}
$$

$$
\frac{1}{\sqrt{1 - x^{2}}} = 1 + \frac{x^{2}}{2} + \frac{3x^{4}}{8} + \frac{5x^{6}}{16} + \cdot \cdot \cdot \frac{1}{\sqrt{1 + x^{2}}} = 1 - \frac{x^{2}}{2} + \frac{3x^{4}}{8} - \frac{5x^{6}}{16} + \cdot \cdot \cdot
$$

<!-- Source PDF page 279; printed label 270. -->

(sec-A-4)=
## A.4 Moment of Inertia

The Moment of Inertia, $I$, represents how the mass of a system is distributed as a function of position and describes how efficiently the system rotates. Here is a chart of basic shapes and their moments of inertia. For information on how to calculate Moments of Inertia see [Section 7.2.2](#sec-7-2-2).

:::{image} ../images/figures/figure-p279-1.png
:alt: Illustration from source PDF page 279
:width: 553px
:align: center
:::

<!-- Source PDF page 280; printed label 271. -->

(sec-A-5)=
## A.5 Vector Differential Operators

This section gives the full coordinate transformations for the gradient, divergence, and curl in 3-D. The following is a brief explanation of those coordinate transformations.

(sec-A-5-1)=
### A.5.1 General Coordinates

In general, consider a 3-D coordinate system $c_{1}, c_{2}$, and $c_{3}$ with orthogonal unit vectors defined as $\hat{e}_{1}, \hat{e}_{2}$, and $\hat{e}_{3}$. Note that $c_{1}, c_{2}$, and $c_{3}$ are merely stand-ins for $x,y,z$ or $r,\theta,\varphi$.

In this general 3-D coordinate system, a line element would be

$$
\mathrm{d}s = \langle h_{1}\mathrm{d}c_{1},h_{2}\mathrm{d}c_{2},h_{3}\mathrm{d}c_{3}\rangle
$$

where $h_{1}, h_{2}$, and $h_{3}$ are scale factors that may need to be applied to each coordinate (the value of these scale factors depends on the coordinate transformation - more on this below).

Because of these scale factors, the gradient, divergence, and curl transformations will be a bit different in each coordinate system. In the general form, these functions are:

The gradient of a function $f$ is then defined as:

$$
\vec{\nabla}f = \Bigg(\frac{1}{h_{1}} \frac{\partial f}{\partial c_{1}} \Bigg)\hat{e}_{1}+ \Bigg(\frac{1}{h_{2}} \frac{\partial f}{\partial c_{2}} \Bigg)\hat{e}_{2}+ \Bigg(\frac{1}{h_{3}} \frac{\partial f}{\partial c_{3}} \Bigg)\hat{e}_{3}
$$

The divergence of a vector $\vec{A}$ is:

$$
\vec{\nabla} \cdot \vec{A} = \frac{1}{h_{1}h_{2}h_{3}} \Bigg[\frac{\partial}{\partial c_{1}} (h_{2}h_{3}A_{1}) + \frac{\partial}{\partial c_{2}} (h_{1}h_{3}A_{2}) + \frac{\partial}{\partial c_{3}} (h_{1}h_{2}A_{3})\Bigg]
$$

and the curl of a vector $\vec{A}$ is:

$$
\vec{\nabla} \times \vec{A} = \frac{1}{h_{1}h_{2}h_{3}}
\begin{vmatrix}
h_{1}\hat{e}_{1} & h_{2}\hat{e}_{2} & h_{3}\hat{e}_{3} \\
\dfrac{\partial}{\partial c_{1}} & \dfrac{\partial}{\partial c_{2}} & \dfrac{\partial}{\partial c_{3}} \\
h_{1}A_{1} & h_{2}A_{2} & h_{3}A_{3}
\end{vmatrix}
$$

(sec-A-5-2)=
### A.5.2 Cartesian Coordinates

In the Cartesian system, we have $c_{1}= x, c_{2}= y$, and $c_{3}= z$ and $h_{1}= 1, h_{2}$ = 1, and $h_{3}$ = 1. As a result, we have the following for Cartesian Coordinates:

$$
\vec{\nabla}f = \frac{\partial f}{\partial x} \hat{x} + \frac{\partial f}{\partial y} \hat{y} + \frac{\partial f}{\partial z} \hat{z}
$$

$$
\vec{\nabla} \cdot \vec{A} = \Bigg[\frac{\partial}{\partial x} (A_{1}) + \frac{\partial}{\partial y} (A_{2}) + \frac{\partial}{\partial z} (A_{3})\Bigg]
$$

<!-- Source PDF page 281; printed label 272. -->

$$
\vec{\nabla} \times \vec{A} =
\begin{vmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
A_{1} & A_{2} & A_{3}
\end{vmatrix}
$$

where $\hat{x}$ is used for $\hat{\imath}, \hat{y}$ is used for $\hat{\jmath}$ , and $\hat{z}$ is used for $\hat{k}$ .

(sec-A-5-3)=
### A.5.3 Cylindrical Coordinates

In cylindrical coordinates, $c_{1}= r, c_{2}= \theta$, and $c_{3}= z$, where

$$
\begin{aligned}
x &= r\cos \varphi \\
y &= r\sin \varphi
\end{aligned}
$$

For cylindrical coordinates, $h_{1}= 1, h_{2}= r$, and $h_{3}$ = 1. Note, these terms should look familiar. That is, for a cylinder, a tiny section of volume is given by:

$$
dV = r \mathrm{d}r\mathrm{d}\theta \mathrm{d}z
$$

Based on the above, we get the following for cylindrical coordinates.

$$
\vec{\nabla}f = \Bigg(\frac{\partial f}{\partial r} \Bigg)\hat{r} + \Bigg(\frac{1}{r} \frac{\partial f}{\partial \theta} \Bigg)\hat{\theta} + \Bigg(\frac{\partial f}{\partial z} \Bigg)\hat{z}
$$

$$
\vec{\nabla} \cdot \vec{A} = \frac{1}{r} \Bigg[\frac{\partial}{\partial r} (rA_{1}) + \frac{\partial}{\partial \theta} (A_{2}) + \frac{\partial}{\partial z} (rA_{3})\Bigg]
$$

$$
\vec{\nabla} \times \vec{A} = \frac{1}{r}
\begin{vmatrix}
\hat{r} & r\hat{\theta} & \hat{z} \\
\dfrac{\partial}{\partial r} & \dfrac{\partial}{\partial \theta} & \dfrac{\partial}{\partial z} \\
A_{1} & rA_{2} & A_{3}
\end{vmatrix}
$$

(sec-A-5-4)=
### A.5.4 Spherical Coordinates

In spherical coordinates, $c_{1}= r, c_{2}= \theta$, and $c_{3}= \varphi$, where

$$
\begin{aligned}
x &= r\sin \theta \cos \varphi \\
y &= r\sin \theta \sin \varphi \\
z &= r\cos \theta
\end{aligned}
$$

For spherical coordinates, $h_{1}= 1, h_{2}= r$, and $h_{3}= r\sin \theta$. Note, these terms should look familiar. That is, for a sphere, a tiny section of volume is given by:

$$
dV = r^{2}\sin \theta \mathrm{d}r\mathrm{d}\theta \mathrm{d}\varphi
$$

<!-- Source PDF page 282; printed label 273. -->

Based on the above, we get the following for spherical coordinates.

$$
\vec{\nabla}f = \Bigg(\frac{\partial f}{\partial r} \Bigg)\hat{r} + \Bigg(\frac{1}{r} \frac{\partial f}{\partial \theta} \Bigg)\hat{\theta} + \Bigg(\frac{1}{r\sin \theta} \frac{\partial f}{\partial \varphi} \Bigg)\hat{\varphi}
$$

$$
\vec{\nabla} \cdot \vec{A} = \frac{1}{r^{2}\sin \theta} \Bigg[\frac{\partial}{\partial r} (r^{2}\sin \theta A_{1}) + \frac{\partial}{\partial \theta} (r\sin \theta A_{2}) + \frac{\partial}{\partial \varphi} (rA_{3})\Bigg]
$$

$$
\vec{\nabla} \times \vec{A} = \frac{1}{r^{2}\sin \theta}
\begin{vmatrix}
\hat{r} & r\hat{\theta} & r\sin\theta\,\hat{\varphi} \\
\dfrac{\partial}{\partial r} & \dfrac{\partial}{\partial \theta} & \dfrac{\partial}{\partial \varphi} \\
A_{1} & rA_{2} & r\sin\theta\,A_{3}
\end{vmatrix}
$$
