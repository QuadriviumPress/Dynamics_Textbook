(ch-3)=
# 3. Simple Harmonic Motion

<!-- Source PDF page 61; printed label 52. -->

::::{admonition} Learning Objectives

- Introduce and define simple harmonic motion

- Solve the equations of motion for simple mass-spring systems and pendulums

::::

In this chapter, we will apply Newton’s Laws to cases of simple harmonic motion.

(sec-3-1)=
## 3.1 Force is Proportional to Position

Let’s consider a force that is proportional to the position of the system. Examples of such forces are found in springs, pendulums, and torsion oscillators. [Figure 3.1](#fig-3-1) shows a case of a spring and mass, where the force acting on the mass from the spring is $F = -kx$, where $k$ is a positive constant. (Note this equation is also called Hooke’s Law.)

:::{figure} ../images/figures/figure-3-1.png
:label: fig-3-1
:enumerator: 3.1
:alt: Figure shows a mass attached to a spring on a horizontal surface.
:width: 195px

Example of the spring force acting on a mass.
:::

A force in the form of $F = -kx$ is also called a *restoring force*, because the force seeks to return a system to a state of equilibrium $(x$ = 0). For example, in [Figure 3.1](#fig-3-1), the spring is stretched from where it wants to be, $x_{0}$. The spring force will try to return the mass back to its equilibrium state.

::::{admonition} Restoring Forces

The key element to a restoring force is that the force is the negative sign in the $F = -kx$ equation. Because of that negative sign, the force vector will always point in the opposite direction as the displacement. If $x$ = 0 is our equilibrium position, then for $x < 0$ the restoring force will move the system toward a positive $x$, and for $x > 0$ the restoring force will move the system towards negative $x$ (in either case, the force tries to get the system back to equilibrium). If $x$ = 0, then there is no force.

::::

If the net force acting on the mass is the spring force, then we can use Newton’s second law, $\sum F = ma = -kx$ to get,

$$
a = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = - \frac{k}{m} x
$$ (eq-3-1)

<!-- Source PDF page 62; printed label 53. -->

Equation 3.1 is a second-order differential equation, where the second time derivative of displacement is proportional to the displacement $(k$ and $m$ are constants). Thus, we need a function that when differentiated twice gives you the negative of that original function multiplied by a constant. This type of problem has a well known solution. Two familiar functions that meet these conditions are the cos and sin functions.

The solution of a $\cos t$ or $\sin t$ function should make sense. Picture a mass hanging from a spring. If you move the mass upward and let go, the mass will initially move downwards until it reaches a maximum drop at which point it will be pulled back upwards until it reaches its original position then it will move back downwards. Essentially, the mass will move down and up in a periodic manner. [Figure 3.2](#fig-3-2) shows the up-down displacement of this mass as a function of time; note that the displacement looks like a cos (or sin) function.

:::{figure} ../images/figures/figure-3-2.png
:label: fig-3-2
:enumerator: 3.2
:alt: Figure shows a cartoon of a mass hanging from a vertical spring next to a graph showing the periodic displacement of the mass over time.
:width: 325px

Motion of a simple harmonic oscillator. The left panel shows that the mass will move up and down in periodic motion. The right panel shows a sketch of its displacement over time. The mass starts with a maximum displacement (e.g., maximum compression of the spring) and moves to the other end (e.g., maximum extension of the spring) and back again. This back-and-forth motion continues.
:::

Therefore, the solution to the second-order differential equation (Eq 3.1) is met with:

$$
x = A\cos (\omega _{0}t + \varphi)
$$ (eq-3-2)

where $A,\omega _{0}$, and $\varphi$ are all constants.

- $A$ is the amplitude of the motion, the maximum displacement from equilibrium.

- $\omega _{0}$ is the angular frequency. This is not the same as angular velocity (recall that we used $\omega = \frac{\mathrm{d}\theta}{\mathrm{d}t})$. Instead, $\omega _{0}$ is a fundamental property of the system itself. See details below for more details.

- $\varphi$ is the phase constant (sets where you are in the motion at $t$ = 0).

Equation 3.2 is a generic solution to the second-order differential equation that works for any simple harmonic oscillator (not just a mass and spring). Note also that instead of cos, we can use $B\sin (\omega _{0}t + \varphi _{2})$, where $B,\omega _{0}$, and $\varphi _{2}$ are all constants. Indeed, the cos and sin forms of the equation are interchangeable if you just alter the value of the phase constant. In practice, the most general solution for simple harmonic motion would be a superposition of cos and sin functions. For this textbook, however, we will assume that the motion can be described via a single periodic function and we will use the cos function by default.

Now that we have $x(t)$, we just need to differentiate once to get the velocity.

$$
\begin{aligned}
v&=\dot{x} \\
v&=\frac{\mathrm{d}}{\mathrm{d}t}\left[A\cos(\omega_{0}t+\varphi)\right]
\end{aligned}
$$

<!-- Source PDF page 63; printed label 54. -->

$$
v = -\omega _{0}A\sin (\omega _{0}t + \varphi)
$$ (eq-3-3)

And we can differentiate again to get the acceleration.

$$
\begin{aligned}
a&=\dot{v} \\
a&=\frac{\mathrm{d}}{\mathrm{d}t}\left[-\omega_{0}A\sin(\omega_{0}t+\varphi)\right] \\
a&=-\omega_{0}^{2}\underbrace{\left[A\cos(\omega_{0}t+\varphi)\right]}_{x(t)}
\end{aligned}
$$

$$
a = -\omega _{0}^{2}x
$$ (eq-3-4)

Thus, we find that $a = -\omega _{0}^{2}x$, where $\omega _{0}$ is the angular frequency constant. Going back to our original definition of the force in Equation (3.1), we had $a = - \frac{k}{m} x$ for the force $F = -kx$. Thus, the generic differential equation of motion solves Hooke’s Law if:

$$
\omega_{0}=\sqrt{\frac{k}{m}}
$$

Note that for other restoring forces, the solution for $\omega _{0}$ will be different.

(sec-3-2)=
## 3.2 Simple Harmonic Motion: Springs

(sec-3-2-1)=
### 3.2.1 Horizontal Springs

A spring is a coil of wire. When stretched or compressed, the spring will try to return to its equilibrium position via a restoring force of $F = -kx$ that acts against the spring’s displacement from equilibrium. The constant, $k$, is the spring constant and it is a measure of the spring’s stiffness.

We just solved the differential equation of motion for a simple spring-mass system in the previous section. So we know that the solution to this motion is

$$
x = A\cos (\omega _{0}t + \varphi)
$$

where $\omega_{0}=\sqrt{\frac{k}{m}}$. To get the values for $A$ and $\varphi$, you need to be given information about the motion at a particular time. These are constants (similar to constants of integration) and require initial conditions to be solved.

The angular frequency, $\omega _{0}$, is a fundamental property of the system itself (depends on the mass and spring constant) and it also relates to the period of motion. A cos function repeats every $2\pi$ radians, so a full period $T$ occurs when $\omega _{0}T = 2\pi$ or:

$$
T=\frac{2\pi}{\omega_{0}}=2\pi\sqrt{\frac{m}{k}}
$$ (eq-3-5)

So the physical properties of the system itself (mass, spring constant) determine the period of motion. That is, the system itself sets the period of motion, not the force that is applied.

<!-- Source PDF page 64; printed label 55. -->

(sec-3-2-2)=
### 3.2.2 Vertical Springs

Consider the case of a vertical spring. If the spring is vertical, we have an additional force to consider: gravity. [Figure 3.3](#fig-3-3) shows a spring hanging from the ceiling. Because there is a force pulling down on the spring, the spring has a different equilibrium point from the case when there is no mass hanging off it.

:::{figure} ../images/figures/figure-3-3.png
:label: fig-3-3
:enumerator: 3.3
:alt: Figure compares the equilibrium positions for a vertical mass and spring.
:width: 221px

Example of a vertical mass-spring system. Without the mass, the spring will have an equilibrium point at $x$ = 0. With the mass, gravity pulls down the spring until it reaches a new equilibrium point at $x = x_{0}$, where $x_{0}< 0$. If the mass is displaced from this new equilibrium point it will undergo simple harmonic motion.
:::

In this case, gravity stretches the spring downward, but the spring also pulls upward to counteract gravity. At some point, the spring force will balance gravity, and the system is in a new equilibrium. To find the new equilibrium position $x_{0}$ and the equation of motion, we go back to Newton’s second law.

$$
\sum F = ma
$$

$F_{g}+ F_{s}= ma =\Rightarrow \sum F$ is gravity $(F_{g})$ and the spring force $(F_{s})$ $ma = -kx - mg =\Rightarrow F_{g}= -mg$ and $F_{s}= -kx$ by definition $(+\hat{x}$ is up)

If the system is static, it is in equilibrium. Here, $ma$ = 0 and $-kx - mg$ = 0, which means that the new equilibrium position is $x_{0}= - \frac{mg}{k}$ . Note that $x_{0}$ is negative because we defined $x$ = 0 to be at the original equilibrium point when there is no mass on the spring and we defined $x$ as positive pointing up.

For any other position, $x$, the system will feel a net force and $a \not =$ 0:

$$
ma = -kx - mg
$$

$$
\begin{aligned}
m\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}&=-kx+kx_{0} \\
0&=\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}+\frac{k}{m}x-\frac{k}{m}x_{0}
\end{aligned}
$$

Here we used $x_{0}=-\frac{mg}{k}$, so $-mg=kx_{0}$.

So we have an additional (constant) term in our differential equation of motion. Nevertheless, we can still solve this second order differential equation. The trick here is that,

$$
\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}} (x - x_{0}) = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}
$$

<!-- Source PDF page 65; printed label 56. -->

if $x_{0}$ is a constant. The reason is that the derivative of a constant is always zero. So the constant does not factor into the differential at all. That means that the solution to this differential equation of motion is just what we had before, but with an offset. For example, substitute $X = x - x_{0}$. Doing this gives us:

$$
\begin{aligned}
\frac{\mathrm{d}^{2}X}{\mathrm{d}t^{2}} &= \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} =\Rightarrow \mathrm{where} x_{0}\mathrm{is} \mathrm{a} \mathrm{constant} \\
\frac{\mathrm{d}^{2}X}{\mathrm{d}t^{2}} &= - \frac{k}{m} X =\Rightarrow \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = - \frac{k}{m} (x - x_{0}) = - \frac{k}{m} X \\
X &= A\cos (\omega _{0}t + \varphi)
\end{aligned}
$$

which is the solution for a generic simple harmonic oscillator. But since $X = x - x_{0}$, the equation for vertical displacement $x$ is then $x - x_{0}= A\cos (\omega _{0}t + \varphi)$, where $x_{0}$ is our new equilibrium position. The equation of motion is,

$$
x = A\cos (\omega _{0}t + \varphi) + x_{0}
$$

::::{admonition} Quick questions

1. Consider a vertical spring-mass system with an equilibrium position at $x_{0}= - \frac{mg}{k}$ . What is the magnitude of the spring force at $x = x_{0}$ and $x$ = 0?

2. How does increasing (or decreasing) the spring constant affect the motion and the equilibrium point of a vertical spring-mass system.

3. If you moved the spring-mass system from Earth to the Moon (lower gravity) or Jupiter (higher gravity), how would the motion and equilibrium position change?

::::

::::{admonition} Test Your Understanding

Test your answers to the above questions with [the University of Colorado simulator](https://phet.colorado.edu/sims/html/masses-and-springs/latest/masses-and-springs_en.html):

::::

(sec-3-3)=
## 3.3 Brief Aside on the Differential Equation of Motion

The Differential Equation of Motion is a convenient tool to solve cases of simple harmonic motion. If you can put your physics into this format,

$$
0 = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} + Cx
$$

where $C$ is constant with time, then you can get the angular frequency, $\omega _{0}$ (and by default, the period $T$ and frequency $f)$ directly from the equation alone. In this form, where the differential has no coefficient, $\omega _{0}^{2}= C$. Other constants do not matter (e.g., consider the vertical spring) to solving $\omega _{0}$. Thus, you can read off the value of $\omega _{0}$ directly from the equation.

<!-- Source PDF page 66; printed label 57. -->

::::{tip} Quick Questions

1. After equating all forces, you obtain a differential equation of motion of the form:

$$
A \frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}} + \frac{4R_{1}k}{R_{2}} y + M(R_{1}^{2}+ R_{2}^{2})g = 0
$$

where all parameters are constants except $y$. What is the angular frequency $(\omega _{0})$ of this system? Note, you do not need to solve the differential equation of motion.

**A)** $\displaystyle \omega_{0}=\frac{4R_{1}k}{R_{2}}$

**B)** $\displaystyle \omega_{0}=\sqrt{\frac{4R_{1}k}{AR_{2}}}$

**C)** $\displaystyle \omega_{0}=\sqrt{\frac{4R_{1}k}{R_{2}}+M(R_{1}^{2}+R_{2}^{2})g}$

**D)** $\displaystyle \omega_{0}=\frac{4R_{1}k}{AR_{2}}+\frac{M(R_{1}^{2}+R_{2}^{2})g}{A}$

::::

(sec-3-4)=
## 3.4 Simple Harmonic Motion: Pendulum

(sec-3-4-1)=
### 3.4.1 Simple Pendulum

Now let’s consider a simple pendulum. A simple pendulum is a mass that hangs at the end of a string and is allowed to swing (see [Figure 3.4](#fig-3-4)).

:::{figure} ../images/figures/figure-3-4.png
:label: fig-3-4
:enumerator: 3.4
:alt: Figure shows the restoring force for a simple pendulum displaced from equilibrium.
:width: 163px

Example of a simple pendulum. The mass $m$ is in equilibrium when it is vertically downward and displaced from equilibrium when shifted an angle $\theta$ from the vertical axis. A restoring force $(F)$ moves the pendulum back to equilibrium.
:::

A pendulum is a simple harmonic oscillator as well, because it has an equilibrium position (straight down) and a restoring force that is proportional to the displacement will seek to return the pendulum to that position.

::::{admonition} Keep in Mind

We’re going to discuss the simple pendulum in two ways. Here, we use $F = ma$ to describe the motion of a simple pendulum. Later in [Chapter 7](#ch-7), we will revisit the simple pendulum using torques to show you how the two approaches differ. One of the key elements of this textbook is determine which methodology is ideal to use for a given physics problem. So when going through both, think about the pros (and cons) of each method.

::::

To solve for the force, let’s look at the free-body diagram of this system ([Figure 3.5](#fig-3-5)).

<!-- Source PDF page 67; printed label 58. -->

:::{figure} ../images/figures/figure-3-5.png
:label: fig-3-5
:enumerator: 3.5
:alt: Figure shows a free-body diagram for a simple pendulum with standard Cartesian axes.
:width: 163px

Free-body diagram of the simple pendulum from [Figure 3.4](#fig-3-4). The labeled forces are tension $(T)$ in red, gravity $(mg)$in blue, and the restoring force $(mg\sin \theta)$ in magenta. Shown in dotted-red is the component of gravity that balances tension $(mg\cos \theta)$.
:::

The restoring force is caused by a component of gravity that is perpendicular to the tension in the string. Because the mass-string system has an angular displacement $(\theta)$ from the equilibrium line, there is a component of gravity along the string and a component of gravity perpendicular to the string. It is the perpendicular component that is our restoring force (see magenta arrow in [Figure 3.5](#fig-3-5)). From trigonometry, the component parallel to the string can be written as $mg\cos \theta$ and the component perpendicular to the string is $mg\sin \theta$. The $mg\cos \theta$ component is equal (and opposite) to the tension in the string. The $mg\sin \theta$ component is our restoring force and it will be driving our motion. So we have,

$$
F = -mg\sin \theta
$$

where the negative sign is present because this is a restoring force (it will act in the opposite direction to our angular displacement). Since $T$ and $mg\cos \theta$ cancel (equal and opposite forces because the string is not deforming), our net force is equal to this restoring force.

You’ll notice that this force equation does not depend on $x$, but instead depends on the angular displacement. If we want to use $F = ma$, we need to get the displacement in units of $x$ because $a = \ddot{x}$ . Using the small angle approximation (see [Appendix B](#app-b)), we can write

$$
\sin \theta = \frac{x}{L} :
$$

:::{figure} ../images/figures/figure-3-6.png
:label: fig-3-6
:enumerator: 3.6
:alt: Figure shows a simple pendulum and the small angle approximation.
:width: 130px

Small angle approximation diagram for small values of $\theta$, as this is approximately a right angle triangle where the $y-$axis $(L)$, and displacement $x$ meet.
:::

The true path of the pendulum is an arc, so this assumption requires that $\theta$ isn’t too big so that there is very little difference between an arc and a straight line. See [Appendix B](#app-b) for a review on applying small angle approximations.

So with the small angle assumption, we get

$$
F = - \frac{mg}{L} x
$$

where $m,g$, and $L$ are all constants.

<!-- Source PDF page 68; printed label 59. -->

This equation has the exact same form as what we used for the spring $F = -kx$, only with different constants. We can solve the equation of motion.

$$
\sum F = ma
$$

$$
\begin{aligned}
- \frac{mg}{L} x &= m \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} \\
- \frac{g}{L} x &= \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} \\
0 &= \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} + \frac{g}{L} x
\end{aligned}
$$

Once more we have a Differential Equation of Motion that we can solve just by looking at it. This equation has the same structure as the spring and mass system. The general solution to this problem is $x(t) = A\cos (\omega _{0}t + \varphi _{1}) + B\sin (\omega _{0}t + \varphi _{2})$, but in this case, we have a different value for the angular frequency.

$$
\omega_{0}^{2}=\frac{g}{L}
$$

Recall that $\omega_{0}^{2}$ equals the coefficient in front of $x$, so

$$
\omega_{0}=\sqrt{\frac{g}{L}}.
$$

And the angular frequency relates to the period of motion by,

$$
T=\frac{2\pi}{\omega_{0}}=2\pi\sqrt{\frac{L}{g}}
$$

The period is independent of the mass of the pendulum.

::::{tip} Quick Questions

1. You have two identical pendulum clocks, but one is on Earth and one is on the Moon. How would the clock on the Moon keep time relative to the one on Earth?

2. How could you adjust the pendulum clock on the Moon for it to keep the same time as the one on Earth?

::::

::::{admonition} The physics of pendulums

The period (or the time necessary for the pendulum to swing back to its starting point) depends entirely on the length of the pendulum and the gravitational field where it is located. With the right series of lengths, you can get some interesting harmonics. [https://www.youtube.com/watch?v=yVkdfJ9PkRQ](https://www.youtube.com/watch?v=yVkdfJ9PkRQ)

::::

(sec-3-4-2)=
### 3.4.2 Physical Pendulum

Technically, any object can be made into a pendulum if displaced from its equilibrium position and allowed to swing freely from a pivot point. We call these cases a physical pendulum. [Figure 3.7](#fig-3-7) shows an example of a physical pendulum.

<!-- Source PDF page 69; printed label 60. -->

:::{figure} ../images/figures/figure-3-7.png
:label: fig-3-7
:enumerator: 3.7
:alt: Figure shows an irregular object as a physical pendulum with a restoring force at the center of mass.
:width: 182px

A physical pendulum. The irregular object has an equilibrium position as shown by the black dashed outline. When rotated out of this equilibrium position, a restoring force $F$ will seek to move it back toward equilibrium.
:::

The solution for a physical pendulum via $F = ma$ is non-trivial, because you need to consider the acceleration of every individual particle $(F_{i}= m_{i}a_{i})$ in the system and the linear acceleration $a_{i}$ will differ throughout the system. Instead, we will revisit the physical pendulum when we discuss *angular acceleration* and torques in [Chapter 7](#ch-7).

(sec-3-5)=
## 3.5 Sample Problems

(example-3-1)=

::::{admonition} Sample Problem 3-1

A block of mass $m$ is attached to two springs on a frictionless surface as shown in the figure below. If the block is displaced from equilibrium and set into simple harmonic motion, **find the period of oscillations for the block**.

:::{figure} ../images/figures/figure-3-8.png
:label: fig-3-8
:enumerator: 3.8
:alt: Figure shows a mass on a horizontal surface with springs attached to the left and right.
:width: 186px

Diagram of the system, with spring one having the constant $k_{1}$ and spring 2 having the constant $k_{2}$.
:::

**Solution**

Let’s first look at the free-body diagram of the system. There is the gravitational force and the normal force, which will be equal and opposite (no vertical motion). There are also restoring forces from each of the springs. If the block is displaced a distance $x$ from the equilibrium position, then the forces will be $F_{1}= -k_{1}x$ and $F_{2}= -k_{2}x$ (both springs are displaced by the same amount). The spring forces are in the same direction, because both act to move the block to equilibrium.

::::

<!-- Source PDF page 70; printed label 61. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-3-9.png
:label: fig-3-9
:enumerator: 3.9
:alt: Figure shows a free body diagram for a mass with two horizontal springs.
:width: 217px

Free-body diagram of the block and two spring system where $F_{1}$ comes from spring 1 and $F_{2}$ comes from spring 2, and the mass has been displaced $\Delta x$ to the left.
:::

Using Newton’s second law, the sum of all (horizontal) forces is;

$$
\begin{aligned}
\sum F&=F_{1}+F_{2}=ma \\
m\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}&=F_{1}+F_{2} \\
m\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}&=-k_{1}x-k_{2}x \\
\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}&=-\frac{k_{1}+k_{2}}{m}x \\
0&=\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}+\frac{k_{1}+k_{2}}{m}x
\end{aligned}
$$

The vertical forces cancel because $F_g=N$.

Again, we have a Differential Equation of Motion, and in this form, we can read off $\omega _{0}^{2}$ from the coefficient in front of the $x$ term.

$$
\begin{aligned}
\omega_{0}^{2}&=\frac{k_{1}+k_{2}}{m} \\
\omega_{0}&=\sqrt{\frac{k_{1}+k_{2}}{m}}
\end{aligned}
$$

But the question asked for the period of oscillations. For the period, we get

$$
T = 2\pi \frac{1}{\omega _{0}}
$$

$$
T=2\pi\sqrt{\frac{m}{k_{1}+k_{2}}}
$$

This is the same solution as the simple (one spring) case, but $k \rightarrow k_{1}+k_{2}$ because there are two springs working together. As a consequence of having these two springs, the period decreased compared to if there was one spring alone.

::::

<!-- Source PDF page 71; printed label 62. -->

(example-3-2)=

::::{admonition} Sample Problem 3-2

A simple pendulum of mass $m$ and length $L$ is also attached to spring with spring constant $k$ as shown in the figure below. The equilibrium point for both the pendulum and spring is given by the vertical with the pivot point. If the pendulum is displaced from this equilibrium by an angle $\theta$ (like a pendulum), **find the period of oscillations**.

:::{figure} ../images/figures/figure-3-10.png
:label: fig-3-10
:enumerator: 3.10
:alt: Figure shows a simple pendulum with a spring attached to the mass.
:width: 99px

A mass $m$ forms a simple pendulum with a massless rope of length $L$. The mass is also attached to a horizontal spring with spring constant $k$. The equilibrium point for both the pendulum and spring is shown by the dashed vertical line (right below the pivot point).
:::

**Solution**

This problem contains two simple harmonic oscillators. Let’s look at a free-body diagram for the mass. At the position of the mass, the forces are gravity on the mass, tension in the rope, and the spring force. Breaking up the gravitational force into its components along the axis of the rope and perpendicular to that axis, we get the restoring force from the pendulum as $F_{p}= F_{g}\sin \theta \approx \frac{mg}{L} x$ for small angles, $\theta$. Note that for small angles, both the restoring forces act in the same direction.

:::{figure} ../images/figures/figure-3-11.png
:label: fig-3-11
:enumerator: 3.11
:alt: Figure shows the free-body diagram for the simple pendulum and spring.
:width: 248px

On the left is the free-body diagram of the spring-mass system, and on the right is the component break-down of the force of gravity, $(F_{g})$ in red.
:::

Putting these forces together, we can solve the equation of motion from the sum of all

::::

<!-- Source PDF page 72; printed label 63. -->

::::{admonition} Continued

forces:

$$
\begin{aligned}
\sum F &= F_{s}+ F_{p}= ma =\Rightarrow T \text{ and } F_{g}\cos \theta \text{ cancel, so we can ignore them} \\
ma &= -kx - \frac{mg}{L} x \\
m \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} &= -\bigg(k + \frac{mg}{L} \bigg)x \\
\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} &= -\Bigg(\frac{kL + mg}{mL} \Bigg)x
\end{aligned}
$$

$$
0 = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} + \Bigg(\frac{kL + mg}{mL} \Bigg)x
$$

Again, we have a Differential Equation of Motion, and in this form, we can read off $\omega _{0}^{2}$ from the coefficient in front of the $x$ term.

$$
\begin{aligned}
\omega_{0}^{2}&=\frac{kL+mg}{mL} \\
\omega_{0}&=\sqrt{\frac{kL+mg}{mL}} \\
\omega_{0}&=\sqrt{\frac{k}{m}+\frac{g}{L}}
\end{aligned}
$$

The angular frequency has a term for the spring and the pendulum, which increases the value of $\omega _{0}$ compared to the value from either the spring or pendulum alone. A larger $\omega _{0}$ will decrease the period (they are inversely proportional). This means that by adding simple harmonic oscillators, the motion goes faster (shorter period).

For this $\omega _{0}$, the period is:

$$
T=\frac{2\pi}{\omega_{0}}=2\pi\sqrt{\frac{mL}{kL+mg}}
$$

::::

(sec-3-6)=
## 3.6 Aside on Damping and Driven Motion

The harmonic motion described above is all perfectly conserved (e.g., there is no loss of energy from friction). In practice, most oscillators undergoing harmonic motion are damped or driven. Examples of damped (energy lost) oscillations include the suspension in a vehicle (this is on purpose to limit the oscillations from bumps on the road) and tuned mass dampers in tall buildings to limit motion at high floors from earthquakes or strong winds. Examples of driven (energy gained) oscillations include pushing a child on a swing (when timed right, the child goes higher and higher) or resonances in bridges. Damped and driven motion will not be covered here.

But for fun, here are some videos that show damping motion in action. An excellent example of a tuned mass damper is the Taipei 101 building in Taiwan. Unlike most skyscrapers, the

<!-- Source PDF page 73; printed label 64. -->

tuned mass damper in Taipei 101 is available to be seen. Here is [a nice video showing the Taipei 101 building tuned mass damper](https://www.youtube.com/watch?v=ohKqE_mwMmo) in action This video does a nice job [illustrating why these dampers work](https://www.youtube.com/watch?v=f1U4SAgy60c).

And to also showcase driven motion, here is a video from 1940 which shows the [collapse of](https://youtu.be/GBa_USozxFM?t=75) [the Tacoma Narrows bridge](https://youtu.be/GBa_USozxFM?t=75) in the USA during a strong wind after less than four months in operation. Here is the [Millennium pedestrian bridge in the UK](https://www.youtube.com/watch?v=eAXVa__XWZ8). It did not collapse, but note how the oscillations are driven; as the bridge sways, more and more people become unbalanced at the same time and then take steps in sequence driving stronger oscillations.

(sec-3-7)=
## 3.7 Real-World Application

Not all oscillations are simple harmonic motion. Nevertheless, other types of periodic behaviour can be expressed with similar base mathematics even if the physics behind them is very different than a simple restoring force. These more complex cases consequently produce more complex oscillatory motions, extending the concepts of *simple* harmonic motion into more varied phenomena.

Seismology is the study of seismic (sound) waves that move around and through the Earth. Studying these waves can provide us information about the structure of our planet’s interior that we couldn’t otherwise constrain. The strongest seismic waves are generated by movements of tectonic plates but waves may also be caused by volcanoes, landslides, explosions, and other energetic events on and under the Earth’s surface.

Seismographs are used to record the motion of the ground due to seismic waves. Those waves travel through layers with different compositions and densities, and so are refracted and reflected. Using multiple instruments, the amount of time it takes seismic waves to travel through the Earth can be calculated and the type of material the waves are travelling through can be deduced, giving a picture of the Earth’s interior.

Since seismic waves can cause widespread damage, many agencies around the world have developed early warning systems to detect earthquakes as quickly as possible. The nationwide Earthquake Early Warning (EEW) system operated in Japan is the most advanced detection system in use, with a network of more than 4,000 seismometers.

**For more information:**

For some introductory science on seismic waves, you can visit [the Science Learning Hub - Pokapū Akoranga Pūtaiao](https://www.sciencelearn.org.nz/resources/340-seismic-waves).

This [web site contains information on earthquake warning systems](https://www.earthsystems.com/earthquake-early-warning-systems/) in use around the world.

[This interactive map](https://www.jma.go.jp/bosai/map.html#9/36.584/140.37/&elem=int&contents=earthquake_map&lang=en ) uses real time data from Japan’s Earthquake Early Warning system.

<!-- Source PDF page 74; printed label 65. -->

(sec-3-8)=
## 3.8 Summary

::::{admonition} Key Takeaways

This chapter focuses on simple harmonic motion and solving problems of simple harmonic motion using Newton’s laws. Simple harmonic motion is a periodic motion (system moves back and forth) that arises when a force has the form of

$$
\vec{F} = -k\vec{r}
$$

where $k$ is a constant. These types of forces are also called restoring forces, because the force itself seeks to return the system back to an equilibrium position (where the displacement is zero).

Solving Newton’s laws for simple harmonic motion yields a second-order differential equation of motion in the form of:

$$
0 = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} + Cx
$$

where $C$ is a positive constant. This differential equation has a very well known solution of a cos (or sin) function, such as

$$
x = A\cos (\omega _{0}t + \varphi)
$$

A key property of simple harmonic motion is the angular frequency, $\omega _{0}$, which can be read directly off the differential equation of motion,

$$
\omega _{0}^{2}= C
$$

The angular frequency is a fundamental property of the system. It depends only on the constants of the system (e.g., mass, rope length, spring constant) and it also sets the period for the periodic motion.

$$
T = \frac{2\pi}{\omega _{0}}
$$

Thus, if you can get a simple harmonic motion problem into its differential equation of motion, you can automatically solve for the period of motion and its angular frequency.

::::

<!-- Source PDF page 75; printed label 66. -->

::::{admonition} Important Equations

**General 2nd-Order Differential:**

$$
\begin{aligned}
0 &= \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} + Cx \\
\mathrm{where}:
\end{aligned}
$$

$$
C = \omega _{0}^{2}\mathrm{for} \mathrm{positive} \mathrm{constant} \mathrm{C}
$$

$$
\begin{aligned}
\mathrm{and} \\
T &= \frac{2\pi}{\omega _{0}}
\end{aligned}
$$

**2nd-Order Differential for Spring-Mass:**

$$
\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}=-\frac{k}{m}x,
\qquad
\omega_{0}=\sqrt{\frac{k}{m}}
$$

**2nd-Order Differential for Simple Pendulum:**

$$
\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}=-\frac{g}{L}x,
\qquad
\omega_{0}=\sqrt{\frac{g}{L}}
$$

**Simple Solution to 2nd-Order Differential:**

$$
x = A\cos (\omega _{0}t + \varphi _{1})
$$

$$
v = -\omega _{0}A\sin (\omega _{0}t + \varphi _{1})
$$

$$
a = -\omega _{0}^{2}x
$$

**General Solution to 2nd-Order Differential:**

$$
x = A\cos (\omega _{0}t + \varphi _{1}) + B\sin (\omega _{0}t + \varphi _{2})
$$

$$
v = -\omega _{0}A\sin (\omega _{0}t + \varphi _{1}) + \omega _{0}B\cos (\omega _{0}t + \varphi _{2})
$$

$$
a = -\omega _{0}^{2}x
$$

::::

<!-- Source PDF page 76; printed label 67. -->

(sec-3-9)=
## 3.9 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-3-1)=

::::{admonition} Practice Problem 3-1

If you are given a clock made from a simple mass and spring system, but the clock is running slow such that each oscillation takes twice as long as it should, what change can you make to the mass to correct the clock?

::::

(problem-3-2)=

::::{admonition} Practice Problem 3-2

A standard pendulum clock on Earth has a period of 2s. If NASA wants to engineer a series of simple pendulum clocks that can keep proper time on all of the planets in the Solar System, what arm lengths would be necessary for each planet?

::::

(problem-3-3)=

::::{admonition} Practice Problem 3-3

An antique pendulum clock uses a uniform rod of length $L$ and operates with an angular frequency of $\omega_{0}=\sqrt{\frac{3g}{L}}$.

a) What is the differential equation of motion for this clock?

b) Plot the period as function of rod length for lengths between 10 cm and 1 m.

c) What length would give you a period of 1s? Check your answer against your plots from part b).

::::

(problem-3-4)=

::::{admonition} Practice Problem 3-4

Two springs with different spring constants are attached to a mass $(m)$ as shown. What is the angular frequency of this simple harmonic motion produced by this system?

:::{figure} ../images/figures/figure-3-12.png
:label: fig-3-12
:enumerator: 3.12
:alt: Figure shows a mass on a horizontal surface with two springs attached to the same side.
:width: 217px

Figure for [Problem 3-4](#problem-3-4).
:::

::::

<!-- Source PDF page 77; printed label 68. -->

(problem-3-5)=

::::{admonition} Practice Problem 3-5

An elevator is falling at nearly the free-fall acceleration. If the elevator also contains a simple pendulum clock, what happens to the periodic motion of the pendulum clock when,

a) The elevator was stationary?

b) While it is in free-fall? Note: free-fall means that the elevator is traveling at near the gravitational acceleration.

::::

(problem-3-6)=

::::{admonition} Practice Problem 3-6

Consider a pendulum-spring system where the angular frequency is:

$$
\omega_{0}=\sqrt{\frac{k}{m}+\frac{g}{L}}
$$

a) Write out the equations for position, velocity, and acceleration assuming small displacements, $A$ in $x$.

b) Plot these equations for different values for $A, k, m$, and $L$ and observe how the graphs change.

::::

(problem-3-7)=

::::{admonition} Practice Problem 3-7

See the figure below. A mass, $m$, is sitting on an incline of angle $\theta$ and attached to a spring from the top. Assume the surface is frictionless. The mass is displaced from equilibrium by a small distance, $x$.

a) Draw a free-body diagram for the mass.

b) What is the equilibrium point of the mass?

c) What is the differential equation of motion for the mass?

d) What is the period of oscillations for this motion? How does the period depend on $\theta$? Comment.

::::

<!-- Source PDF page 78; printed label 69. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-3-13.png
:label: fig-3-13
:enumerator: 3.13
:alt: Figure shows a mass on an incline with a spring attached at the top of the incline.
:width: 217px

Figure for [Problem 3-7](#problem-3-7).
:::

::::

(problem-3-8)=

::::{admonition} Practice Problem 3-8

A mass $m$ sits on a frictionless surface with one spring attached to each side. The springs have spring constants of $k_{1}$ and $3k_{1}$, respectively. If the mass is displaced from equilibrium with an amplitude $A$, it will oscillate.

a) Draw a free-body diagram for the mass.

b) Find the differential equation of motion for the mass.

c) Find the angular frequency and period of the mass as it oscillates.

d) Find the equations for displacement, velocity, and acceleration in terms of the variables given.

e) Plot the functions from part d). Sample python codes are available in the [online](https://github.com/OSTP/Dynamics_Textbook/tree/main/py_notebooks) [repository](https://github.com/OSTP/Dynamics_Textbook/tree/main/py_notebooks).

::::

(problem-3-9)=

::::{admonition} Practice Problem 3-9

Two ideal springs with constants $k_{1}$ and $k_{2}$ are connected to each other and hang vertically from a ceiling. A mass is attached to the lower spring and the system is set in simple harmonic motion. Note that the two springs are connected in series with this arrangement.

a) Draw a free-body diagram for the mass.

b) We want to replace the two springs with a single spring but retain the same simple harmonic motion. Show that the effective spring constant for this new spring is:

$$
k_{eff}= \frac{k_{1}k_{2}}{k_{1}+ k_{2}}
$$

Hint: For ideal (massless) springs that are connected, they will have the same force, but different displacements.

::::

<!-- Source PDF page 79; printed label 70. -->

(problem-3-10)=

::::{admonition} Practice Problem 3-10

Three springs, $k_{1}, k_{2}$, and $k_{3}$ are attached to a mass, $m$ in series as shown in the figure below. Springs $k_{1}$ and $k_{2}$ are in series on one side with $k_{3}$ on the other. Assume the surface is frictionless. The mass is displaced from equilibrium by a small distance, $x$.

a) Draw a free-body diagram for the mass.

b) What is the differential equation of motion for the mass?

c) Show that this system has a period of oscillations of:

$$
T=2\pi\sqrt{\frac{m(k_{1}+k_{2})}{k_{1}k_{2}+k_{3}(k_{1}+k_{2})}}
$$

:::{figure} ../images/figures/figure-3-14.png
:label: fig-3-14
:enumerator: 3.14
:alt: Figure shows a mass on a horizontal surface with three springs.
:width: 279px

Figure for [Problem 3-10](#problem-3-10)
:::

::::
