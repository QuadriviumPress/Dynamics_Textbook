(ch-1)=
# 1. Calculus and Vectors

<!-- Source PDF page 11; printed label 2. -->

::::{admonition} Learning Objectives

- Review of vector notation and basic calculus

- Review of coordinate systems

- Application to simple physical systems

::::

This chapter reviews basic calculus and vector notation and coordinate systems. Please also refer to [Appendix A](#app-a) for helpful equations and identities.

(sec-1-1)=
## 1.1 Coordinates and Motion in Vector Notation

(sec-1-1-1)=
### 1.1.1 Linear Motion

For linear motion, we can use the Cartesian coordinate system. The position of an object is described by a vector $\vec{r}$ in $x, y$, and $z$, the linear velocity of the object is the time derivative of position, and the linear acceleration is the time derivative of velocity.

$$
\vec{r} = x\hat{\imath} + y\hat{\jmath} + z\hat{k} = \langle x,y,z\rangle
$$ (eq-1-1)

:::{figure} ../images/figures/figure-1-1.png
:label: fig-1-1
:enumerator: 1.1
:alt: Figure shows a standard set of 3D Cartesian axes, with a position vector pointing from the origin to a point P.
:width: 143px

Position of a vector in Cartesian coordinates where $\hat{\imath}$ is the unit vector for $x, \hat{\jmath}$ is the unit vector for $y$, and $\hat{k}$ is the unit vector for $z$.
:::

The equations of linear motion in 1-D:

$$
\begin{aligned}
v_{x}&= \frac{\mathrm{d}x}{\mathrm{d}t} = \dot{x} \\
a_{x}&= \frac{\mathrm{d}v_{x}}{\mathrm{d}t} = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = \ddot{x}
\end{aligned}
$$

$$
\begin{aligned}
v_{y}&= \frac{\mathrm{d}y}{\mathrm{d}t} = \dot{y} \\
a_{y}&= \frac{\mathrm{d}v_{y}}{\mathrm{d}t} = \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} = \ddot{y}
\end{aligned}
$$

$$
\begin{aligned}
v_{z}&= \frac{\mathrm{d}z}{\mathrm{d}t} = \dot{z} \\
a_{z}&= \frac{\mathrm{d}v_{z}}{\mathrm{d}t} = \frac{\mathrm{d}^{2}z}{\mathrm{d}t^{2}} = \ddot{z}
\end{aligned}
$$

<!-- Source PDF page 12; printed label 3. -->

::::{admonition} Helpful Nomenclature

A dot over a variable can be used as shorthand for the *time* derivative of that variable. Two dots would be the second time derivative, and so forth.

Note that dots over variables are only a shorthand for the time derivative. If you have a $\frac{\mathrm{d}}{\mathrm{d}x}$ derivative, then do not use a dot.

::::

Equations of linear motion in 3-D:

$$
\vec{r} = x\hat{\imath} + y\hat{\jmath} + z\hat{k} = \langle x,y,z\rangle
$$

$$
\vec{v} = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} = \dot{\vec{r}} = \frac{\mathrm{d}x}{\mathrm{d}t} \hat{\imath} + \frac{\mathrm{d}y}{\mathrm{d}t} \hat{\jmath} + \frac{\mathrm{d}z}{\mathrm{d}t} \hat{k} = \Bigg\langle \frac{\mathrm{d}x}{\mathrm{d}t}, \frac{\mathrm{d}y}{\mathrm{d}t}, \frac{\mathrm{d}z}{\mathrm{d}t} \Bigg\rangle
$$

$$
\vec{a} = \frac{\mathrm{d}\vec{v}}{\mathrm{d}t} = \frac{\mathrm{d}^{2}\vec{r}}{\mathrm{d}t^{2}} = \ddot{\vec{r}} = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} \hat{\imath} + \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} \hat{\jmath} + \frac{\mathrm{d}^{2}z}{\mathrm{d}t^{2}} \hat{k} = \Bigg\langle \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}, \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}, \frac{\mathrm{d}^{2}z}{\mathrm{d}t^{2}} \Bigg\rangle
$$

The above equations highlight that there are several ways to write a parameter in vector notation. For example, $\vec{r}$ can be expressed as $x\hat{\imath} + y\hat{\jmath} + z\hat{k}$ or $\langle x,y,z\rangle$. You should try to be consistent within a problem so that there is less chance for confusion or error in your solutions.

::::{admonition} Definitions

The time derivative of position gives you *instantaneous* velocity and the time derivative of velocity gives you the *instantaneous* acceleration. These are instantaneous because they correspond to the velocity or acceleration in that exact instant or moment in time. By contrast, the *average* velocity $(\bar{v} = \frac{\Delta \vec{r}}{\Delta t})$ and *average* acceleration $(\bar{a} = \frac{\Delta \vec{v}}{\Delta t}$ ) are measured over a longer duration of time, $\Delta$t. The average quantity is denoted by a bar (–) over the variable.

Note that in the limit as $\Delta t \rightarrow 0, \frac{\Delta \vec{r}}{\Delta t} \rightarrow \vec{v}$ and $\frac{\Delta v}{\Delta t} \rightarrow \vec{a}$. So for a very short duration of time, $\Delta t \rightarrow$ d$t$, the average velocity and average acceleration are equivalent to the instantaneous quantities.

::::

::::{tip} Quick Questions

1. If your velocity is constant between $t_{1}$ and $t_{2}$, how does your instantaneous velocity at $t = t_{2}$ compare to the average velocity between $t_{1}$ and $t_{2}$?

2. If your acceleration is constant between $t_{1}$ and $t_{2}$, is the instantaneous velocity at $t = t_{2}$ the same as the average velocity between $t_{1}$ and $t_{2}$?

::::

<!-- Source PDF page 13; printed label 4. -->

(sec-1-1-2)=
### 1.1.2 Rotational Motion

Rotational motion is when you have a body spinning about a rotation axis.

:::{figure} ../images/figures/figure-1-2.png
:label: fig-1-2
:enumerator: 1.2
:alt: Figure shows the circular motion of a point on a rigid body that rotates about the z-axis.
:width: 146px

For a rigid body rotating on a fixed axis, a point $P$ on the body will travel in a circle with radius $r$ about the rotation axis.
:::

For rotational motion, it is useful to describe the motion in terms of angles: angular position $(\theta)$, angular velocity $(\omega)$, and angular acceleration $(\alpha)$. Note that a radius $r$ is also necessary to describe the motion, and we will assume this is constant for now. For this coordinate system to work, you need a reference axis (reference point).

Consider the figure below. In time $t_{1}$ to $t_{2}$ the object has rotated from the first position at $\theta _{1}$ to the second position at $\theta _{2}$. The distance from the origin to both points (radius) is constant. Thus, the angular position that the object moves is $\Delta \theta = \theta _{2}- \theta _{1}$ in time $\Delta t = t_{2}- t_{1}$. The distance traveled is the arc, $s$, as traced out by the angle $\Delta \theta$.

:::{figure} ../images/figures/figure-1-3.png
:label: fig-1-3
:enumerator: 1.3
:alt: Figure compares the change in angle and the arc length from a rotating point on a 2D Cartesian plane.
:width: 390px

Left panel shows the change in angular position $(\Delta \theta)$ that the object moves. The right panel defines the arc, $S$.
:::

::::{admonition} Definitions

The above example defines $\theta$ as increasing counter-clockwise. It is important that you define your axes at the start and that you keep consistent with that defined reference axis.

::::

For angular motion, we generally measure angles in radians not degrees. One complete circle is when $\theta = 2\pi$ or $s = 2\pi r$ (the perimeter of a circle). Note that a complete rotation does not start back at $\theta$ = 0.

<!-- Source PDF page 14; printed label 5. -->

$2\pi$ rad = $360^{\circ}$ = 1 revolution

1 rad = $57.296^{\circ}= 0.159$ revolutions

The average angular velocity of the object is then given by $\bar{\omega} = \frac{\Delta \theta}{\Delta t}$. As we shrink $\Delta t$ to a very small time interval $(\Delta t \rightarrow$ d$t)$, then we get the instantaneous angular velocity or the angular velocity, $\omega$. The angular velocity is given by the time derivative of $\theta$ and the angular acceleration is given by the time derivative of the angular velocity.

$$
\omega = \frac{\mathrm{d}\theta}{\mathrm{d}t} = \dot{\theta}
$$

$$
\alpha = \frac{\mathrm{d}\omega}{\mathrm{d}t} = \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} = \ddot{\theta}
$$

The units of $\omega$ is rad $\mathrm{s}^{-1}$ and the units of $\alpha$ are rad $\mathrm{s}^{-2}$, although we often drop the radians and give $\mathrm{s}^{-1}$ and $\mathrm{s}^{-2}$, respectively. If you see $\mathrm{s}^{-1}$ or $\mathrm{s}^{-2}$ for $\omega$ and $\alpha$, the radians are implied.

For a rigid body, all points in the object move with the same angular velocity and angular acceleration because every point is moving together (the object doesn’t deform during rotation).

::::{tip} Quick Questions

1. What is the angle $\theta$ (in radians) for two complete rotations?

2. A wheel with radius of 1 m rotates at 2.5 revolutions per second. What is the angular displacement (in radians) of the wheel after 1 minute?

::::

(sec-1-2)=
## 1.2 Introduction to Plane Polar Coordinates

In cases of circular motion, it is often easier to solve a problem by changing your coordinate system from Cartesian plane $(x,y)$ to polar coordinates $(r,\theta)$. The two coordinate systems are connected, where $x = r\cos \theta$ and $y = r\sin \theta$, where $r$ is the radius length and $\theta$ is the polar angle (see [Figure 1.4](#fig-1-4)). Solving for $r$ and $\theta$, we get:

$$
\begin{aligned}
r &= \sqrt{x^{2}+y^{2}} \\
\theta &= \tan^{-1}\Bigg(\frac{y}{x}\Bigg)
\end{aligned}
$$

Of course, $r$ and $\theta$ are vector quantities, where $\hat{r}$ points away from the origin of the system and $\hat{\theta}$ is orthogonal to $\hat{r}$ in the counter-clockwise direction (usually). Note that the hat symbol indicates a unit vector (direction only). [Figure 1.4](#fig-1-4) shows these vector directions.

The position vector in plane polar coordinates can be written as $\vec{r} = r\hat{r}$ and the angle vector can be written as $\vec{\theta} = \theta \hat{\theta}$ .

<!-- Source PDF page 15; printed label 6. -->

:::{figure} ../images/figures/figure-1-4.png
:label: fig-1-4
:enumerator: 1.4
:alt: Figure 1.4 from the source textbook
:width: 228px

Visual definitions of $\hat{r}$ and $\hat{\theta}$ in plane polar coordinates. The unit vector for radius extends away from the origin and the unit vector for angle points counter clockwise. Note that $\hat{\theta}$ is always tangent to the radius by definition.
:::

::::{admonition} Real World Applications

Aircraft and naval navigation are both based on cylindrical coordinate systems, using a distance (radius), direction (angle), and altitude or depth $(z)$. These coordinate systems are often slightly modified to use North, either magnetic or true, as the zero angle. The use of polar coordinates are helpful in putting context to the positions of objects and obstacles relative to the moving vehicle.

::::

Now we want to find an equation for $\vec{v}$ and $\vec{a}$ in polar coordinates instead of Cartesian coordinates. This is a variation of how we defined velocity and acceleration previously (because previously we used Cartesian coordinates).

Let’s look at velocity first.

$$
\vec{v} = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} = \frac{\mathrm{d}(r\hat{r})}{\mathrm{d}t} = \frac{\mathrm{d}r}{\mathrm{d}t} \hat{r} + r \frac{\mathrm{d}\hat{r}}{\mathrm{d}t}
$$

where $\frac{\mathrm{d}\hat{r}}{\mathrm{d}t} \not =$ 0. Consider the line moving in [Figure 1.4](#fig-1-4). The $\hat{r}$ unit vector will point in a different direction as the radius vector moves around the circle.

[Figure 1.5](#fig-1-5) defines the $\hat{r}$ and $\hat{\theta}$ unit vectors in terms of Cartesian axes. Both $\hat{r}$ and $\hat{\theta}$ have components in $x$ and $y$.

$$
\hat{r} = \cos \theta \hat{\imath} + \sin \theta \hat{\jmath}
$$

$$
\hat{\theta} = -\sin \theta \hat{\imath} + \cos \theta \hat{\jmath}
$$

Note that the Cartesian unit vectors $(\hat{\imath}, \hat{\jmath}$ ) are fixed, whereas the polar-axes $(\hat{r}, \hat{\theta}$ ) are moving relative to them because the radial vectors is moving.

<!-- Source PDF page 16; printed label 7. -->

:::{figure} ../images/figures/figure-1-5.png
:label: fig-1-5
:enumerator: 1.5
:alt: Figure 1.5 from the source textbook
:width: 228px

Sketch showing how $\hat{r}$ and $\hat{\theta}$ can be described in terms of $\hat{\imath}$ and $\hat{\jmath}$ . Note that the Cartesian system $(\hat{\imath}$ and $\hat{\jmath}$ ) do not change with time, but the plane polar system $(\hat{r}$ and $\hat{\theta}$ ) do change with time.
:::

If we take the derivative of $\hat{r}$ with respect to time, we get:

$$
\begin{aligned}
\frac{\mathrm{d}\hat{r}}{\mathrm{d}t}
&= \frac{\mathrm{d}}{\mathrm{d}t}\left(\cos\theta\hat{\imath}+\sin\theta\hat{\jmath}\right) \\
&= -\sin\theta\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\imath}
  +\cos\theta\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\jmath} \\
&= \frac{\mathrm{d}\theta}{\mathrm{d}t}
  \underbrace{\left(-\sin\theta\hat{\imath}+\cos\theta\hat{\jmath}\right)}_{\hat{\theta}} \\
&= \frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}
 = \omega\hat{\theta}
\end{aligned}
$$

The above equation applies a full time derivative to $\hat{r}$ , which means that you must not only take the time derivative of $\cos \theta$ and $\sin \theta$, but also time derivative of $\theta$. See the textbook repository for a video showing the difference between full and partial derivatives.

Now that we have $\frac{\mathrm{d}\hat{r}}{\mathrm{d}t}$, we can go back to our velocity equation from before. For polar coordinates we get:

$$
\vec{v} = \frac{\mathrm{d}r}{\mathrm{d}t} \hat{r} + r \frac{\mathrm{d}\hat{r}}{\mathrm{d}t}
$$

$$
\vec{v} = \frac{\mathrm{d}r}{\mathrm{d}t} \hat{r}+r \frac{\mathrm{d}\theta}{\mathrm{d}t} \hat{\theta}
$$ (eq-1-2)

where the first term is the radial velocity component $\vec{v}_{r}$ and the second term is the tangential velocity component $\vec{v}_{\theta}$. The radial velocity component indicates how the point is moving in and out along the direction of the radius vector, whereas the tangential velocity component of the motion describes how the point is moving along a circle (motion that is tangent to the radius vector). For circular motion, the radius is constant, such that $\frac{\mathrm{d}r}{\mathrm{d}t}=0$ and you get $\vec{v}_{circ}= r\omega \hat{\theta}$ .

By definition the speed (or $|\vec{v}|$) is given by $\sqrt{\vec{v}\cdot\vec{v}}=\sqrt{v_{r}^{2}+v_{\theta}^{2}}=\sqrt{v_{r}^{2}+(r\omega)^{2}}$, using the vector dot product (see also, [Chapter 1.5.1](#sec-1-5-1)).

<!-- Source PDF page 17; printed label 8. -->

We can also take the time derivative of $\hat{\theta}$ , using the definition of $\hat{\theta}$ in Cartesian coordinates.

$$
\begin{aligned}
\frac{\mathrm{d}\hat{\theta}}{\mathrm{d}t}
&= \frac{\mathrm{d}}{\mathrm{d}t}\left(-\sin\theta\hat{\imath}+\cos\theta\hat{\jmath}\right) \\
&= -\cos\theta\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\imath}
  -\sin\theta\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\jmath} \\
&= -\frac{\mathrm{d}\theta}{\mathrm{d}t}
  \underbrace{\left(\cos\theta\hat{\imath}+\sin\theta\hat{\jmath}\right)}_{\hat{r}} \\
&= -\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{r}
 = -\omega\hat{r}
\end{aligned}
$$

For acceleration, we want the time derivative of velocity. Following a similar procedure,

$$
\begin{aligned}
\vec{a}
&= \frac{\mathrm{d}\vec{v}}{\mathrm{d}t}
 = \frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}r}{\mathrm{d}t}\hat{r}
 +r\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}\right) \\
&= \frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}\hat{r}
 +\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\hat{r}}{\mathrm{d}t}
 +\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}
 +r\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}}\hat{\theta}
 +r\frac{\mathrm{d}\theta}{\mathrm{d}t}\frac{\mathrm{d}\hat{\theta}}{\mathrm{d}t} \\
&= \frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}\hat{r}
 +\frac{\mathrm{d}r}{\mathrm{d}t}\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}\right)
 +\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}
 +r\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}}\hat{\theta}
 +r\frac{\mathrm{d}\theta}{\mathrm{d}t}\left(-\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{r}\right) \\
&= \frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}\hat{r}
 +2\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}
 +r\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}}\hat{\theta}
 -r\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)^{2}\hat{r} \\
&= \left[\frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}
 -r\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)^{2}\right]\hat{r}
 +\left(r\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}}
 +2\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)\hat{\theta}
\end{aligned}
$$ (eq-1-3)

where the first term is the acceleration in the radial direction $(a_{r})$ and the second term is the acceleration in the tangential direction $(a_{\theta})$. That is:

$$
\vec{a}_{r}= \Bigg[\frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}} - r\Bigg(\frac{\mathrm{d}\theta}{\mathrm{d}t} \Bigg)^{2}\Bigg]\hat{r}
$$

$$
\vec{a}_{\theta}= \Bigg(r \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + 2 \frac{\mathrm{d}r}{\mathrm{d}t} \frac{\mathrm{d}\theta}{\mathrm{d}t} \Bigg)\hat{\theta}
$$

These acceleration terms are key in rotating reference frames ([Chapter 5](#ch-5)).

::::{tip} Quick Questions

1. Consider an object moving such that $\theta$ is constant with time. What is the acceleration term in this case? Does this make sense?

2. Consider a simple pendulum in plane polar coordinates. How does the radial acceleration $(\vec{a}_{r})$ change as a function of time? Comment.

::::

<!-- Source PDF page 18; printed label 9. -->

(sec-1-3)=
## 1.3 Equations of Motion

In the previous section, we defined the positions, velocities, and accelerations for linear and circular motion. To describe the motion, however, you need to solve these equations.

$$
\vec{v} = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} =\Rightarrow \vec{r} = \int \vec{v} \mathrm{d}t
$$

$$
\vec{a} = \frac{\mathrm{d}\vec{v}}{\mathrm{d}t} =\Rightarrow \vec{v} = \int \vec{a} \mathrm{d}t
$$

$$
\omega = \frac{\mathrm{d}\theta}{\mathrm{d}t} =\Rightarrow \theta = \int \omega \mathrm{d}t
$$

$$
\alpha = \frac{\mathrm{d}\omega}{\mathrm{d}t} =\Rightarrow \omega = \int \alpha \mathrm{d}t
$$

The solutions to these integrals depends on how the system moves with time. For example, consider the case when $\alpha$ and $\vec{a}$ are constant with time. Let’s look at the case of linear motion with constant acceleration in 1-D so that we can drop the vector notation.

$$
v_{x}= \int a_{x}\,\mathrm{d}t
$$

$$
v_{x}= a_{x}t + C_{1}
$$

where $a_x$ is constant by definition and $C_{1}$ is a constant of integration.

$$
x = \int v_{x}\,\mathrm{d}t
$$

$$
x = \int (a_{x}t + C_{1})\,\mathrm{d}t
$$

where we have substituted the equation for $v_x$. Integrating gives

$$
x = \frac{1}{2}a_{x}t^{2}+C_{1}t+C_{2},
$$

where $C_{2}$ is a constant of integration.

The constant $C_{1}$ is the initial velocity $v_{x,0}$ (at $t$ = 0) and $C_{2}$ is the initial position $x_{0}$ (at $t$ = 0). Subbing in those definitions for the constants of integration, we get:

$$
v_{x}= a_{x}t + v_{x,0}
$$

$$
x = \frac{1}{2} a_{x}t^{2}+ v_{x,0}t + x_{0}
$$

Hopefully these equations look familiar. Of course, since position and velocity are vectors quantities, you need to solve for the motion along the different coordinate axes (e.g., $x,y,z)$ separately. For example, the acceleration may be zero along one axis and non-zero along another axis (e.g., such is the case with gravity).

Note that if you take the time derivative of $x = \frac{1}{2} a_{x}t^{2}+v_{x,0}t+x_{0}$, you recover the equation for $v_{x}= a_{x}t + v_{x,0}$ as you should. In general, it is a good idea to check the consistency of your equations.

<!-- Source PDF page 19; printed label 10. -->

::::{admonition} Definitions

The above equations of motion for $v_{x}$ and $x$ (and the equivalent for $y$ and $z)$ are only applicable if the acceleration is constant. If your acceleration is changing as a function of time, then the above equations will not apply and you need to solve the equations of motion (see [Chapter 2](#ch-2)).

::::

::::{admonition} Real World Applications

We typically use Standard Internation (SI) units to describe position, velocity, acceleration, and time. But historically and around the world, there have been may different ways of looking at those measurements. One interesting example is the water clock from the Babylonian Empire, where time had the same units as mass. These clocks used the weight of water passing through the clock as a measure of time. Since the Babylonian Empire wasn’t directly on the equator, the amount of water used to break up the day had to be adjusted throughout the year.

::::

(sec-1-4)=
## 1.4 Linear and Rotational Motion

We can also connect circular motion to linear motion. Consider two points associated with rotational motion with a circular radius of $r_{0}$ as shown below.

:::{figure} ../images/figures/figure-1-6.png
:label: fig-1-6
:enumerator: 1.6
:alt: Figure 1.6 from the source textbook
:width: 205px

The system is rotating from position $\theta _{1}$ to $\theta _{2}$. The vectors $\vec{r}_{1}$ and $\vec{r}_{2}$ represent those two positions. Note that $|\vec{r}_{1}| = |\vec{r}_{2}|$ in this simple case.
:::

We can write the radius vectors in terms of their $x$ and $y$ values. For example, $x_{1}= r_{1}\cos \theta _{1}$ and $y_{1}= r_{1}\sin \theta _{1}$. The same can be applied to the second position. In vector form, we get:

$$
\vec{r} = x(t)\hat{\imath} + y(t)\hat{\jmath}
$$

$$
\vec{r} = r_{0}\cos \theta \hat{\imath} + r_{0}\sin \theta \hat{\jmath}
$$

For circular motion, $\theta$ changes with time. Let’s consider the simplest case where $\dot{\theta} = \omega$ = constant, such that we can solve for $\theta (t)$ as $\theta = \int \omega$d$t = \omega t + \theta _{0}$, where $\theta _{0}$ is a constant of integration and represents the initial angle. It is often convenient to define the initial angle as $\theta _{0}$ = 0 so $\theta (t) = \omega t$. Therefore, we get:

$$
\vec{r}=\underbrace{r_{0}\cos(\omega t)}_{x(t)}\hat{\imath}
+\underbrace{r_{0}\sin(\omega t)}_{y(t)}\hat{\jmath}
$$ (eq-1-4)

<!-- Source PDF page 20; printed label 11. -->

We can then look at the velocity and acceleration of the system by just taking the time derivatives of $\vec{r}$.

$$
\begin{aligned}
\vec{v} &= \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \\
\vec{v} &= [-r_{0}\omega \sin (\omega t)]\hat{\imath} + [r_{0}\omega \cos (\omega t)]\hat{\jmath}
\end{aligned}
$$

$$
\begin{aligned}
\vec{a} &= \frac{\mathrm{d}\vec{v}}{\mathrm{d}t} \\
\vec{a} &= \Big[-r_{0}\omega ^{2}\cos (\omega t)\Big]\hat{\imath} + \Big[-r_{0}\omega ^{2}\sin (\omega t)\Big]\hat{\jmath}
\end{aligned}
$$

$$
\vec{a} = -\omega ^{2}\vec{r}
$$

::::{tip} Quick Questions

1. Show that the speed $|\vec{v}|$ in the above example is equal to $\omega r_{0}$.

2. For constant $\omega$, compare the linear acceleration $\vec{a}$ to the angular acceleration $\alpha$?

::::

(example-1-1)=

::::{admonition} Sample Problem 1-1

You throw a ball straight up into the air with a constant velocity of $v_{0}$ and at an initial height of $r_{0}$. **(1) What is the maximum height that the ball reaches? (2) How** **long does it take for the ball to hit the ground?**

**Solution**

This is a 1-D motion problem under constant acceleration $(a = -g \hat{y}$ ). First consider how the ball will move. For vertical motion upward with a downward acceleration, the ball will initially rise. But due to the pull downward by gravity, the ball will slow down, and then momentarily come to a stop $(v$ = 0 at the crest of motion) before it falls back down again, accelerating as it falls. [Figure 1.7](#fig-1-7) shows a cartoon of this motion.

:::{figure} ../images/figures/figure-1-7.png
:label: fig-1-7
:enumerator: 1.7
:alt: Figure displays the vertical motion of a ball.
:width: 248px

Cartoon of 1-D vertical motion.
:::

$$
\mathrm{For} \mathrm{vertical} \mathrm{motion} \mathrm{upward} \mathrm{with} \mathrm{an} \mathrm{ac}-
$$

$$
\mathrm{celeration} \mathrm{downward}, \mathrm{the} \mathrm{ball} \mathrm{rises} \mathrm{ini}-
$$

$$
\mathrm{tially} (\mathrm{A} \rightarrow \mathrm{B}) \mathrm{and} \mathrm{slows} \mathrm{down} \mathrm{as} \mathrm{it}
$$

$$
\mathrm{moves} \mathrm{upward} \mathrm{until} \mathrm{it} \mathrm{has} v = 0 (\mathrm{point}
$$

$$
\mathrm{B} \mathrm{at} \mathrm{the} \mathrm{peak}), \mathrm{before} \mathrm{it} \mathrm{falls} \mathrm{back} \mathrm{down}
$$

$$
\mathrm{again} (\mathrm{B} \rightarrow \mathrm{D}).
$$

::::

<!-- Source PDF page 21; printed label 12. -->

Note that we are using the $y$ axis only at this time because all the motion is in the vertical.

1. **What is the maximum height that the ball reaches?** This is the height at point B in [Figure 1.7](#fig-1-7). This problem is a linear motion question with constant acceleration. We just solved that equation in [Section 1.3](#sec-1-3), so we will need to use the equation, $y = \frac{1}{2} at^{2}+ v_{y,0}t + r_{0}$ to solve for $y$ when the ball is at its heights point. We aren’t given that time when this happens, but we can solve for it, because when the ball has reached its maximum height, $v_{y}$ = 0 (requirement of the physics). So the first step is to get the time when the ball has reached its maximum height.

$$
v_{y}= at + v_{y,0}=\Rightarrow \mathrm{see} \mathrm{Section} 1.3
$$

$$
\begin{aligned}
0 &= at + v_{y,0}=\Rightarrow \mathrm{set} v_{y}= 0 \mathrm{at} \mathrm{the} \mathrm{maximum} \mathrm{height} \\
t &= - \frac{v_{y,0}}{a} \\
t &= \frac{v_{y,0}}{g} \\
&=\Rightarrow \mathrm{because} a = -g
\end{aligned}
$$

For simplicity, we can drop the vector notation because everything is happening in 1-D. Here positive corresponds to $+\hat{y}$ and negative corresponds to $-\hat{y}$ .

So now we have the time when the ball reaches the maximum height. We can put this time into our distance equation to solve for the maximum height.

$$
\begin{aligned}
y &= \frac{1}{2} at^{2}+ v_{y,0}t + r_{0} \\
y &= \frac{1}{2} (-g)\Bigg(\frac{v_{y,0}}{g} \Bigg)^{2}+ v_{y,0}\Bigg(\frac{v_{y,0}}{g} \Bigg) + r_{0}=\Rightarrow t = \frac{v_{y,0}}{g}, a = -g
\end{aligned}
$$

$$
\begin{aligned}
y &= - \frac{1}{2} \Bigg(\frac{v_{y,0}^{2}}{g} \Bigg) + \Bigg(\frac{v_{y,0}^{2}}{g} \Bigg) + r_{0} \\
&=\Rightarrow \mathrm{simplify}
\end{aligned}
$$

$$
y = \frac{1}{2} \Bigg(\frac{v_{y,0}^{2}}{g} \Bigg) + r_{0}
$$

Now we have our equation for the maximum height given our initial velocity $v_{y,0}$ and initial height $r_{0}$. This is the generic solution for all initial values of $v_{y,0}$ and $r_{0}$. If you are given these quantities, you can plug them in to solve the problem.

<!-- Source PDF page 22; printed label 13. -->

::::{tip} Quick Questions

(a) Check the dimensional analysis for $t$ and $y$ in the above equations. (b) What is the maximum height of a ball when $v_{y,0}$ = 10 m $\mathrm{s}^{-1}$ and $r_{0}= 1.8$

$$
\mathrm{m} (\mathrm{assume} g = 9.8 \mathrm{m} \mathrm{s}^{-2})?
$$

(c) Consider the case where the acceleration is positive, not negative. What

$$
\mathrm{does} t = \frac{-v_{y,0}}{a} \mathrm{mean} \mathrm{for} \mathrm{a} \mathrm{positive} \mathrm{acceleration}?
$$

::::

2. **How long does it take for the ball to reach the ground?** So this is at the end of the motion (point D in [Figure 1.7](#fig-1-7)). We don’t know the speed at which the ball reaches the ground or the time, but we do know the ball hits the ground when $y$ = 0. So we want to solve for the time when $y$ = 0. Using the height equation, we get $y = - \frac{1}{2} gt^{2}+ v_{y,0}t + r_{0}$ = 0, which is a quadratic equation. The solution for a quadratic equation of the form 0 = $Ax^{2}+ Bx + C$ is:

$$
x = \frac{-B \pm \sqrt{B^{2}- 4AC}}{2A}
$$

In this case, $t$ is our variable, $A = - \frac{1}{2} g, B = v_{y,0}$, and $C = r_{0}$. Plugging those numbers in gives:

$$
t = \frac{v_{y,0}\pm\sqrt{v_{y,0}^{2}+2gr_{0}}}{g}
$$

There are two solutions. Since $2gr_{0}$ is positive, the term $\sqrt{v_{y,0}^{2}+2gr_{0}}>v_{y,0}$ for all values of $v_{y,0}$ and $r_{0}$. So there will be one value of $t > 0$ and one value of $t < 0$. The latter case $(t < 0)$ is unphysical given the set up of this problem, however. While it mathematically solves the problem, we know that the ball’s motion started from a height $r_{0}$ at $t$ = 0. Effectively, the $t < 0$ case corresponds to the time when the ball would need to be thrown from $y$ = 0 such that it has a speed of $v_{y,0}$ at $t$ = 0 and height $r_{0}$. But that wasn’t our question, so we are instead interested in the $t > 0$ case.

So our solution to this problem is:

$$
t = \frac{v_{y,0}+\sqrt{v_{y,0}^{2}+2gr_{0}}}{g}
$$

Here we drop the $-$ case because it is unphysical.

<!-- Source PDF page 23; printed label 14. -->

::::{tip} Quick Questions

(a) Check the dimensional analysis for $t$ from the quadratic equation.

(b) What is the velocity of the ball when it hits the ground?

(c) What is the velocity of the ball at point C in Figure 1.7?

::::

(example-1-2)=

::::{admonition} Sample Problem 1-2

A wheel rotating at an angular speed of $\omega _{0}$ is allowed to decelerate. After $\tau$ seconds the new angular speed is $\omega _{\tau}$. If the angular acceleration is constant, **how long does** **it take the wheel to come to rest and how many revolutions does the wheel** **make before coming to a rest?**

**Solution**

Let’s first consider the motion. The wheel is fixed in place and spinning along an axis. The rate at which it is spinning is slowing down with time, but we do not know the angular acceleration (only that it is negative). We also do not know how long it takes to come to rest. But we are given the initial angular speed $(\omega _{0})$, and the speed $\omega _{\tau}$ at a specific time $\tau$, where $\omega _{0}> \omega _{\tau}$. We also know the final angular speed $\omega _{t}$ = 0 at time $t$.

To solve this problem, we need to look at equations for angular motion. With constant angular acceleration, these have the same form as the equations for rotational motion that we went through earlier in [Section 1.2](#sec-1-2).

$$
\omega = \alpha t + \omega _{0}, \theta = \frac{1}{2} \alpha t^{2}+ \omega _{0}t + \theta _{0}
$$

1. **How long does it take the wheel to come to a rest?** We will use the equation for angular speed to solve this problem. (You may notice a degree of similarity with the last problem. This was intentional to show the how similar problems can have slight differences in answers and methodology.)

Here, we don’t know $\alpha$ or $t$. If we set $\omega$ = 0 at time $t$, we have 0 = $\alpha t+\omega _{0}$, where the only known quantity is $\omega _{0}$. But we can solve for $\alpha$ because we are told that the acceleration is constant. That means that the instantaneous acceleration at any time is equal to the average acceleration between any fixed time. Between $t$ = 0 and $t = \tau$, the angular velocity decreased from $\omega _{0}$ to $\omega _{\tau}$ such that the average acceleration is:

::::

<!-- Source PDF page 24; printed label 15. -->

::::{admonition} Continued

$$
\alpha = \frac{\Delta \omega}{\Delta t}
$$

$$
\alpha = \frac{\omega _{\tau}- \omega _{0}}{\tau} =\Rightarrow \mathrm{for} \omega _{0}\mathrm{at} t = 0 \mathrm{to} \omega _{\tau}\mathrm{at} t = \tau
$$

Now that we have $\alpha$, we can solve for the time at which the wheel has reached rest.

$$
\begin{aligned}
t &= - \frac{\omega _{0}}{\alpha} =\Rightarrow 0 = \alpha t + \omega _{0}\mathrm{as} \mathrm{given} \mathrm{above} \\
t &= - \frac{\omega _{0}\tau}{\omega _{\tau}- \omega _{0}} =\Rightarrow \mathrm{sub} \mathrm{in} \mathrm{the} \mathrm{equation} \mathrm{for} \alpha
\end{aligned}
$$

Note that for $t > 0$, you must have $\omega _{\tau}< \omega _{0}$ (true by definition).

2. **How many revolutions does the wheel make before coming to a rest?** This is a question of how large an angle, $\theta$, the wheel rotates through. In [Section 1.1.2](#sec-1-1-2), we defined revolutions and angular displacement. Recall the quick question in [Section 1.1.2](#sec-1-1-2) about how many radians are in 2 revolutions and 3 revolutions.

To get the total angular displacement $(\Delta \theta)$ from $t$ = 0 until the wheel comes to rest at $t$, we can use the above equation for $\theta$, because we have $\alpha, t$, and $\omega _{0}$.

$$
\begin{aligned}
\Delta\theta
&= \frac{1}{2}\alpha t^{2}+\omega_{0}t+\theta_{0} \\
&= \frac{1}{2}\left(\frac{\omega_{\tau}-\omega_{0}}{\tau}\right)
   \left(-\frac{\omega_{0}\tau}{\omega_{\tau}-\omega_{0}}\right)^{2}
   +\omega_{0}\left(-\frac{\omega_{0}\tau}{\omega_{\tau}-\omega_{0}}\right) \\
&= \frac{1}{2}\left(\frac{\omega_{0}^{2}\tau}{\omega_{\tau}-\omega_{0}}\right)
   -\left(\frac{\omega_{0}^{2}\tau}{\omega_{\tau}-\omega_{0}}\right) \\
&= -\frac{1}{2}\left(\frac{\omega_{0}^{2}\tau}{\omega_{\tau}-\omega_{0}}\right)
\end{aligned}
$$

Note that we are interested in the angular displacement. As such, the initial angle $\theta _{0}$ does not matter. We are counting revolutions from $t$ = 0 where $\theta _{0}$ is our reference angle and set to $\theta _{0}$ = 0.

(a) How many revolutions do you get if $\omega _{0}$ = 240 revolutions per minute,

$$
\omega _{\tau}= 180 \mathrm{revolutions} \mathrm{per} \mathrm{minute}, \mathrm{and} \tau = 10 \mathrm{s}?
$$

(b) How many revolutions do you get if $\omega _{0}$ = 19 radians per second, $\omega _{\tau}$ = 12

$$
\mathrm{radians} \mathrm{per} \mathrm{second}, \mathrm{and} \tau = 1 \mathrm{minute}?
$$

::::

<!-- Source PDF page 25; printed label 16. -->

(sec-1-5)=
## 1.5 Vector Calculus

(sec-1-5-1)=
### 1.5.1 Vector Dot Product

For any two vectors, $\vec{a} = x_{a}\hat{\imath} + y_{a}\hat{\jmath} + z_{a}\hat{k}$ and $\vec{b} = x_{b}\hat{\imath} + y_{b}\hat{\jmath} + z_{b}\hat{k}$ , the vector dot product (also called the vector scalar product) is given by:

$$
\vec{a} \cdot \vec{b} = x_{a}x_{b}+ y_{a}y_{b}+ z_{a}z_{b}
$$

Since the dot product is just scalar multiplication of terms, vector order does not matter

$$
(\mathrm{e.g}., \vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}).
$$

In principle, the dot product represents the projection of one vector onto the other. For example, when you want to calculate the $x-$component of a vector, you take the projection of that vector on the $x-$axis. This is equivalent to $\vec{a} \cdot \hat{\imath}$, where only the $x-$component is retained.

The dot product can also be expressed as:

$$
\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos \theta
$$

where $|\vec{a}|$ is the magnitude of $\vec{a}, |\vec{b}|$ is the magnitude of $\vec{b}$ and $\theta$ is the angle between the two vectors when the vectors are tail-to-tail. So the angle between any two vectors can be calculated from:

$$
\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}
$$

A vector magnitude is given by:

$$
b=|\vec{b}|=\sqrt{b_{x}^{2}+b_{y}^{2}+b_{z}^{2}}
$$

which is essentially the dot product of a vector with itself $(\theta$ = 0).

$$
b^{2}= |\vec{b}|^{2}= \vec{b} \cdot \vec{b}
$$

(sec-1-5-2)=
### 1.5.2 Vector Cross Product

For any two vectors, $\vec{a}$ and$\vec{b}$, the vector cross product is given by:

$$
\vec{c} = \vec{a} \times \vec{b}
$$

Unlike the dot product, the vector cross product results in a vector, which has both magnitude and direction, and the vector $\vec{c}$ is perpendicular to both $\vec{a}$ and $\vec{b}$. In other words, the vector cross product $\vec{c}$ is normal (perpendicular) to a plane that is defined by $\vec{a}$ and$\vec{b}$.

The magnitude of $\vec{c}$ can be given as:

$$
|\vec{c}| = |\vec{a}||\vec{b}|\sin \theta
$$

<!-- Source PDF page 26; printed label 17. -->

where $\theta$ is the angle between the two vectors when the vectors are tail-to-tail. But this is only the magnitude. To get the direction of the cross product, you can use one of two methods: (1) the right hand rule (RHR) or (2) the matrix determinant method to solve the vector cross product.

[Figure 1.8](#fig-1-8) shows how to solve for the cross product direction with the RHR.

:::{figure} ../images/figures/figure-1-8.png
:label: fig-1-8
:enumerator: 1.8
:alt: Cartoon hand of the right hand rule for the vector cross product.
:width: 195px

Vector orientation from the right hand rule. For $\vec{a} \times \vec{b}$, align your index finger with the direction of $\vec{a}$ and your middle finger with the direction of $\vec{b}$. Your thumb then points in the direction given by $\vec{a} \times \vec{b}$.
:::

The matrix determinant method gives you the full vector solution for the cross product:

$$
\begin{aligned}
\hat{\imath} \hat{\jmath} \hat{k} \\
\vec{a} \times \vec{b} &= |a_{x}a_{y}a_{z}| \\
b_{x}b_{y}b_{z} \\
&= (a_{y}b_{z}- a_{z}b_{y})\hat{\imath} + (a_{z}b_{x}- a_{x}b_{z})\hat{\jmath} + (a_{x}b_{y}- a_{y}b_{x})\hat{k}
\end{aligned}
$$

For the vector cross product, order matters. Here are a few helpful identities:

$$
\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}
$$

$$
\vec{c} \times (\vec{a} + \vec{b}) = (\vec{c} \times \vec{a}) + (\vec{c} \times \vec{b})
$$

$$
n(\vec{a} \times \vec{b}) = (n\vec{a}) \times \vec{b} = \vec{a} \times (n\vec{b}) = (\vec{a} \times \vec{b})n
$$

::::{admonition} Definitions

In general, angular velocity $(\omega)$ and angular acceleration $(\alpha)$ are vectors, although we often drop the vector symbol. The true definition of these terms are:

$$
\begin{aligned}
\vec{\omega} &= \frac{\vec{r} \times \vec{v}}{r^{2}} \\
\vec{\alpha} &= \frac{\vec{r} \times \vec{a}}{r^{2}}
\end{aligned}
$$

where the direction is given by the right-hand rule. For rotational motion:

:::{image} ../images/figures/figure-p026-2.png
:alt: Cartoon of the angular momentum vector with rotation direction.
:width: 124px
:align: center
:::

$$
=\Rightarrow \mathrm{curl} \mathrm{your} \mathrm{fingers} \mathrm{in} \mathrm{direction} \mathrm{of} \mathrm{rotation}
$$

$$
=\Rightarrow \mathrm{thumb} \mathrm{points} \mathrm{in} \mathrm{the} \mathrm{direction} \mathrm{of} \vec{\omega}
$$

::::

<!-- Source PDF page 27; printed label 18. -->

(sec-1-6)=
## 1.6 Approximations

In physics, you can often make approximations to simplify the math based on the conditions of your system. For example, if you have a complicated force acting on a system, but you are only interested in short distances or short times, you can often simplify the equation for that force making the calculations easier. Deviations between the true value (considering the full complicated force equation) and the approximation (with the simplified force equation) would be considered small, such that you get a good idea of how the system will move without needing to do the complicated math. (Of course, with some high-precision physics, you cannot make this approximation.)

A very common approach is to use the Taylor series expansion. The idea here is that any function can be broken up into a series of polynomials following:

$$
\begin{aligned}
f(x) &= f(x_{0}) + \frac{\mathrm{d}f(x_{0})}{\mathrm{d}x} (x - x_{0}) + \frac{1}{2} \frac{\mathrm{d}^{2}f(x_{0})}{\mathrm{d}x^{2}} (x - x_{0})^{2}+ \\
\frac{1}{3!} \frac{\mathrm{d}^{3}f(x_{0})}{\mathrm{d}x^{3}} (x - x_{0})^{3}+ \cdot \cdot \cdot + \frac{1}{n!} \frac{\mathrm{d}^{n}f(x_{0})}{\mathrm{d}x^{n}} (x - x_{0})^{n}
\end{aligned}
$$ (eq-1-5)

where $f(x)$ is the function and $x_{0}$ is a reference value for the function and the ! symbol is the factorial symbol. That is $f(x)$ describes the entire function for all values $x$, whereas $f(x_{0})$ is the value of the function at the specific value of $x = x_{0}$. See [Appendix B.2](#sec-B-2) for more details and other approximation techniques.

For Equation 1.5, consider values of $x \approx x_{0}$. That is, you are only looking at cases of your variable, $x$ when it is close to your reference value. In this case, $x-x_{0}$ is small. Thus, higher order terms like $(x-x_{0})^{2}$ and $(x-x_{0})^{3}$ are very small and can be dropped. Suddenly, your function has become very simple.

Let’s look at an example. Consider the Taylor series expansion for $e^{x}$ for small values of $x$. In this case, we can set $x_{0}$ = 0 because we are looking at small values of $x$. The expansion

$$
\mathrm{is}:
$$

$$
f(x) \approx f(0) + f^{\prime}(0)(x) + \frac{1}{2} f^{\prime \prime}(0)(x)^{2}+ \frac{1}{3!} f^{\prime \prime \prime}(0)(x)^{3}+ \cdot \cdot \cdot +
$$

where $f^{\prime }(0)$ means take the derivative of $f(x)$ with respect to $x$ and evaluate that for $x$ = 0. For $f = e^{x}$, we have:

$$
f(0) = e^{0}= 1
$$

$$
\begin{aligned}
f^{\prime}(0) &= e^{0}= 1 =\Rightarrow \frac{\mathrm{d}e^{x}}{\mathrm{d}x} = e^{x} \\
f^{\prime \prime}(0) &= e^{0}= 1 =\Rightarrow \frac{\mathrm{d}^{2}e^{x}}{\mathrm{d}x^{2}} = e^{x}
\end{aligned}
$$

and so forth. Taking these terms, we can approximate the solution to $e^{x}$ at $x \approx 0$ as:

$$
e^{x}\approx 1 + x
$$

<!-- Source PDF page 28; printed label 19. -->

where we drop the higher order terms because if $x$ is small $(|x| \ll$ 1), then the higher order terms which have $x^{2}$ and $x^{3}$ become negligible. A function of 1 + $x$ is much simpler to work with than a function of $e^{x}$. This highlights the power of a Taylor series expansion.

[Figure 1.9](#fig-1-9) demonstrates this approximation. The figure compares a function of $e^{x}$ with a function of $1+x$. For small values of $x$ (such as $-0.3 < x < 0.3)$, the two functions are very similar. For larger values of $x$, however, the approximation breaks down. Note, however that you can include additional higher order terms when necessary. That is, $e^{x}\approx 1+x+ \frac{1}{2} x^{2}$ would give a better approximation than $e^{x}\approx 1 + x$.

:::{figure} ../images/figures/figure-1-9.png
:label: fig-1-9
:enumerator: 1.9
:alt: Graph showing how well the Taylor approximation applies to an exponetial curve.
:width: 403px

The left figure compares $y = e^{x}$ with the Taylor approximation of $y = 1+x$ for different values of $x$. The inset shows a zoom-in of the region between $x = -0.3$ and $x = 0.3$.
:::

::::{admonition} Real World Applications

A common application of Taylor Series approximations is the small angle case, where for small angles $\sin \theta \approx \theta$ and $\tan \theta \approx \theta$ (for angles in radians). In astronomy, nearby stars make small shifts in position relative to more distant background stars due to Earth’s orbit around the Sun. The size of the shift, called a stellar parallax, is measured as the angle on the sky from the apparent shift in position. From trigonometry, the parallax angle is given by $\tan \theta _{p}= \frac{Earth orbit}{star distance}$. Since stars are very far away, stellar parallaxes are very small angles $(\ll$ 1 rad), so we can simplify the parallax equation as $\theta _{p}= \frac{Earth orbit}{star distance}$. Knowing the Earth’s orbit size, we can therefore find the distances to stars by measuring their parallax angles with telescopes. For example, the *Gaia* space [telescope](https://www.esa.int/Science_Exploration/Space_Science/Gaia/Gaia_creates_richest_star_map_of_our_Galaxy_and_beyond) has measured stellar parallaxes to over 1 billion stars providing unprecedented maps of our Galaxy.

::::

See [Appendix A.3](#sec-A-3) for a list of common Taylor series approximations and [Appendix B.2](#sec-B-2) for more details on this method and other approximations. Taylor series approximations [may](https://xkcd.com/2605/) [seem confusing at first](https://xkcd.com/2605/), but they can work for you when applied properly. When we use the Taylor approximation throughout this text, think about why we are using it and how the approximation simplifies the calculations.

<!-- Source PDF page 29; printed label 20. -->

(example-1-3)=

::::{admonition} Sample Problem 1-3

Simplify the function $f(x)=\sqrt{3+e^{x}}$ assuming $x$ is very small $(x \rightarrow 0)$. Take the first two terms of the expansion only.

**Solution**

We just solved $e^{x}\approx 1+x$. So for small values of $x$, we can simplify the $e^{x}$ term. Thus,

$$
\sqrt{3+e^{x}}\approx\sqrt{3+1+x}\approx\sqrt{4+x}
$$

But we can go further. We can also simplify the square root function. The Taylor series equation will be:

$$
f(x) \approx f(0) + f^{\prime }(0)(x)
$$

taking the first two terms only. So we need to evaluate the function and the derivatives for $x$ = 0.

$$
f(0)=\sqrt{4+0}=2
$$

$$
f^{\prime}(0) = \frac{1}{2} \frac{1}{\sqrt{4 + 0}} = \frac{1}{4}
$$

Thus, our expansion becomes:

$$
\begin{aligned}
f(x)&\approx f(0)+f^{\prime}(0)(x) \\
\sqrt{3+e^{x}}&\approx 2+\frac{1}{4}x
\end{aligned}
$$

which is a much simpler function than the original one. You can visualize and calculate problems with $f(x)=2+\frac{1}{4}x$, but it is much harder to picture and use $f(x)=\sqrt{3+e^{x}}$.

::::

::::{admonition} Lance’s Thoughts

You might run across a very complicated equation you need to approximate, something that combines trigonometric and exponential or logarithmic functions, or a complex polynomial. The key is to think of it in the same way as doing a multiple integral: work from the inside out, one function at a time.

::::

<!-- Source PDF page 30; printed label 21. -->

::::{tip} Challenge Question

1. Find the first three terms of the Taylor series for $y = e^{\cos (2x)}$ assuming $x$ is close to 0. Plot the function and your approximation using a programming language. See the [online repository](https://github.com/OSTP/Dynamics_Textbook/tree/main/py_notebooks) for examples using python.

::::

::::{admonition} Number of Terms

How many terms of the Taylor series expansion should you take? Generally, it will depend on the problem and the degree of accuracy you need. The best way to determine the number of terms is to stop when you have a good representation for how a function changes. For example, if you want to know how a function is changing for small values of $x$ but the first two terms of the Taylor series expansion give you zero or a constant, then you will want to go to higher order terms.

Consider a Taylor series expansion of $\cos x$ for small values of $x$. From the first two terms, you get:

$$
f(x) \approx f(0) + f^{\prime }(0)(x)
$$

$$
\cos x\approx 1-\sin(0)(x)=1
$$

$$
\cos x \approx 1
$$

which is a constant. The first two terms alone are not helpful if you want to know how $\cos x$ varies with $x$ for small values of $x$. To get around this, add an additional term:

$$
\begin{aligned}
f(x)&\approx f(0)+f^{\prime}(0)(x)+\frac{1}{2}f^{\prime\prime}(0)(x)^{2} \\
\cos x&\approx 1-\sin(0)(x)-\frac{1}{2}\cos(0)(x)^{2} \\
\cos x&\approx 1-\frac{1}{2}x^{2}
\end{aligned}
$$

Now our expansion gives us a simple function for how $\cos x$ varies with $x$ for small values.

::::

(sec-1-7)=
## 1.7 Real-World Application: LIGO

One of the simplest, fundamental concepts in physics is the case of constant motion where $d = vt$. And this basic equation is at the core of one of the most ground-breaking discoveries in the 21st century, gravitational waves.

First predicted by Einstein in 1916, gravitational waves are a natural outcome of General Relativity and can be described as “ripples” in spacetime. They are incredibly small in

<!-- Source PDF page 31; printed label 22. -->

magnitude, where *strong* gravitational waves have magnitudes on the order of $10^{-18}$ m, which is around one thousandth the diameter of a proton. With the level of sensitivity needed, it was roughly a century between prediction and detection.

The first gravitational waves were detected on September 14, 2015 by the Laser Interferometer Gravitational-wave Observatory (LIGO) experiment. The experiment itself uses interferometry where identical laser beams reflect off mirrors and then converge on a detector producing an interference pattern (see [Figure 1.10](#fig-1-10)). When a gravitational wave passes through the Earth, it temporarily warps space and changes the distance between the mirrors which subsequently changes the arrival time of the reflected beams at the detector. LIGO can detect a change in distance between its mirrors on the order of $10^{-19}$ m.

:::{figure} ../images/figures/figure-1-10.png
:label: fig-1-10
:enumerator: 1.10
:alt: Figure 1.10 from the source textbook
:width: 644px

Cartoon showing the basic concept behind the LIGO experiment. Laser light is split into two orthogonal beams and reflects off distant mirrors that are 4 km away. The reflected light combine at a detector. The distance between the mirrors is so precise that the reflected waves should destructively interfere at the detector. A gravitational wave alters the mirror separations causing the combined wave to produce an interference pattern instead.
:::

The slight change in distance from a passing gravitational wave alters the interference pattern measured at the detector. [Figure 1.11](#fig-1-11) shows the gravitational wave signal from the first detection, which were generated by a pair of merging intermediate-mass black holes located 1.3 billion light years away. The interference pattern is often described as a “chirp”, because it rises to higher frequencies toward the end. Research into gravitation waves include LIGO in the USA, VIRGO in Italy, and GEO600 in Germany, with a third site, KAGRA, under construction in Japan. Multiple experiments all over the world are necessary to pinpoint the direction of the gravitational wave events because each site will

<!-- Source PDF page 32; printed label 23. -->

measure a difference in signal and arrival time.

:::{figure} ../images/figures/figure-1-11.png
:label: fig-1-11
:enumerator: 1.11
:alt: Figure shows the interference pattern from the first detected gravitational waves.
:width: 273px

First gravitational wave signal from LIGO. The strain $(y$ axis) indicates the fractional change in distance between the mirrors (positive means further, negative means closer) for two different experiments located in Washington and Louisiana. The lower panel overlays both experiments (with a shift in the Hanford data because the gravitational waves reached each detector at slightly different times). The thin “predicted” lines show the best-fit merging black hole model, where black holes of 36 $\mathrm{M}_{\odot}$ and 29 $\mathrm{M}_{\odot}$ merged to form a black hole of 62 $\mathrm{M}_{\odot}$. The missing mass $(\sim 3 \mathrm{M}_{\odot})$ was converted into the energy that created the gravitational waves. Credit: Caltech/MIT/LIGO Lab.
:::

LIGO is an international collaboration including more than 1200 scientists from over 100 institutions located in 18 different countries. The ground-breaking discovery has significant implications for general relativity, black holes, and our universe. But recall that the basic principle at the heart of this experiment is a change in arrival time from a change in distance.

**For more information:** The [LIGO Scientific Collaboration](https://www.ligo.org/detections/GW150914.php) website has a lot of information about the original detection and process. [This video](https://www.youtube.com/watch?v=QyDcTbR-kEA) translated the merging event into a sound bite that showcases the “chirp” from the merger. [Sky & Telescope](https://skyandtelescope.org/astronomy-news/gravitational-wave-detection-heralds-new-era-of-science-0211201644/) also has a nice article (with lots of links) describing the first detection.

<!-- Source PDF page 33; printed label 24. -->

(sec-1-8)=
## 1.8 Summary

::::{admonition} Key Takeaways

This chapter is about setting up the coordinate systems and solving for the equation of motion knowing the acceleration. This section focuses on Cartesian coordinates, where motion is described in terms of $x,y,z$:

$$
\vec{r} = x\hat{\imath} + y\hat{\jmath} + z\hat{k}
$$

$$
\vec{v} = \dot{x}\hat{\imath} + \dot{y}\hat{\jmath} + \dot{z}\hat{k}
$$

$$
\vec{a} = \ddot{x}\hat{\imath} + \ddot{y}\hat{\jmath} + \ddot{z}\hat{k}
$$

And plane-polar coordinates, where the position vector is given by $\langle r,\theta \rangle$, and the velocity is described by:

$$
\begin{aligned}
\vec{v} &= \frac{\mathrm{d}r}{\mathrm{d}t} \hat{r} + r \frac{\mathrm{d}\theta}{\mathrm{d}t} \hat{\theta} \\
\vec{a} &= \Bigg[\frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}} - r\Bigg(\frac{\mathrm{d}\theta}{\mathrm{d}t} \Bigg)^{2}\Bigg]\hat{r} + \Bigg(r \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + 2 \frac{\mathrm{d}r}{\mathrm{d}t} \frac{\mathrm{d}\theta}{\mathrm{d}t} \Bigg)\hat{\theta}
\end{aligned}
$$

where there is a radial and transverse $(\theta)$ component to velocity and acceleration.

For purely circular rotation, we the coordinates are easy to relate:

$$
\vec{r} = r_{0}\cos (\omega t)\hat{\imath} + r_{0}\sin (\omega t)\hat{\jmath}
$$

And the radial vector is constant such that:

$$
\vec{v} = r\omega \hat{\theta}
$$

$$
\vec{a} = -r\omega ^{2}\hat{r}
$$

Note that we assume that the rotation rate is not changing.

This Chapter also described the vector dot $(\vec{a}\cdot \vec{b})$ and vector cross product $(\vec{a}\times \vec{b})$, which will be used more explicitly in later chapters. The vector dot product is essentially a projection of $\vec{a}$ onto $\vec{b}$ and yields a scalar answer. The vector cross product gives the vector that is normal to the surface described by $\vec{a}$ and$\vec{b}$.

Finally, the Chapter introduced Taylor series expansion as a method to simplify complex functions. We will use this method to more efficiently solve physics problems.

::::

<!-- Source PDF page 34; printed label 25. -->

::::{admonition} Important Equations

**Cartesian Coordinates:**

$$
\begin{aligned}
\vec{r}&=x\hat{\imath}+y\hat{\jmath}+z\hat{k} \\
\vec{v}&=\dot{x}\hat{\imath}+\dot{y}\hat{\jmath}+\dot{z}\hat{k} \\
\vec{a}&=\ddot{x}\hat{\imath}+\ddot{y}\hat{\jmath}+\ddot{z}\hat{k}
\end{aligned}
$$

**Circular rotation:**

$$
\vec{r}=\underbrace{r_{0}\cos(\omega t)}_{x(t)}\hat{\imath}
+\underbrace{r_{0}\sin(\omega t)}_{y(t)}\hat{\jmath}
$$

(in Cartesian coordinates)

**Plane-Polar Coordinates:**

$$
\vec{v}=\frac{\mathrm{d}r}{\mathrm{d}t}\hat{r}
+r\frac{\mathrm{d}\theta}{\mathrm{d}t}\hat{\theta}
$$

$$
\vec{a}=\left[\frac{\mathrm{d}^{2}r}{\mathrm{d}t^{2}}
-r\left(\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)^{2}\right]\hat{r}
+\left(r\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}}
+2\frac{\mathrm{d}r}{\mathrm{d}t}\frac{\mathrm{d}\theta}{\mathrm{d}t}\right)\hat{\theta}
$$

For circular motion in plane-polar coordinates,

$$
\vec{v}=\omega r\hat{\theta}, \qquad \vec{a}=-\omega^{2}\vec{r}.
$$

**Vector Dot Product:**

$$
\vec{a} \cdot \vec{b} = x_{a}x_{b}+ y_{a}y_{b}+ z_{a}z_{b}
$$

$$
\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos \theta
$$

**Vector Cross Product:**

$$
\vec{a} \times \vec{b} = (a_{y}b_{z}- a_{z}b_{y})\hat{\imath} + (a_{z}b_{x}- a_{x}b_{z})\hat{\jmath} + (a_{x}b_{y}- a_{y}b_{x})\hat{k}
$$

$$
|\vec{a} \times \vec{b}| = |\vec{a}||\vec{b}|\sin \theta
$$

**Taylor series approximation (for small** $x)$**:**

$$
f(x) \approx f(0) + f^{\prime}(0)(x) + \frac{1}{2} f^{\prime \prime}(0)(x)^{2}+ \frac{1}{3!} f^{\prime \prime \prime}(0)(x)^{3}+ \cdot \cdot \cdot +
$$

::::

<!-- Source PDF page 35; printed label 26. -->

(sec-1-9)=
## 1.9 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-1-1)=

::::{admonition} Practice Problem 1-1

The equation of acceleration for a system is $a = Ce^{-t/\tau}$. If the system starts with $v = v_{0}$, what is the equation for velocity, $v(t)$?

::::

(problem-1-2)=

::::{admonition} Practice Problem 1-2

Two vectors are $\vec{a} = c\hat{\imath}+4c\hat{\jmath}$ and$\vec{b} = 3\hat{\imath}+5\hat{\jmath}$ , where $c$ is a constant. What is the vector dot product $\vec{a} \cdot \vec{b}$ and cross product $\vec{a} \times \vec{b}$?

::::

(problem-1-3)=

::::{admonition} Practice Problem 1-3

Two vectors are $\vec{a} = 2k\hat{\imath}+2\hat{\jmath}$ and$\vec{b} = 3\hat{\imath}+3k\hat{\jmath}$ , where $k$ is a constant. What is the angle between these vectors?

::::

(problem-1-4)=

::::{admonition} Practice Problem 1-4

Find $\vec{a} \cdot \vec{b}$ if:

$$
\begin{aligned}
\mathrm{a}) \vec{a} &= -4\hat{\imath} + 4\hat{\jmath} + 4\hat{k}, \vec{b} = 4\hat{\imath} - 4\hat{\jmath} - 4\hat{k} \\
\mathrm{b}) \vec{a} &= 7\hat{\imath} + 5\hat{\jmath} + 3\hat{k}, \vec{b} = 2\hat{\imath} + 4\hat{\jmath} - 8\hat{k} \\
\mathrm{c}) \vec{a} &= 3\hat{\imath} + 3\hat{\jmath} + 2c\hat{k}, \vec{b} = 3c\hat{\imath} - 3\hat{\jmath} - c\hat{k}
\end{aligned}
$$

d) What value(s) of the constant $c$ in part c) would make $\vec{a}$ and$\vec{b}$ perpendicular?

::::

<!-- Source PDF page 36; printed label 27. -->

(problem-1-5)=

::::{admonition} Practice Problem 1-5

For the vectors $\vec{a} = 9\hat{\imath} - 3\hat{\jmath} + 2\hat{k}, \vec{b} = -4\hat{\imath} - 5\hat{\jmath} + 2\hat{k}$ , and $\vec{c} = 3s\hat{\imath} + 3\hat{\jmath} + 9s\hat{k}$ , solve:

$$
\begin{aligned}
\mathrm{a}) \vec{a} \times \vec{b} \\
\mathrm{b}) \vec{b} \times \vec{c} \\
\mathrm{c}) \vec{c} \times \vec{b}
\end{aligned}
$$

$$
\mathrm{d}) \vec{c} \times \vec{a}
$$

::::

(problem-1-6)=

::::{admonition} Practice Problem 1-6

Two vectors are $\vec{a} = 2\hat{\imath} + \hat{\jmath} + \hat{k}$ and $\vec{b} = \hat{\imath} + 2\hat{\jmath} + \hat{k}$ . Solve the following triple cross products:

$$
\begin{aligned}
\mathrm{a}) \vec{a} \times (\vec{a} \times \vec{b}) \\
\mathrm{b}) \vec{b} \times (\vec{b} \times \vec{a}) \\
\mathrm{c}) (\vec{b} \times \vec{a}) \times \vec{b}
\end{aligned}
$$

::::

(problem-1-7)=

::::{admonition} Practice Problem 1-7

For each of the following, find the plane-polar $(r,\theta)$ coordinates or equation.

$$
\mathrm{a}) P(x,y) = (3,4)
$$

$$
\begin{aligned}
\mathrm{b}) y &= x \\
\mathrm{c}) y &= x^{2}+ x
\end{aligned}
$$

::::

(problem-1-8)=

::::{admonition} Practice Problem 1-8

A particle moves in a cloud chamber such that its position can be described by, $r = e^{2t}$ and $\theta = t^{2}$. Find its velocity and acceleration. Assume all quantities are unitless.

::::

(problem-1-9)=

::::{admonition} Practice Problem 1-9

A toy car on a racing track is moving in a circle of constant radius, $R$. The speed of the car is increasing as $v = bt$, where $b$ is a positive constant. What is the angle between the total velocity and total acceleration vectors at time $t=\sqrt{\frac{R}{b}}$?

::::

<!-- Source PDF page 37; printed label 28. -->

(problem-1-10)=

::::{admonition} Practice Problem 1-10

A cat goes for a walk in a spiral path. In polar coordinates, the cat’s radius and angle coordinates are given by $r(t) = be^{kt}$ and $\theta (t) = ct$, where $b, k$, and $c$ are all positive constants.

a) What is the cat’s velocity, in polar coordinates?

b) What is the cat’s acceleration, in polar coordinates?

c) Show that the angle between the velocity and acceleration is a constant.

::::

(problem-1-11)=

::::{admonition} Practice Problem 1-11

For small $x$, solve the first *three* terms of the Taylor series for

$$
\mathrm{a}) f(x) = \tan x
$$

$$
\mathrm{b}) f(x) = \frac{1}{1 - x}
$$

$$
\mathrm{c}) f(x) = \ln (1 - x)
$$

::::

(problem-1-12)=

::::{admonition} Practice Problem 1-12

For small $x$, solve the first *two* terms of the Taylor series for

$$
\mathrm{a}) f(x) = (1 - x^{2})^{3}
$$

$$
\mathrm{b}) f(x) = e^{\sin 5x}
$$

$$
\mathrm{c}) \ln (x^{2}+ 3x + 2)
$$

::::

(problem-1-13)=

::::{admonition} Practice Problem 1-13

Plot the functions and Taylor series approximations (first three non-zero terms) for the following functions ([sample python script](https://github.com/OSTP/Dynamics_Textbook/tree/main/py_notebooks)).

a) $f(x) = e^{-x^{2}}$ for $x \approx 0$

b) $f(x) = 2e^{x^{2}}$ for $x \approx 0$

c) ln (1 + $x)$ for $x \approx 0$

d) $e^{x}$ for $x \approx 2$

::::
