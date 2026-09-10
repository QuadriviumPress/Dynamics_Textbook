(ch-12)=
# 12. The Lagrange Method

<!-- Source PDF page 257; printed label 248. -->

::::{admonition} Learning Objectives

- Introduction to the Lagrangian and Euler-Lagrange equations

- Apply the Lagrangian method to physics problems

::::

In this chapter, we will introduce the Lagrangian and the Euler-Lagrange method to solving physics problems. This technique represents another tool in your physics toolkit, much like how we can use energy conservation, momentum conservation, and Newton’s laws to solve physics problems.

(sec-12-1)=
## 12.1 Introduction to the Lagrangian Method

Consider the case of a single particle being acted on by a conservative force in 1-D $(x-$axis). From the energy equations, we can say that:

$$
F = - \frac{\partial U}{\partial x}
$$

But from Newton’s laws, we can also write the force as

$$
F = \frac{\mathrm{d}p}{\mathrm{d}t} = m \frac{\mathrm{d}v}{\mathrm{d}t} = m \frac{\mathrm{d}\dot{x}}{\mathrm{d}t}
$$

for constant mass. We can therefore relate the force to the kinetic energy, because the kinetic energy depends on the velocity, $K = \frac{1}{2} m\dot{x}^{2}$.

$$
\frac{\mathrm{d}K}{\mathrm{d}\dot{x}}=m\dot{x},
\qquad
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}K}{\mathrm{d}\dot{x}}\right)
=m\frac{\mathrm{d}\dot{x}}{\mathrm{d}t}=F.
$$

We can combine these two force equations to say that:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\mathrm{d}K}{\mathrm{d}\dot{x}} \Bigg) = - \frac{\mathrm{d}U}{\mathrm{d}x}
$$

The above equation is a function of the kinetic and potential energies. So we define the **Lagrangian** as:

$$
L = K - U
$$ (eq-12-1)

<!-- Source PDF page 258; printed label 249. -->

where $L$ is the Lagrangian, and we will use the symbol $L$ for the Lagrangian to make it distinct from the angular momentum (defined as $L$ in this text).

$L$ is a function of position and velocity. That is, $L = L(x,\dot{x}$ ) in 1-D, because $K = K(\dot{x}$ ) and $U = U(x)$. In this case, $K$ is not a function of position and $U$ is not a function of velocity. As such,

$$
\frac{\partial L}{\partial x} = - \frac{\partial U}{\partial x}
$$

$$
\frac{\partial L}{\partial \dot{x}} = \frac{\partial K}{\partial \dot{x}}
$$

where $\partial$ indicates a partial derivative. For a partial derivative, you hold all other variables constant and only take the derivative with respect to the one variable.

Therefore, we can rewrite
$\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}K}{\mathrm{d}\dot{x}}\right)=-\frac{\mathrm{d}U}{\mathrm{d}x}$,
which we had before as:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$ (eq-12-2)

This is the **Euler-Lagrange equation**. The above example is for 1-D motion in the $x-$axis, but in practice, you can apply the arguments to represent the Euler-Lagrange equations in other (independent) coordinates. In its general form, the Euler-Lagrange equation is:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}_{i}} \Bigg) = \frac{\partial L}{\partial x_{i}}
$$ (eq-12-3)

where $x_{i}$ represents a coordinate axis (e.g., could be $x, y, r$, etc.). For multi-dimensional problems, you need to solve the Euler-Lagrange equations for each dimension (each axis) separately.

The Lagrangian method represents yet another way you can solve problems in physics. For the rest of the chapter, we will look at a few examples.

::::{tip} Quick Questions

1. Show that the units of the Euler-Lagrange equation match expectations.

2. Show that you get comparable equations for the $y$ and $z$ axis.

::::

::::{admonition} Caveats to the Lagrange Method

For the Lagrange method to work, we must treat $\dot{x}_{i}$ and $x_{i}$ as independent variables and assume that the time dependence only enters the problem through $x$ and $\dot{x}_{i}$.

::::

<!-- Source PDF page 259; printed label 250. -->

(sec-12-2)=
## 12.2 Application to 1-D Problems

(example-12-1)=

::::{admonition} Sample Problem 12-1

Consider a horizontal spring-mass system on a frictionless surface. **Compare the** **differential equation of motion for the mass using (1) Newton’s Laws, (2)** **Energy Conservation, and (3) the Euler-Lagrange method.**

:::{figure} ../images/figures/figure-12-1.png
:label: fig-12-1
:enumerator: 12.1
:alt: Figure shows a simple horizontal mass-spring system.
:width: 155px

Horizontal spring mass system with the spring constant $k$, and mass $m$.
:::

**Solution**

**Method 1: Newton’s Laws:**

$$
\sum \vec{F} = m\vec{a}
$$

$$
\begin{aligned}
-kx &= m \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = m\ddot{x} =\Rightarrow \mathrm{net} \mathrm{force} \mathrm{is} \mathrm{spring} \mathrm{force} \\
0 &= \ddot{x} + \frac{k}{m} x
\end{aligned}
$$

**Method 2: Energy Conservation:**

$$
\begin{aligned}
E &= K + U =\Rightarrow \mathrm{assume} U = 0 \mathrm{at} \mathrm{equilibrium} \\
E &= \frac{1}{2} m\dot{x}^{2}+ \frac{1}{2} kx^{2}=\Rightarrow K = \frac{1}{2} m\dot{x}^{2}, U = \frac{1}{2} kx^{2} \\
\frac{\mathrm{d}E}{\mathrm{d}t} &= \frac{\mathrm{d}}{\mathrm{d}t} \bigg(\frac{1}{2} m\dot{x}^{2}+ \frac{1}{2} kx^{2}\bigg) \\
0 &= m\dot{x} \frac{\mathrm{d}\dot{x}}{\mathrm{d}t} + kx\dot{x} =\Rightarrow \mathrm{set} \frac{\mathrm{d}E}{\mathrm{d}t} = 0 \\
0 &= \ddot{x} + \frac{k}{m} x =\Rightarrow \mathrm{simplify}
\end{aligned}
$$

**Method 3: Euler-Lagrange:**

For this method, we will solve

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$

::::

<!-- Source PDF page 260; printed label 251. -->

::::{admonition} Continued

where we can use the energy terms from previously to solve the Lagrangian,

$$
L = K - U = \frac{1}{2} m\dot{x}^{2}- \frac{1}{2} kx^{2}
$$

Taking each partial differential term of the Euler-Lagrange equations separately:

$$
\frac{\partial L}{\partial x} = \frac{\partial}{\partial x} \bigg(- \frac{1}{2} kx^{2}\bigg) = -kx
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial}{\partial \dot{x}} \bigg[\frac{1}{2} m\dot{x}^{2}\bigg]\Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} (m\dot{x}) = m\ddot{x}
$$

So now going back to the Euler-Lagrange equation:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$

$$
\begin{aligned}
m\ddot{x} &= -kx \\
0 &= \ddot{x} + \frac{k}{m} x
\end{aligned}
$$

All three methods match!

1. Use the Lagrangian to get the equation of motion for a vertical mass-spring system and a simple pendulum. Compare to using the other methods.

::::

::::{admonition} Lance’s Thoughts

Thinking about a variable and its time derivative as two separate variables is a little strange to begin with, but if you’re able to set up the Lagrangian system properly, a couple of quick derivatives can get you to the solution a lot faster. It might help your first few tries at it to back out of dot notation very briefly: $x$ and $v$ look more different than $x$ and $\dot{x}$ . Visually, it can be easier to distinguish

$$
m_{1}a = (m_{1}+ m_{2})v^{2}+ m_{1}gx_{1}+ m_{2}g(h - x_{1})
$$

from

$$
m_{1}\ddot{x} = (m1 + m2)\dot{x} + m_{1}gx_{1}+ m_{2}g(h - x_{1})
$$

until you get used to the process and so can be easier to see position and velocity as separate variables.

::::

<!-- Source PDF page 261; printed label 252. -->

(example-12-2)=

::::{admonition} Sample Problem 12-2

Consider an Atwood machine with a pulley that is a solid disk of mass $M$ and radius $R (I = \frac{1}{2} MR^{2})$ and two masses, $m_{1}$ and $m_{2}$. Assume the rope is inextensible and the pulley rotates without slipping. **What is the acceleration of** $m_{1}$**?**

:::{figure} ../images/figures/figure-12-2.png
:label: fig-12-2
:enumerator: 12.2
:alt: Figure shows a simple Atwood machine with two masses on either side.
:width: 93px

The Atwood machine for this problem.
:::

**Solution**

We’ve looked at this problem previously with energy conservation ([Sample Problem 9-3](#example-9-3)). Please review that question for more details, but briefly, the potential energy of the system comes from the vertical position of the two masses and the kinetic energy is from the linear motion of the two masses and the rotational motion of the pulley. [Figure 12.3](#fig-12-3) shows the definition of the position of each of the masses. Note that we have set the $y$ = 0 line (and the $U$ = 0 line) to be at the center of the pulley.

:::{figure} ../images/figures/figure-12-3.png
:label: fig-12-3
:enumerator: 12.3
:alt: Figure shows the position of each mass in the Atwood machine relative to center of the pulley.
:width: 211px

The Atwood machine with the positions of each mass.
:::

For this system, we have:

$$
\begin{aligned}
U &= -m_{1}gy_{1}- m_{2}gy_{2} \\
K &= \frac{1}{2} m_{1}(\dot{y}_{1})^{2}+ \frac{1}{2} m_{2}(\dot{y}_{2})^{2}+ \frac{1}{2} I\omega ^{2}
\end{aligned}
$$

At first glance, this may seem like a 2-D problem, but the positions of $y_{1}$ and $y_{2}$ are not independent. As one increases, the other decreases because the rope is inextensible

::::

<!-- Source PDF page 262; printed label 253. -->

(does not stretch) and has a constant length. If the length of the rope is $A$ (a constant), then $y_{1}+ y_{2}= A$. We can then express $y_{2}$ and $\dot{y}_{2}$ with respect to $y_{1}$.

$$
y_{2}= A - y_{1}
$$

$$
\dot{y}_{2}= -\dot{y}_{2}
$$

Moreover, since this is an ideal pulley, it rotates without slipping so we can also use $|\dot{y}_{1}| = R\omega$. Thus, we can re-write the energy equations as:

$$
U = -m_{1}gy_{1}- m_{2}g(A - y_{1})
$$

$$
\begin{aligned}
K &= \frac{1}{2} (m_{1}+ m_{2})(\dot{y}_{1})^{2}+ \frac{1}{2} I \bigg(\frac{\dot{y}_{1}}{R} \bigg)^{2} \\
&= \frac{1}{2} \bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\dot{y}_{1}^{2}=\Rightarrow \mathrm{sub} \mathrm{in} I = \frac{1}{2} MR^{2}
\end{aligned}
$$

The Lagrangian (in terms of $y_{1}$ and $\dot{y}_{1}$ only is then:

$$
\begin{aligned}
L &= \frac{1}{2} m_{1}+ m_{2}+ \frac{1}{2} M \dot{y}_{1}^{2}+ m_{1}gy_{1}+ m_{2}g(A - y_{1}) \\
&= \frac{1}{2} \bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\dot{y}_{1}^{2}+ (m_{1}- m_{2})gy_{1}+ m_{2}gA
\end{aligned}
$$

Note that this Lagrangian contains a constant term $(m_{2}gA)$. This term does not factor into the Euler-Lagrange equations because it has no dependence on position or velocity. You can essentially ignore any constant terms in the Lagrangian method.

The terms of the Euler-Lagrange equation are:

$$
\frac{\partial L}{\partial y_{1}} = \frac{\partial}{\partial y_{1}} [(m_{1}- m_{2})gy_{1}] = (m_{1}- m_{2})g
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{y}_{1}} \Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial}{\partial \dot{y}_{1}} \bigg[\frac{1}{2} \bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\dot{y}_{1}^{2}\bigg]\Bigg)
$$

$$
\begin{aligned}
&= \frac{\mathrm{d}}{\mathrm{d}t} \bigg[\bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\dot{y}_{1}\bigg] \\
&= \bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\ddot{y}_{1}
\end{aligned}
$$

And the Euler-Lagrange equation is:

<!-- Source PDF page 263; printed label 254. -->

::::{admonition} Continued

$$
\begin{aligned}
\frac{\partial L}{\partial y_{1}} &= \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{y}_{1}} \Bigg) \\
(m_{1}- m_{2})g &= \bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg)\ddot{y}_{1} \\
\ddot{y}_{1}&= \frac{g(m_{1}- m_{2})}{m_{1}+ m_{2}+ \frac{1}{2} M}
\end{aligned}
$$

This is exactly what we got from energy conservation ([Sample Problem 9-3](#example-9-3)).

::::

(sec-12-3)=
## 12.3 Application in 2-D

(example-12-3)=

::::{admonition} Sample Problem 12-3

Consider an object of mass $m$ moving in an elliptical orbit under gravity in polar coordinates where the acceleration due to gravity changes with position. **Solve the** **Euler-Lagrange equations for this object.**

**Solution**

For this problem we have motion in 2-D because the object is in an elliptical orbit, which means that

$$
\vec{v} = v_{r}\hat{r} + v_{\theta}\hat{\theta} = \dot{r}\hat{r} + (r\dot{\theta})\hat{\theta}
$$

where $\hat{r}$ and $\hat{\theta}$ are independent dimensions.

To solve the Lagrangian, we need the sources of potential and kinetic energy. The only source of potential energy is the gravitational field and the only source of kinetic energy is the orbital motion (note that we are using the central force potential, not the effective potential here). For this system, we have:

$$
\begin{aligned}
U &= - \frac{GMm}{r} \\
K &= \frac{1}{2} mv^{2}
\end{aligned}
$$

where the squared velocity is given by:

$$
v^{2}= v_{r}^{2}+ v_{\theta}^{2}= \dot{r}^{2}+ (r\dot{\theta})^{2}
$$

See [Chapter 1.2](#sec-1-2) for a review of plane-polar coordinates. Thus, in polar coordinates, the energy equations are:

::::

<!-- Source PDF page 264; printed label 255. -->

$$
\begin{aligned}
U &= - \frac{GMm}{r} \\
K &= \frac{1}{2} m(\dot{r}^{2}+ r^{2}\dot{\theta}^{2})
\end{aligned}
$$

And the Lagrangian is:

$$
L = \frac{1}{2} m(\dot{r}^{2}+ r^{2}\dot{\theta}^{2}) + \frac{GMm}{r}
$$

So the Lagrangian is really $L = L(r,\dot{r},\theta,\dot{\theta}$ ) and each dimension must be solved separately.

$$
\frac{\partial L}{\partial r} = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{r}} \Bigg)
$$

$$
\frac{\partial L}{\partial \theta} = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{\theta}} \Bigg)
$$

Note, however, that the Lagrangian does not have any $\theta$ dependence. That’s because gravity is a radial force. As a consequence, we can say that:

$$
\frac{\partial L}{\partial \theta} = 0
$$

Thus, from the Euler-Lagrange equation:

$$
\frac{\partial L}{\partial \theta} = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{\theta}} \Bigg)
$$

$$
0 = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{\theta}} \Bigg)
$$

So the derivative of the Lagrangian with angular velocity $(\frac{\partial L}{\partial \dot{\theta}}$ ) is constant with time.

$$
\frac{\partial L}{\partial \dot{\theta}} = \frac{\partial}{\partial \dot{\theta}} \bigg(\frac{1}{2} mr^{2}\dot{\theta}^{2}\bigg) = mr^{2}\dot{\theta} = \mathrm{constant}
$$

The term $mr^{2}\dot{\theta}$ is the angular momentum of the system (see [Chapter 6](#ch-6)) and we recover the condition that angular momentum is constant (as expected for a central force; [Chapter 10](#ch-10)) directly from the Lagrangian and Euler-Lagrange equations.

<!-- Source PDF page 265; printed label 256. -->

::::{admonition} Continued

Now let’s look at the radial terms.

$$
\frac{\partial L}{\partial r} = \frac{\partial}{\partial r} \bigg(\frac{1}{2} mr^{2}\dot{\theta}^{2}+ \frac{GMm}{r} \bigg) = mr\dot{\theta}^{2}- \frac{GMm}{r^{2}}
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{r}} \Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial}{\partial \dot{r}} \bigg[\frac{1}{2} m\dot{r}^{2}\bigg]\Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} (m\dot{r}) = m\ddot{r}
$$

And the Euler-Lagrange equation is:

$$
\frac{\partial L}{\partial r} = \frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{r}} \Bigg)
$$

$$
mr\dot{\theta}^{2}- \frac{GMm}{r^{2}} = m\ddot{r}
$$

At this point, we have two equations of motion.

$L = mr^{2}\dot{\theta} =\Rightarrow L$ is the angular momentum (and this is constant)

$$
m\ddot{r}=mr\dot{\theta}^2-\frac{GMm}{r^2}
\qquad\text{(the radial component)}
$$

We can combine these equations to remove the $\dot{\theta}$ term from the radial equation.

$$
\begin{aligned}
m\ddot{r} &= mr \frac{L^{2}}{m^{2}r^{4}} - \frac{GMm}{r^{2}} =\Rightarrow \dot{\theta} = \frac{L}{mr^{2}} \\
\ddot{r} &= \frac{L^{2}}{m^{2}r^{3}} - \frac{GM}{r^{2}}
\end{aligned}
$$

We have now created a 1-D equation of motion because $L, G, m$, and $M$ are all constants. The only variable is $r$. That means that we can solve this problem.

You will also notice that this is the effective force for a system moving under a gravitational force that we found in [Chapter 10.6](#sec-10-6) and used in [Chapter 11](#ch-11) when looking at Kepler’s Law’s of Planetary Motion.

::::

(sec-12-4)=
## 12.4 Example Problem: Sphere on an Incline

The following problem includes rolling and translation motion.

(example-12-4)=

::::{admonition} Sample Problem 12-4

A sphere rolls down an incline of angle $\theta$ without slipping. Assume that the moment of inertia of the sphere is $\frac{2}{5} MR^{2}$. **Solve the Euler-Lagrange equations for the** **rolling sphere.** Assume $U$ = 0 at $x$ = 0 at the top of the incline.

::::

<!-- Source PDF page 266; printed label 257. -->

:::{figure} ../images/figures/figure-12-4.png
:label: fig-12-4
:enumerator: 12.4
:alt: Figure shows a sphere rolling down an inclined plane where.
:width: 186px

A sphere of radius $R$ rolls down an incline of angle $\theta$.
:::

**Solution**

First, we need the potential and kinetic energies. The only source of potential energy is the change in gravitational potential energy as the sphere rolls down. For kinetic energy, we have the translation and rotation of the sphere.

Since the motion is along the incline only, we will define $\hat{x}$ to be pointing down along the incline, where $U$ = 0 at $x$ = 0 (the top of the incline). [Figure 12.5](#fig-12-5) shows our coordinate system in terms of $x$. With this definition, the height of the sphere from the top of the incline as a function of $x$ is $x\sin \theta$:

:::{figure} ../images/figures/figure-12-5.png
:label: fig-12-5
:enumerator: 12.5
:alt: Figure shows a right triangle defining the height as a function of distance down the incline.
:width: 248px

Using Pythagorean theorem we can determine the change in height of the sphere.
:::

The potential energy is therefore:

$$
U = -Mg\Delta h
$$

$$
U = -Mgx\sin \theta
$$

The potential energy is negative because $U$ decreases as the sphere rolls down and we have defined $x$ as positive pointing down the incline (how we defined the coordinate system).

For the kinetic energy, we have the translation and rotation motion of the sphere, which we defined in [Chapter 8](#ch-8). The kinetic energy is:

$$
K = \frac{1}{2} M\dot{x}^{2}+ \frac{1}{2} I\omega ^{2}
$$

<!-- Source PDF page 267; printed label 258. -->

::::{admonition} Continued

For a sphere, $I = \frac{2}{5} MR^{2}$ (see [Appendix A.4](#sec-A-4)) it is rolling without slipping, which means

$$
\omega = \frac{v_{cm}}{R} = \frac{\dot{x}}{R}
$$

Substituting the moment of inertia equation and the rolling without slipping condition, the kinetic energy becomes:

$$
K = \frac{1}{2} M\dot{x}^{2}+ \frac{1}{2} \bigg(\frac{2}{5} \bigg)MR^{2}\bigg(\frac{\dot{x}}{R} \bigg)^{2}= \frac{7}{10} M\dot{x}^{2}
$$

Now we can solve for the Lagrangian:

$$
L = K - U = \frac{7}{10} M\dot{x}^{2}+ Mgx\sin \theta
$$

Note that $\theta$ is constant and not a coordinate axis in this problem. This Lagrangian is in 1-D (all motion is along the $\hat{x}$ axis).

The Euler-Lagrange equations are:

$$
\frac{\partial L}{\partial x} = Mg\sin \theta
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\mathrm{d}}{\mathrm{d}t} \bigg(\frac{7}{5} M\dot{x}\bigg) = \frac{7}{5} M\ddot{x}
$$

To solve for the motion itself, we equate the two Euler-Lagrange equations:

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) &= \frac{\partial L}{\partial x} \\
\frac{7}{5} M\ddot{x} &= Mg\sin \theta \\
\ddot{x} &= \frac{5}{7} g\sin \theta
\end{aligned}
$$

Thus, our acceleration is proportional to gravity, with a $\sin\theta$ term due to the incline, as expected. The additional factor of $5/7$ is due to the fact that the sphere is rolling down the incline instead of sliding.

::::

(sec-12-5)=
## 12.5 Challenging Problem: Particle on a Wire

For this problem, the solution is not a simple differential equation. Consider whether you would try to solve this problem using Newton’s Laws or energy conservation.

<!-- Source PDF page 268; printed label 259. -->

(example-12-5)=

::::{admonition} Sample Problem 12-5

A particle of mass $m$, moves along a bent wire. The shape of the wire can be described with the equation $y = ax^{4}$. (Note that the wire equation represents the path the particle can move along.) **What is the equation of motion for the particle?**

:::{figure} ../images/figures/figure-12-6.png
:label: fig-12-6
:enumerator: 12.6
:alt: Figure shows a parabolic-like wire with a bead on it on Cartesian coordinates.
:width: 217px

The function $y = ax^{4}$ is the the path that particle of mass $m$ moves along.
:::

**Solution**

To help solve this problem, we will break it down into a few parts. We will get the equation of motion when we have expressions for $K$ and $U$. That means we need to describe the motion of the particle at any given time and we need to describe the position of the particle at any give time.

**a) What is the velocity of the particle?**

Since the particle moves in two-dimensions, $x$ and $y$, we have:

$$
\vec{v} = \dot{x}\hat{\imath} + \dot{y}\hat{\jmath}
$$

The position in the y-direction can be described by the equation of the wire, $y = ax^{4}$ so the y-velocity is the derivative with respect to time of our y-position, $\dot{y} = 4ax^{3}\dot{x}$ . This means that:

$$
\vec{v} = \dot{x}\hat{\imath} + 4ax^{3}\dot{x}\hat{\jmath}
$$

**b) Solve the Lagrangian.**

We know that,

$$
L = K - U
$$

::::

<!-- Source PDF page 269; printed label 260. -->

so let’s find our kinetic and potential energies. We only have translation kinetic energy from the motion of the particle,

$$
K = \frac{1}{2} mv^{2}
$$

where,

$$
v^{2}= \vec{v} \cdot \vec{v}
$$

$$
v^{2}= \dot{x}^{2}+ \dot{y}^{2}
$$

$$
v^{2}= \dot{x}^{2}+ (4ax^{3}\dot{x})^{2}
$$

$$
v^{2}= \dot{x}^{2}+ 16a^{2}x^{6}\dot{x}^{2}
$$

$$
v^{2}= \dot{x}^{2}(1 + 16a^{2}x^{6})
$$

Therefore, we can solve for the kinetic energy in terms of $x$ and $\dot{x}$ only.

$$
K = \frac{1}{2} m\dot{x}^{2}(1 + 16a^{2}x^{6})
$$

The only source of potential energy is gravity,

$$
U = mgh =\Rightarrow \mathrm{where} h = y
$$

$$
U = mgy =\Rightarrow \mathrm{where} U = 0 \mathrm{when} y = 0
$$

$$
U = mgax^{4}
$$

Note that $U$ is positive since the particle is above the $y$ = 0 point, so $U > 0$. We can now solve our Lagrangian:

$$
\begin{aligned}
L &= K - U \\
L &= \frac{1}{2} m\dot{x}^{2}(1 + 16a^{2}x^{6}) - mgax^{4}
\end{aligned}
$$

**c) Find the differential equation of motion of the bead.**

To do this let’s solve the Euler-Lagrange equation:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$

<!-- Source PDF page 270; printed label 261. -->

::::{admonition} Continued

We can start by solving the left-side:

$$
\begin{aligned}
\frac{\partial L}{\partial x} &= \frac{\partial}{\partial x} \bigg[\frac{1}{2} m\dot{x}^{2}(1 + 16a^{2}x^{6}) - mgax^{4}\bigg] \\
\frac{\partial L}{\partial x} &= \frac{1}{2} m\dot{x}^{2}\Big[16a^{2}(6x^{5})\Big] - 4mgax^{3} \\
\frac{\partial L}{\partial x} &= 48m\dot{x}^{2}a^{2}x^{5}- 4mgax^{3}
\end{aligned}
$$

Now let’s solve the right-side:

$$
\begin{aligned}
\frac{\partial L}{\partial\dot{x}}
&=\frac{\partial}{\partial\dot{x}}
\left[\frac12m\dot{x}^2(1+16a^2x^6)-mgax^4\right]\\
&=m\dot{x}(1+16a^2x^6),\\
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot{x}}\right)
&=\frac{\mathrm{d}}{\mathrm{d}t}\left[m\dot{x}(1+16a^2x^6)\right].
\end{aligned}
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = m\ddot{x}(1 + 16a^{2}x^{6}) + m\dot{x}(96a^{2}x^{5}\dot{x})
$$

Now we can equate the two sides and solve for the differential equation of motion:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$

$$
m\ddot{x}(1 + 16a^{2}x^{6}) + m\dot{x}(96a^{2}x^{5}\dot{x}) = 48m\dot{x}^{2}a^{2}x^{5}- 4mgax^{3}
$$

$$
m\ddot{x}(1 + 16a^{2}x^{6}) + m\dot{x}(48^{2}x^{5}\dot{x}) + 4mgax^{3}= 0
$$

$$
\ddot{x}(1 + 16a^{2}x^{6}) + \dot{x}(48^{2}x^{5}\dot{x}) + 4gax^{3}= 0
$$

The solution is a differential equation of motion, but it is difficult to solve because it is non-linear with respect to both $x$ and $\dot{x}$ . Thus, we leave the equation in this form.

1. Try solving this problem using energy conservation. Hint: Remember that energy conservation uses full derivatives and not partial derivatives.

2. If you were to try Newton’s law, to solve this problem, what other force is acting on the bead other than gravity (it is this force that makes applying Newton’s laws difficult)?

::::

<!-- Source PDF page 271; printed label 262. -->

(sec-12-6)=
## 12.6 Real-World Applications

Initially, it might seem like the Euler-Lagrange Method is unnecessarily complicated, but we’re really just touching the edge of what it can be used for. Remember that this textbooks is still mostly focusing on simple, idealized problems. The real world of experimentation and research is much more complex, and many physics problems don’t have simple, analytical solutions and can only be probed numerically using computers.

Lagrangian mechanics help simplify the calculations for complex or even chaotic systems where forces are hard to define or the initial conditions can drastically change the outcome (e.g., consider the [motion of a double pendulum](https://www.youtube.com/watch?v=czLIj-4suOk)). In terms of physics research, solving problems with the Euler-Lagrange method is often more efficient when mapping the motion of stars in galactic mergers or near supermassive black holes, tracing particle collisions in accelerators, solving problems in fluid mechanics, or tracking systems of particles in thermodynamics or quantum mechanics. The Euler-Lagrange equations are a tool to break down big problems into smaller calculations.

One common application of Lagrangian mechanics is with magnetohydrodynamics (MHD), which is the study of fluids that conduct electrically. MHD is used in many branches of physics, but one example is nuclear fusion experimentation, where many experiments seek to produce energy by magnetically confining a fast-moving plasma in a torus. MHD research must solving various equations such as the equation of state, mass continuity, Faraday’s law, and Ohm’s law simultaneously for the entire system, and these equations are usually non-linear with time. As such, Lagrangian mechanics are often employed to simplify the problem.

For more information: [Wikipedia webpage on MHD](https://en.wikipedia.org/wiki/Magnetohydrodynamics), listing various forms and equations. [Science article](https://www.science.org/content/article/bizarre-reactor-might-save-nuclear-fusion) on some recent nuclear fusion experiment designs.

(sec-12-7)=
## 12.7 Summary on the Lagrange Method

::::{admonition} Key Takeaways

We have shown that the Lagrange method involves two main steps. First, you define the Lagrangian:

$$
L = K - U
$$

Second, you solve the Euler-Lagrange equations. For example, for motion in the $x-$axis only:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) = \frac{\partial L}{\partial x}
$$

::::

<!-- Source PDF page 272; printed label 263. -->

::::{admonition} Continued

The Euler-Lagrange equations and the Lagrangian hold under very general circumstances. You can apply these equations to n-dimensional systems (e.g., you do not need to be restricted to 3 dimensions). Systems in n-dimension are often called Euclidean space. In broad terms, you can express the Euler-Lagrange equations as:

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}_{i}} \Bigg) = \frac{\partial L}{\partial x_{i}}
$$

where $x_{i}$ represents a coordinate (and these do not need to be Cartesian coordinates).

**Strategies for employing the Lagrange method successfully**.

1. Choose your coordinate system carefully. You want a coordinate system that simplifies the problem.

2. Write out $K$ and $U$ and $L = K -U$. Note that the physics is just in $L = K -U$, so once you have the Lagrangian, you have finished with the physics.

3. Solve the Euler-Lagrange equations for each coordinate system separately. Note that a constant in the potential (e.g., $U \rightarrow U(x_{i}) + U_{0})$ does not affect the solution. So you do not care about constant values for the potential.

4. If $L$ does not depend on a position coordinate (e.g., $x_i$), then $\partial L/\partial x_i=0$ and $\partial L/\partial\dot{x}_i$ is a constant. See for example the Gravity example in [Section 12.3](#sec-12-3).

5. Once you have $L$, you can obtain the equation of motion using the Euler-Lagrange equations.

::::

::::{admonition} Important Equations

**Lagrangian: Euler-Lagrange Equation:**

$$
\begin{aligned}
L &= K - U \\
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}} \Bigg) &= \frac{\partial L}{\partial x}
\end{aligned}
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t} \Bigg(\frac{\partial L}{\partial \dot{x}_{i}} \Bigg) = \frac{\partial L}{\partial x_{i}}
$$

::::

<!-- Source PDF page 273; printed label 264. -->

(sec-12-8)=
## 12.8 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-12-1)=

::::{admonition} Practice Problem 12-1

Use the Euler-Lagrange method to find the differential equation of motion for a vertical spring and confirm you get the same answer as [Chapter 3](#ch-3).

::::

(problem-12-2)=

::::{admonition} Practice Problem 12-2

Use the Euler-Lagrange method to find the differential equation for a physical pendulum that is constructed from a rod of length $L$ and mass $M$ that is pivoted at one end. Confirm that you get the same answer as [Chapter 7](#ch-7).

::::

(problem-12-3)=

::::{admonition} Practice Problem 12-3

A mass $M$ sits at the top of a frictionless incline of angle $\theta$ and slides down the plane. Use the Euler-Lagrange equations to find the differential equation of motion.

::::

(problem-12-4)=

::::{admonition} Practice Problem 12-4

An ideal string is wrapped around a disk of mass $M$ and radius $R$ so that it unwinds as the disk falls. If the moment of inertia of the disk is $\frac{1}{2} MR^{2}$, what is the Lagrangian for this motion? Assume that the disk moves without slipping and only gravity affects this system. Assume $U$ = 0 at $y$ = 0.

:::{figure} ../images/figures/figure-12-7.png
:label: fig-12-7
:enumerator: 12.7
:alt: Figure shows the disk attached to a strong on one end that is a distance y from the top.
:width: 108px

Figure for [Problem 12-4](#problem-12-4).
:::

::::

<!-- Source PDF page 274; printed label 265. -->

(problem-12-5)=

::::{admonition} Practice Problem 12-5

Two identical blocks of mass $m$ are connected by an ideal rope. One block is placed on a smooth horizontal table and the other block hangs over the edge. When the second hanging block is released, it pulls on the first block. Find the Euler-Lagrange equations while the first block remains on the table. Assume $U$ = 0 at the height of the table.

::::

(problem-12-6)=

::::{admonition} Practice Problem 12-6

A block of mass $m$ is attached to a spring with constant $k$ on an incline as shown in the figure. If the block is displaced a small value $x$ from the equilibrium position,

a) What is the kinetic energy of the mass?

b) What is the potential energy of the mass?

c) Find the Lagrangian of the system and solve the Euler-Lagrange equations.

:::{figure} ../images/figures/figure-12-8.png
:label: fig-12-8
:enumerator: 12.8
:alt: Figure shows a simple spring-mass system on an inclined plane where the mass is supported from the top of the incline.
:width: 217px

Figure for [Problem 12-6](#problem-12-6).
:::

::::

(problem-12-7)=

::::{admonition} Practice Problem 12-7

Two masses are joined by an ideal rope across an ideal pulley as shown. Mass $M_{2}$ hangs over the edge and mass $M_{1}$ sits on a frictionless incline. Use the Euler-Lagrange equations to find the differential equation of motion.

:::{figure} ../images/figures/figure-12-9.png
:label: fig-12-9
:enumerator: 12.9
:alt: Figure shows the set up of two masses and a pulley with an incline.
:width: 310px

Figure for [Problem 12-7](#problem-12-7).
:::

::::

<!-- Source PDF page 275; printed label 266. -->

(problem-12-8)=

::::{admonition} Practice Problem 12-8

A circular disk of mass $M$ and radius $R$ hangs from a pivot point that is displaced from the centre of mass by a distance $s = R/2$ as shown.

a) What is the Lagrangian for this system?

b) Check that this answer makes sense by applying the Euler-Lagrange equations and showing that you get a standard differential equation of motion.

:::{figure} ../images/figures/figure-12-10.png
:label: fig-12-10
:enumerator: 12.10
:alt: Figure shows a physical pendulum disk that is pivoted a small distance above its center.
:width: 93px

Figure for [Problem 12-8](#problem-12-8).
:::

::::

(problem-12-9)=

::::{admonition} Practice Problem 12-9

A snowboarder of mass $m$ is sliding on a frictionless half-pipe that has a cycloid shape described by:

$$
\begin{aligned}
x &= \frac{a}{4} (2\theta + \sin 2\theta) \\
y &= \frac{a}{4} (1 - \cos 2\theta)
\end{aligned}
$$

where $a$ is a constant and 0 $< \theta < \pi$. See the figure below.

a) If gravity is the only force on the snowboarder, find the potential energy. Express this in terms of $\theta$ and $\dot{\theta}$ .

b) What is the kinetic energy of the snowboarder? Express this in terms of $\theta$ and $\dot{\theta}$ .

c) What is the Lagrangian of the system? Express this in terms of $\theta$ and $\dot{\theta}$ .

d) Use the Euler-Lagrange equations to find the differential equation of motion. Do not solve this equation.

::::

<!-- Source PDF page 276; printed label 267. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-12-11.png
:label: fig-12-11
:enumerator: 12.11
:alt: Figure shows a cartoon snowboarder on a parabollic-like track with Cartesian coordinates labeled.
:width: 232px

Figure for [Problem 12-9](#problem-12-9).
:::

::::

(problem-12-10)=

::::{admonition} Practice Problem 12-10

See the figure below. A mass $M$ hangs from a spring that is allowed to expand/contract and rotate. Assume that the potential energy from gravity is zero at the pivot point.

a) Describe how the system would move if it is displaced a small distance $x$ along the axis of the spring and an angle $\theta$ from the vertical.

b) What is the potential energy of this system?

c) What is the kinetic energy of this system?

d) Use the Lagrange method to find the differential equation of motion for this system? Note: you must solve the $x$ and $\theta$ terms separately. Do not solve the differential equation.

:::{figure} ../images/figures/figure-12-12.png
:label: fig-12-12
:enumerator: 12.12
:alt: Figure shows mass hanging from a vertical spring that allowed to move as a pendulum and a spring.
:width: 139px

Figure for [Problem 12-10](#problem-12-10).
:::

::::
