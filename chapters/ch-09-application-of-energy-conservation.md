(ch-9)=
# 9. Application of Energy Conservation

<!-- Source PDF page 198; printed label 189. -->

::::{admonition} Learning Objectives

- Apply energy conservation to problems involving rolling and translation

- Apply energy conservation to problems involving simple harmonic motion

- Identify the differential equation of motion from energy conservation

::::

In this chapter, we will apply energy conservation to solve problems in physics. Throughout this chapter, compare the method of energy conservation to using Newton’s laws.

(sec-9-1)=
## 9.1 Energy Conservation

In [Chapter 8](#ch-8), we showed that conservative forces had the property of

$$
\Delta K + \Delta U = 0
$$ (eq-9-1)

where $K$ is the kinetic energy and $U$ is the potential energy. This result indicates that $K + U = E$ = constant.

$$
K + U = E = \mathrm{constant}
$$ (eq-9-2)

where $E$ is the mechanical energy of the system. If $E$ is a constant, then your mechanical energy equals the total (kinetic plus potential) energy of your system.

Because energy is scalar instead of a vector quantity, it is sometimes easier to solve a question using energy conservation than using Newton’s Laws. The important points to consider are:

1. What are your sources of kinetic energy (translation versus rotation)?

2. What are your sources of potential energy?

3. How can you write both forms of energy in terms of the parameters needed and in terms of time?

If you can answer those questions, you can solve physics problems using energy conservation.

If energy is conserved, you can compare the energy before and after the motion. The total energy initially must equal the total energy at the end. Any gain or loss in kinetic energy corresponds to a gain or loss in potential energy. This is similar to how we applied the conservation of momentum and angular momentum to problems.

$$
E_{i}= E_{f}
$$

$$
K_{i}+ U_{i}= K_{f}+ U_{f}
$$

<!-- Source PDF page 199; printed label 190. -->

For this method to be applicable, you need to have a clearly defined energy (potential and kinetic) for at least one point in the motion.

Alternatively, if energy is conserved, then $E$ is a constant and

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0
$$ (eq-9-3)

For this method to be applicable, you need to express the energy as a function of a time $t$.

(sec-9-2)=
## 9.2 Energy Conservation in 3-D

Consider a particle moving in 3-D,

$$
\begin{aligned}
K &= \frac{1}{2} m(\vec{v} \cdot \vec{v}) =\Rightarrow \mathrm{Note} \mathrm{that} \vec{v} \cdot \vec{v} = v^{2} \\
&= \frac{1}{2} m(\dot{x}^{2}+ \dot{y}^{2}+ \dot{z}^{2})
\end{aligned}
$$

in the case of Cartesian coordinates and linear motion.

Now, the rate of change of the kinetic energy for this particle is given by ![Formula, source page 199](../images/math/p199-59cfa506e2cd.svg) . This does not need to be constant with time (although $E$ is assumed to be constant).

$$
\begin{aligned}
\frac{\mathrm{d}K}{\mathrm{d}t} &= \frac{1}{2} m \frac{\mathrm{d}}{\mathrm{d}t} (\dot{x}^{2}+ \dot{y}^{2}+ \dot{z}^{2}) \\
\frac{\mathrm{d}K}{\mathrm{d}t} &= \frac{1}{2} m(2\dot{x}\ddot{x} + 2\dot{y}\ddot{y} + 2\dot{z}\ddot{z}) \\
\frac{\mathrm{d}K}{\mathrm{d}t} &= m(\dot{x}\ddot{x} + \dot{y}\ddot{y} + \dot{z}\ddot{z}) =\Rightarrow \mathrm{Note} \mathrm{the} \mathrm{bracket} \mathrm{term} \mathrm{is} \dot{\vec{r}} \cdot \ddot{\vec{r}} \\
\frac{\mathrm{d}K}{\mathrm{d}t} &= m\dot{\vec{r}} \cdot \ddot{\vec{r}} \\
\frac{\mathrm{d}K}{\mathrm{d}t} &= \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \cdot \vec{F} =\Rightarrow \mathrm{Recall} \mathrm{that} \vec{F} = m\vec{a} = m\ddot{\vec{r}} \\
\mathrm{d}K &= \mathrm{d}\vec{r} \cdot \vec{F}
\end{aligned}
$$

Due to symmetry with the dot product, we can say that $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$. So we end up with:

$$
\mathrm{d}K = \vec{F} \cdot \mathrm{d}\vec{r}
$$

$$
\mathrm{d}K = \mathrm{d}W_{net}
$$

which is just our work-kinetic energy theorem again.

What about the potential energy? Well, our potential energy must be dependent on position (a conservative force depends on position). Assume that $U \rightarrow U(\vec{r})$.

$$
\frac{\mathrm{d}U}{\mathrm{d}t} = \frac{\mathrm{d}U(\vec{r})}{\mathrm{d}t}
$$

d$U \partial U$ d$x \partial U$ d$y \partial U$ d$z$

:::{image} ../images/math/p199-a3204d421bd0.svg
:alt: Mathematical expression from source PDF page 199
:class: source-equation
:align: center
:::

<!-- Source PDF page 200; printed label 191. -->

$$
\partial U \partial U \partial U
$$

Recall that ![Formula, source page 200](../images/math/p200-4b63debb297c.svg) . Therefore, we can re-write the above as:

$$
\partial x \partial y \partial z
$$

$$
\frac{\mathrm{d}U}{\mathrm{d}t} = \vec{\nabla}U \cdot \frac{\mathrm{d}\vec{r}}{\mathrm{d}t}
$$

So if we assume that we only have conservative forces, then $E = K + U$ then the time derivative of the energy is:

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= \frac{\mathrm{d}K}{\mathrm{d}t} + \frac{\mathrm{d}U}{\mathrm{d}t} \\
&= \vec{F} \cdot \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} + \vec{\nabla}U \cdot \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \\
&= \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \cdot (\vec{F} + \vec{\nabla}U)
\end{aligned}
$$

Since $\vec{F} = -\vec{\nabla}U$ for a conservative force, we get

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \cdot (\vec{F} + \vec{\nabla}U) = \frac{\mathrm{d}\vec{r}}{\mathrm{d}t} \cdot (\vec{F} - \vec{F}) = 0
$$

for any velocity for the particle. So if you have a system that is fully described by conservative forces in any dimension, then that system will have its total energy conserved.

Keep in mind that not all forces that are functions of position are conservative forces. For a system to have a conservative force, $\vec{\nabla} \times \vec{F}$ = 0 (see [Chapter 8](#ch-8)) or the work done on the system within a close loop must be zero.

(example-9-1)=

::::{admonition} Sample Problem 9-1

Consider a force $\vec{F} = -ky\hat{\imath}+kx\hat{\jmath}$ . **Show that the work done on a particle by this** **force in a closed loop does not equal to zero.**

**Solution**

While one could demonstrate that $\vec{F}$ is a conservative force by showing $\vec{\nabla}\times \vec{F} \not =$ 0, the problem specifically asks to show the solution for a closed loop. To solve this problem, we need to evaluate the integral:

$$
\oint \vec{F} \cdot \mathrm{d}\vec{r}
$$

where $\oint$ indicates a closed loop. You can take any closed loop for a conservative force. So it is handy to take a direct (simple) closed path. [Figure 9.1](#fig-9-1) shows a very simple closed loop from $(0,0) \rightarrow (a,0) \rightarrow (a,b) \rightarrow (0,b) \rightarrow (0,$ 0). You can technically do any closed loop, but make the math easy for yourself and take something simple.

::::

<!-- Source PDF page 201; printed label 192. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-9-1.png
:label: fig-9-1
:enumerator: 9.1
:alt: Figure shows a closed square loop drawn in the x-y plane.
:width: 217px

A simple closed loop. You can define any closed loop for conservative forces, but direct paths are the most mathematically simple to use. Here we have four paths that are labeled as (1), (2), (3), and (4).
:::

So we can break up the work for this system using each of the different path legs. For the first path length (1), it is entirely along the $x-$axis, so we can solve the work from just $F_{x}$ because no work is being done in $y$ along that axis.

$$
W_{1}= W(0,0) \rightarrow W(a,0) = \int_{0}^{a} F_{x}\mathrm{d}x = -ky\int_{0}^{a} \mathrm{d}x = -kya = 0
$$

because $y$ = 0 for this section, (e.g., $W_{1}= -kya$ = 0 because $y$ = 0).

We can make similar calculations for the other sections.

$$
\begin{aligned}
W_{2}&= W(a,0) \rightarrow W(a,b) = _{0}^{b}F_{y}\mathrm{d}y = kx _{0}^{b}\mathrm{d}y = kxb = kab (x = a) \\
W_{3}&= W(a,b) \rightarrow W(0,b) = \int_{a}^{0} F_{x}\mathrm{d}x = -k\int y\int_{a}^{0} \mathrm{d}x = kya = kab (y = b) \\
W_{4}&= W(0,b) \rightarrow W(0,0) = _{b}^{0}F_{y}\mathrm{d}y = kx _{b}^{0}\mathrm{d}y = -kxb = 0 (x = 0)
\end{aligned}
$$

So the total work done in this closed loop is $W = W_{1}+W_{2}+W_{3}+W_{4}= 0+kab+kab+0$ = $2kab \not =$ 0. So the above force is *not* conservative.

1. Confirm that the force $\vec{F} = -ky\hat{\imath}+kx\hat{\jmath}$ is not conservative by taking $\vec{\nabla}\times \vec{F}$ .

2. Is $\vec{F} = (xy)\hat{\imath}+(xz)\hat{\jmath}+(yz)\hat{k}$ conservative? Try both the closed loop and the curl methods. Which do you like better?

::::

<!-- Source PDF page 202; printed label 193. -->

(sec-9-3)=
## 9.3 Example Problems: Gravity and Rotation

(example-9-2)=

::::{admonition} Sample Problem 9-2

A uniform spherical shell of mass $M$ and radius $R$ is able to rotate about a vertical axis without friction ([Figure 9.2](#fig-9-2)). A massless rope passes around the shell at its equator and over a pulley to a smaller mass $m$ that is hanging over the edge of a table. **If there** **are no losses in energy, what is the velocity of the mass** $m$ **after it has fallen** **a distance** $h$ **from rest?** Assume the pulley is a disk with mass $M_{p}$ and radius $R_{p}$.

:::{figure} ../images/figures/figure-9-2.png
:label: fig-9-2
:enumerator: 9.2
:alt: Figure shows the setup of the problem with a sphere, pulley, and hanging mass.
:width: 161px

The set up for this problem shows the spherical shell of mass $M$ and $R$ that can rotate on an axis. There is a disk-pulley with mass $M_{p}$ and radius $R_{P}$ that can likewise rotate about an axis. There is a mass $m$ hanging over the edge that can descend due to gravity. There is no friction (no energy loss) and that the rope has no mass and cannot stretch.
:::

**Solution**

First, how will this system move? At time $t$ = 0, everything is at rest. Then the mass $m$ is released and drops a distance $h$, pulling on the rope and subsequently rotating the pulley and the spherical shell (see blue marks in [Figure 9.2](#fig-9-2)).

You can try to solve this problem using forces, torques, and Newton’s laws, but we will use energy here. We are told that there are no losses in energy, so the only force driving the motion is gravity, which is a conservative force.

Energy conservation requires measuring $\Delta U$ and $\Delta K$. So we need to consider all the sources of potential energy and all the sources of kinetic energy.

*Potential energy*: In this case, there is only one source of potential energy, the little mass $m$. It drops in height where the change in height is $\Delta y = -h$, where the negative indicates that the object decreased in height from its original reference position (it’s position at $t$ = 0). Recall that potential energy from gravity is equal to $U_{g}= mg\Delta y$, if you assume that the gravitational acceleration is constant (see [Chapter 8](#ch-8)). Thus, we can take any convenient reference position for $\Delta y$. The height at $t$ = 0 is a convenient reference position, so we’ll use that. Therefore, we have

$$
\Delta U = -mgh
$$

::::

<!-- Source PDF page 203; printed label 194. -->

There is a loss of potential energy, which means there will be a gain in kinetic energy, as expected.

*Kinetic energy:* Initially, everything is at rest, so $K_{i}$ = 0. But after the mass $m$ moves, there are three sources of kinetic energy. There is the moving mass $m$, the rotating pulley, and the rotating spherical shell.

$$
\begin{aligned}
K &= K_{m}+ K_{p}+ K_{s} \\
K &= \frac{1}{2} mv^{2}+ \frac{1}{2} I_{p}\omega _{p}^{2}+ \frac{1}{2} I_{s}\omega _{s}^{2}
\end{aligned}
$$

where $v = \dot{y}$ is the speed of the mass, $I_{p}$ and $\omega _{p}$ are the moment of inertia and angular velocity of the pulley, and $I_{s}$ and $\omega _{s}$ are the moment of inertia and angular velocity for the spherical shell.

The pulley is a disk, so $I_{p}= \frac{1}{2} M_{p}R_{p}^{2}$. The moment of inertia for a spherical shell is $I_{s}= \frac{2}{3} M_{s}R_{s}^{2}$ (see [Appendix A.4](#sec-A-4)). Since the rope is massless and cannot be stretched (it is inextensible), the velocity at any point of the rope must be constant. If we say that the mass moves at a velocity $v$, then the velocity vector where the rope meets the pulley has a speed $v$ and the velocity vector where the rope meets the shell has a speed $v$. So the pulley and shell have the same linear velocity $v$ at the radii where the rope contacts them. That means the linear velocity is $v$ at a radius of $R_{s}$ for the shell at at a radius of $R_{p}$ for the pulley.

Since we have only rolling motion, we can say:

$$
\begin{aligned}
\omega _{p}&= \frac{v}{R_{p}} \\
\omega _{s}&= \frac{v}{R_{s}}
\end{aligned}
$$

Taking our equations for the angular speeds and the moments of inertia, we get:

$$
\begin{aligned}
K &= \frac{1}{2} mv^{2}+ \frac{1}{2} I_{p}\omega _{p}^{2}+ \frac{1}{2} I_{s}\omega _{s}^{2} \\
K &= \frac{1}{2} mv^{2}+ \frac{1}{2} \bigg(\frac{1}{2} M_{p}R_{p}^{2}\bigg)\Bigg(\frac{v}{R_{p}} \Bigg)^{2}+ \frac{1}{2} \bigg(\frac{2}{3} M_{s}R_{s}^{2}\bigg)\bigg(\frac{v}{R_{s}} \bigg)^{2} \\
K &= \frac{1}{2} mv^{2}+ \frac{1}{4} M_{p}v^{2}+ \frac{1}{3} M_{s}v^{2}
\end{aligned}
$$

So our change in kinetic energy is:

$$
\begin{aligned}
\Delta K &= K_{f}- K_{i} \\
\Delta K &= \frac{1}{2} mv^{2}+ \frac{1}{4} M_{p}v^{2}+ \frac{1}{3} M_{s}v^{2}
\end{aligned}
$$

<!-- Source PDF page 204; printed label 195. -->

::::{admonition} Continued

From the conservation of energy, we have $\Delta K = -\Delta U$. Sub in our equations for $\Delta K$ and $\Delta U$.

$$
\begin{aligned}
-\Delta U &= \Delta K \\
mgh &= v^{2}\bigg(\frac{1}{2} m + \frac{1}{4} M_{p}+ \frac{1}{3} M_{s}\bigg)
\end{aligned}
$$

$$
v^{2}= \frac{mgh}{\frac{1}{2} m + \frac{1}{4} M_{p}+ \frac{1}{3} M_{s}}
$$

:::{image} ../images/math/p204-14b558551b11.svg
:alt: Mathematical expression from source PDF page 204
:class: source-equation
:align: center
:::

So we have solved for the speed of the mass. To get the velocity, we need to specify a direction. In this case, we know that the mass is falling down, so the direction would be down.

::::

(example-9-3)=

::::{admonition} Sample Problem 9-3

Let’s try to solve the motion of a Atwood Machine where the pulley is a disk of mass $M$ and radius $R$. The hanging masses of mass $M_{1}$ and $M_{2}$. See [Figure 9.3](#fig-9-3). Assume that the rope connecting the masses is light (negligible mass) and inextensible (any stretch of the rope is negligible) and that the pulley has a frictionless ball bearing (so no energy losses). **What is the acceleration of the two masses?**

:::{figure} ../images/figures/figure-9-3.png
:label: fig-9-3
:enumerator: 9.3
:alt: Figure shows a single Atwood machine with two masses.
:width: 124px

The Atwood machine. Assume that the rope is inextensible and that there is no friction on the bearing for the pulley. The pulley is a disk of mass $M$ and radius $R$.
:::

**Solution**

While this problem can also be solved using Newton’s laws and forces, let’s look at energy conservation.

$$
K + U = E = \mathrm{constant}
$$

::::

<!-- Source PDF page 205; printed label 196. -->

First step is to consider all sources of kinetic energy and all sources of potential energy.

For potential energy, we have the two masses within a gravitational field. For small distances, we can assume that $F_{g}= mg$ and that means that $U = mg\Delta y$, where $\Delta y$ indicates the change in vertical. If we set $y$ = 0 to be at the midpoint of the pulley (see [Figure 9.4](#fig-9-4)), then the potential energy of the masses are $U_{1}= -mgy_{1}$ and $U_{2}= -mgy_{2}$, where $y_{1}$ and $y_{2}$ are the positions of the masses relative to the pulley.

:::{figure} ../images/figures/figure-9-4.png
:label: fig-9-4
:enumerator: 9.4
:alt: Figure shows the positions of the two masses relative to the center of the pulley.
:width: 248px

Position of masses in the Atwood machine. The midpoint of the pulley sets the $y$ = 0 point, with the masses distances $y_{1}$ and $y_{2}$ being measured from the $y$ = 0.
:::

Note that there is no potential energy from the pulley because the pulley does not move vertically. So there is no work done by gravity in moving the pulley (by its centre of mass).

So our potential energy of the system is given by:

$$
U = -mgy_{1}- mgy_{2}
$$

This is the potential energy for a given time, $t$. We don’t know which mass will move up and which one will move down. All we know is that $m_{1}$ and $m_{2}$ are at specific positions $y_{1}$ and $y_{2}$ at $t$.

For the kinetic energy, there are three sources of kinetic energy in this system. We have the translation motion of $m_{1}$, the translation motion of $m_{2}$, and the rotational motion of the pulley. For the translation motion, we have $K_{1}= \frac{1}{2} m_{1}(\dot{y}_{1})^{2}$ and $K_{2}= \frac{1}{2} m_{2}(\dot{y}_{2})^{2}$. For the rotational motion, we have $K_{p}= \frac{1}{2} I\omega ^{2}$.

$$
\begin{aligned}
K &= K_{1}+ K_{2}+ K_{p} \\
K &= \frac{1}{2} m_{1}(\dot{y}_{1})^{2}+ \frac{1}{2} m_{2}(\dot{y}_{2})^{2}+ \frac{1}{2} I\omega ^{2}
\end{aligned}
$$

Similar to the previous problem, we need to connect the rotational motion to the translation motion. The pulley rotates at an angular speed of $\omega$. Since the rope is inextensible (does not stretch), we can assume that the two masses move at the same speed

<!-- Source PDF page 206; printed label 197. -->

$(|\dot{y}_{1}| = |\dot{y}_{2}| = v)$ and with the same linear speed as the contact point of the pulley, which is $v = R\omega$ (e.g., see [Figure 9.5](#fig-9-5)).

:::{figure} ../images/figures/figure-9-5.png
:label: fig-9-5
:enumerator: 9.5
:alt: Figure shows a diagram of the pulley with its rotation speed at the edge labeled on both sides of contact with the string.
:width: 155px

Rotation of the pulley assuming $m_{1}> m_{2}$. The pulley rotates at the angular speed $\omega$. The velocity of that angular speed at the two points shown will be $v = \omega R$ where $v$ is the speed of the masses.
:::

Re-writing our kinetic energy equation, we have:

$$
1 1 1
$$

![Formula, source page 206](../images/math/p206-eb183369e28e.svg) where $|\dot{y}_{1}| = |\dot{y}_{2}| = \omega R$

$$
\begin{aligned}
2 2 2 \\
1 1 1 \dot{y} ^{2}
\end{aligned}
$$

![Formula, source page 206](../images/math/p206-c3fd78c54fd0.svg) use $\dot{y}_{1}$ for simplicity

$$
\begin{aligned}
2 2 2 R \\
1 1 1 1 \dot{y} ^{2}
\end{aligned}
$$

![Formula, source page 206](../images/math/p206-da9ecad8ddb8.svg) for a disk

$$
\begin{aligned}
2 2 2 2 R \\
K &= \frac{1}{2} m_{1}(\dot{y}_{1})^{2}+ \frac{1}{2} m_{2}(\dot{y}_{1})^{2}+ \frac{1}{4} M(\dot{y}_{1})^{2}
\end{aligned}
$$

Similar to the potential energy, this kinetic energy is for time $t$ when the masses are moving at a speed of $v$. If the system starts at rest, we would need to calculate the change in position of $y_{1}$ and $y_{2}$ to get the change in kinetic energy. But we were not told of an initial configuration. Instead, we have determined $U$ and $K$ at time $t$. So we will use Equation 9.3:

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0
$$

Our total energy is $E = U + K$ which is a constant. So at time $t$, the sum of the potential energy and kinetic energy is:

$$
\begin{aligned}
E &= U + K \\
E &= -mgy_{1}- mgy_{2}+ \frac{1}{2} m_{1}(\dot{y}_{1})^{2}+ \frac{1}{2} m_{2}(\dot{y}_{1})^{2}+ \frac{1}{4} M(\dot{y}_{1})^{2}
\end{aligned}
$$

Since the total energy is constant for a system with only conservative forces, the time derivative of the total energy is zero (Equation 9.3):

<!-- Source PDF page 207; printed label 198. -->

::::{admonition} Continued

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= 0 \\
0 &= \frac{\mathrm{d}}{\mathrm{d}t} \bigg[-mgy_{1}- mgy_{2}+ \frac{1}{2} m_{1}(\dot{y}_{1})^{2}+ \frac{1}{2} m_{2}(\dot{y}_{1})^{2}+ \frac{1}{4} M(\dot{y}_{1})^{2}\bigg] \\
0 &= -m_{1}g\dot{y}_{1}- m_{2}g\dot{y}_{2}+ m_{1}\dot{y}_{1}\ddot{y}_{1}+ m_{2}\dot{y}_{1}\ddot{y}_{1}+ \frac{1}{12} M\dot{y}_{1}\ddot{y}_{1}
\end{aligned}
$$

0 = ![Formula, source page 207](../images/math/p207-a746364a2fcb.svg) sub $\dot{y}_{2}= -\dot{y}_{1}$

$$
\begin{aligned}
2 \\
1
\end{aligned}
$$

0 = ![Formula, source page 207](../images/math/p207-1a7fbaafef56.svg) eliminate $\dot{y}_{1}$

$$
\begin{aligned}
2 \\
0 &= g(m_{2}- m_{1}) + \ddot{y}_{1}\bigg(m_{1}+ m_{2}+ \frac{1}{2} M\bigg) \\
\ddot{y}_{1}&= \frac{g(m_{1}- m_{2})}{m_{1}+ m_{2}+ \frac{1}{2} M}
\end{aligned}
$$

So our acceleration of $m_{1}$ is given by the above equation. And we can find the acceleration of $m_{2}$ from $\ddot{y}_{2}= -\ddot{y}_{1}$.

1. Consider the difference between using Newton’s second law versus energy conservation for the above Atwood question. Which method do you find better or easier to use? Why?

::::

(sec-9-4)=
## 9.4 Application to Simple Harmonic Motion

In general, you can use Newton’s laws or energy conservation to solve simple harmonic motion problems. But there are many cases where energy conservation can save you a lot of extra work. Consider using Newton’s laws to calculate the following problem instead.

(example-9-4)=

::::{admonition} Sample Problem 9-4

Consider a mass $m$ hanging from the center of a disk pulley of mass $M$ and radius $R$ as shown in [Figure 9.6](#fig-9-6). The pulley is supported by an inextensible and massless rope that is fixed to the ceiling at one end and attached to a spring of spring constant $k$ on the other end. If the pulley rotates without slipping, **find the equilibrium position** **and the period of oscillations if the small mass** $m$ **is pulled down a small** **distance.** Assume there is no loss of energy from friction.

::::

<!-- Source PDF page 208; printed label 199. -->

:::{figure} ../images/figures/figure-9-6.png
:label: fig-9-6
:enumerator: 9.6
:alt: Figure shows the setup of the problem with the pulley and a spring supporting a hanging mass.
:width: 167px

A “simple” harmonic oscillator formed by a pulley and spring. The pulley is a disk of radius $R$ and mass $M$ that is held up by an inextensible cord that is attached to the ceiling on one end and attached to a spring of spring constant $k$ on the other end. A small mass $m$ hangs from the centre of the disk.
:::

**Solution**

**Find the equilibrium position.** When you are in equilibrium, there is no movement, so there is no rotation and no velocity. That means that all forces are zero. But before we can answer this question, how do the pulley, mass, and spring move relative to each other?

We can solve for this equilibrium point by setting the net force and net torque on the pulley equal to zero (that will be the equilibrium point). [Figure 9.7](#fig-9-7) shows the free-body diagram for the pulley.

:::{figure} ../images/figures/figure-9-7.png
:label: fig-9-7
:enumerator: 9.7
:alt: Figure shows a free body diagram for the pulley alone with all forces labelled.
:width: 155px

Free-body diagram of the pulley. There is a tension $T_{1}$ from the rope on the left, and a tension $T_{2}$ from the small mass $m$ acting at the centre of mass. The pulley has its own gravity $mg$. And there is the spring force $F_{s}$ acting on the right side of the pulley.
:::

Since we’re in equilibrium, the net torque must be zero. Therefore, $T_{1}= F_{s}$, otherwise the pulley would rotate. For a spring, $F_{s}= -kx = T_{1}$. The other unknown force is $T_{2}$, but that is simply the tension caused by the hanging mass $m$ and therefore $T_{2}= mg$.

<!-- Source PDF page 209; printed label 200. -->

So for our sum of all forces, we have:

$$
\sum F = T_{1}+ F_{s}- Mg - mg
$$

$$
0 = -2kx - g(M + m) =\Rightarrow \mathrm{for} \mathrm{equilibrium}, \sum F = 0
$$

$$
x_{0}= - \frac{g(M + m)}{2k}
$$

**What is the period of small oscillations?** We want the differential equation of motion. If you can get the equation in the form of $\ddot{x} + Cx$ = 0, then you can read off $\omega _{0}^{2}$ and can get the period.

You can solve this problem using forces and torques, but we will use the conservation of energy here.

The potential energy is given by the gravitational potential energy of the two masses and the potential energy of the spring. Thus, our potential energy is:

$$
U = -Mgx - mgx + \frac{1}{2} k\Delta x^{2}
$$

where we have specified that the potential energy is zero for the masses at $x$ = 0. A convenient reference point (e.g., setting $x$ = 0 for the gravitational energy) is at $x_{0}$, since this is a known reference point. Note that the spring potential is *not* zero at $x = x_{0}$. So we need to consider $\Delta x$ for the spring.

The kinetic energy of the spring is given by the motion of translation energy of the mass, the translation energy of the pulley, and the rotation of the pulley.

$$
K = \frac{1}{2} I\omega ^{2}+ \frac{1}{2} Mv^{2}+ \frac{1}{2} mv^{2}
$$

Before we combine the energies this question, let’s first ask how this system will move. The spring will stretch and compress, and this will lower and raise $m$ and the pulley, and the pulley will also rotate. At first glance, you may be tempted to assume that if the mass moves down a distance $x$, then the pulley should move down a distance $x$ and the spring should be stretched a distance $x$. But for this system, the spring will *stretch* *twice as much* as $m$ and $M$ move down because some of the kinetic energy that goes into the pulley and mass is used to rotate the pulley rather than translate the pulley. This is the same principle behind rolling without slipping (see [Chapter 7](#ch-7)).

Let’s look at the motion of the pulley. [Figure 9.8](#fig-9-8) shows the translational and rotational motion of the pulley. First, consider the motion of the mass and pulley. The mass is connected to the pulley at its centre-of-mass by an inextensible rope. Whatever distance one moves, the other will move the same amount, and this motion will equal the motion of the centre-of-mass of the pulley, $v_{cm}$. Since the pulley is also rotating without slipping, we can connect the centre of mass motion directly to the rotation

$$
(v_{cm}= \omega R).
$$

<!-- Source PDF page 210; printed label 201. -->

:::{figure} ../images/figures/figure-9-8.png
:label: fig-9-8
:enumerator: 9.8
:alt: Figure shows the pulley alone with all velocities labelled to demonstrate rolling without slipping in the problem.
:width: 186px

Translation and rotational motion of the pulley from [Figure 9.6](#fig-9-6). The entire disk moves down with $v = v_{cm}$. But when the pulley moves, it will also rotate without slipping with $\omega = v_{cm}/R$. So at point $P$ on the fixed side, the velocity is instantaneously zero.
:::

Second, let’s consider how the spring stretches relative to the pulley’s motion. As the pulley moves down with the stretch of the spring, the pulley will rotate clockwise (see [Figure 9.8](#fig-9-8)). Point $P$ is the contact point for the rotation and the net velocity there will be zero. Note that the contact point will be on the side of pulley that is fixed to the ceiling. That’s because the other side with the spring is able to change in height, not the fixed side. On the side with the spring, however, the velocities from the translation and rotation add together such that pulley moves away from the spring at twice the speed of the centre of mass.

::::{tip} Quick Questions

1. How would the pulley rotate when it is moving upwards (spring is contracting) instead of moving downwards?

2. At what point in the simple harmonic motion is the rotation of the pulley the fastest? Does that make sense?

::::

So this means that if the mass and pulley move $x$ in time $t$, the spring stretches (or compresses) by a displacement of $2x$ in the same time. We must take into account this difference in the spring’s displacement relative to the vertical displacement of the mass and pulley in our energy conservation.

The total energy is

$$
\begin{aligned}
E &= K + U \\
E &= \frac{1}{2} I\omega ^{2}+ \frac{1}{2} Mv^{2}+ \frac{1}{2} mv^{2}- Mgx - mgx + \frac{1}{2} k(2x - x_{0})^{2}
\end{aligned}
$$

where the change in potential energy depends on a displacement of $2x-x_{0}$, because we set our reference position to $x_{0}$ and the spring stretches and compresses at twice the rate that the pulley and mass move.

<!-- Source PDF page 211; printed label 202. -->

::::{admonition} Continued

$$
v
$$

For rotating without slipping, $\omega$ = . So we can simplify the above as:

$$
R
$$

$$
\begin{aligned}
E &= \frac{1}{2} I \bigg(\frac{v}{R} \bigg)^{2}+ \frac{1}{2} Mv^{2}+ \frac{1}{2} mv^{2}- (M + m)gx + \frac{1}{2} k(2x - x_{0})^{2} \\
E &= \frac{1}{2} v^{2} \frac{I}{R^{2}} + M + m\bigg) - (M + m)gx + \frac{1}{2} k(2x - x_{0})^{2} \\
E &= \frac{1}{2} v^{2}\bigg(\frac{1}{2} M + M + m\bigg) - (M + m)gx + \frac{1}{2} k(2x - x_{0})^{2}=\Rightarrow I = \frac{1}{2} MR^{2} \\
E &= \frac{1}{2} v^{2} \frac{3}{2} M + m\bigg) - (M + m)gx + \frac{1}{2} k(2x - x_{0})^{2}
\end{aligned}
$$

Now take the derivative of the energy with respect to time.

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= 0 = \frac{\mathrm{d}}{\mathrm{d}t} \bigg[\frac{1}{2} v^{2}\bigg(\frac{3}{2} M + m\bigg) - (M + m)gx + \frac{1}{2} k(2x - x_{0})^{2}\bigg] \\
0 &= \frac{3}{2} M + m v \frac{\mathrm{d}v}{\mathrm{d}t} - (M + m)gv + k(2x - x_{0})(2v) \\
0 &= \bigg(\frac{3}{2} M + m\bigg) \frac{\mathrm{d}v}{\mathrm{d}t} - (M + m)g + 2k(2x - x_{0}) =\Rightarrow \mathrm{eliminate} v \\
0 &= \frac{\mathrm{d}v}{\mathrm{d}t} + \Bigg(\frac{1}{\frac{3}{2} M + m} \Bigg)\Big[4kx - (M + m)g - 2kx_{0}\Big]
\end{aligned}
$$

:::{image} ../images/math/p211-53b3770c4386.svg
:alt: Mathematical expression from source PDF page 211
:class: source-equation
:align: center
:::

:::{image} ../images/math/p211-622c94dbdb75.svg
:alt: Mathematical expression from source PDF page 211
:class: source-equation
:align: center
:::

Note how we recover the differential equation of motion directly from energy conservation. We have it in the familiar form that we want and we can solve for the period of oscillations easily from this.

$$
\omega _{0}^{2}= \frac{4k}{\frac{3}{2} M + m}
$$

:::{image} ../images/math/p211-df11239e7e80.svg
:alt: Mathematical expression from source PDF page 211
:class: source-equation
:align: center
:::

Try to solve the same problem using torques and forces. Be wary of your vector directions and whatever coordinate system you originally define. You should obtain the exact same solution if done properly.

::::

<!-- Source PDF page 212; printed label 203. -->

(sec-9-5)=
## 9.5 Summary

::::{admonition} Key Takeaways

This chapter applies the concepts from [Chapter 8](#ch-8), in particular those of energy conservation, to physics problems. The main idea of energy conservation is that,

$$
E = U + K = \mathrm{constant}
$$

Energy is conserved if all of the forces acting on your system are conservative forces. If there is a non-conservative force (e.g., friction), then energy will not be conserved and $E$ will not be constant.

There are two main approaches to solving physics problems with energy conservation.

1. You can derive independent equations for $E$ at two different times, $E_{1}$ and $E_{2}$. If you can derive an equation for the energy at two distinct times (e.g., you are given a reference speed and position), then you can solve the physics of a problem by setting $E_{1}= E_{2}$.

2. You can derive an general equation for the energy for any given time, $t$. In this case, you do not have a unique solution for $E$ from your energy equation alone. Nevertheless, since energy is conserved, it is constant with time, which means

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0
$$

By setting the time derivative of $E$ to zero, you will obtain a differential equation of motion from which you can use to solve the physics problem.

While going through this chapter and the practice problems below, compare how the solution from energy conservation with what you would need to do if you were applying Newton’s second law instead. Consider which method you prefer and under which circumstances you would favour one over the other.

::::

::::{admonition} Important Equations

**Energy Conservation:**

$$
\Delta K + \Delta U = 0
$$

$$
\begin{aligned}
K + U &= E = \mathrm{constant} \\
\frac{\mathrm{d}E}{\mathrm{d}t} &= 0
\end{aligned}
$$

::::

<!-- Source PDF page 213; printed label 204. -->

(sec-9-6)=
## 9.6 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-9-1)=

::::{admonition} Practice Problem 9-1

A roller coaster has a frictionless track in the $xz-$plane as shown below. The roller coaster car starts at the top of the track at rest. When the car is released, at which position(s) will it be moving with a maximum speed?

:::{figure} ../images/figures/figure-9-9.png
:label: fig-9-9
:enumerator: 9.9
:alt: Figure shows the roller coaster represented as a graph with eight points labelled A to H to indicate different positions in the motion.
:width: 310px

The roller coaster car travels along the track starting at position $A$ and ending at position $H$.
:::

::::

(problem-9-2)=

::::{admonition} Practice Problem 9-2

A rock of mass $M$ is released from a height $h$ above the ground. What is the velocity of the rock when it has fallen half the distance? Neglect air resistance.

::::

(problem-9-3)=

::::{admonition} Practice Problem 9-3

A mass $m$ is attached to a spring with constant $k$ and set in simple harmonic motion with an amplitude $A$. Find the equations for potential and kinetic energy in terms of $m, k$, and $A$. Plot these forces and their sum as a function of time from $t$ = 0 to $t = T$ (the period of oscillations). For the plot, choose arbitrary values for $k, m$, and $A$.

::::

(problem-9-4)=

::::{admonition} Practice Problem 9-4

A particle of mass $m$ slides on a frictionless wire that is bent to form a loop. The wire has a loop of radius $R$ and the particle starts from rest at a point that is level with the midpoint of the loop as shown in the figure. What is the magnitude of the normal force on the particle when it reaches the bottom of the loop?

::::

<!-- Source PDF page 214; printed label 205. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-9-10.png
:label: fig-9-10
:enumerator: 9.10
:alt: Figure shows the mass located on the left-side of a round loop.
:width: 186px

The particle of mass $m$ travels on the loop of radius $R$.
:::

::::

(problem-9-5)=

::::{admonition} Practice Problem 9-5

A small mass $m$ forms a pendulum with an ideal rope of length $L$. The small mass is brought to an angle of $60^{\circ}$ from the vertical and released from rest to strike a block right beneath the vertical as shown in the figure below. What is the speed of the particle right before it strikes the block? (Assume that the rope remains taut over the entire motion).

:::{figure} ../images/figures/figure-9-11.png
:label: fig-9-11
:enumerator: 9.11
:alt: Figure shows a pendulum at its initial displacement before it is release to hit a stationary block.
:width: 155px

Mass striking a block
:::

::::

(problem-9-6)=

::::{admonition} Practice Problem 9-6

A particle of mass $m$ sits at the top of a frictionless dome of radius $R$. The particle starts at rest but at $t$ = 0, it begins to slide off the dome. What is the speed of the particle as a function of its vertical height, $y$?

:::{figure} ../images/figures/figure-9-12.png
:label: fig-9-12
:enumerator: 9.12
:alt: Figure shows a dome with the particle located at an angle theta from the top.
:width: 217px

Dome and particle.
:::

::::

<!-- Source PDF page 215; printed label 206. -->

(problem-9-7)=

::::{admonition} Practice Problem 9-7

A person with mass $M$ is jumping on a trampoline that has an effective spring constant of $k$. The trampoline has a height of $d$ above the ground.

a) What is the maximum height with respect to the ground that the person can reach while jumping on this trampoline?

b) How does the maximum height compare between an adult and a child jumping? Assume the child has half the mass of the adult. Does this make sense?

::::

(problem-9-8)=

::::{admonition} Practice Problem 9-8

A solid cylinder of mass $M$, radius $R$, and length $L$ is released from rest at the top of an incline of height $h$. It rolls without slipping to the bottom. What is the speed of the cylinder when it reaches the bottom?

::::

(problem-9-9)=

::::{admonition} Practice Problem 9-9

See the figure below. A solid cylinder of mass $M$ and radius $R$ is connected to a spring with spring constant $k$ at its centre of mass as shown in the figure. The cylinder has a moment of inertia of $\frac{1}{2} MR^{2}$ at its centre of mass and it can roll on the floor without slipping.

a) If the spring is displaced by $x$, what is the velocity of the cylinder centre of mass relative to $\dot{x}$ ?

b) What is the rotational angular speed of the cylinder?

c) What are the equations for rotational and translational kinetic energy? How do the rotational and translational kinetic energies compare?

d) If the cylinder is displaced a small amount from equilibrium it will oscillate. Use energy conservation to solve the differential equation of motion and find the period of oscillations.

:::{figure} ../images/figures/figure-9-13.png
:label: fig-9-13
:enumerator: 9.13
:alt: Figure shows the cylinder with a spring attached to it’s center.
:width: 217px

The cylinder and spring system.
:::

::::
