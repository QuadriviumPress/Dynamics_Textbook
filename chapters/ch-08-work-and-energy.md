(ch-8)=
# 8. Work and Energy

<!-- Source PDF page 173; printed label 164. -->

::::{admonition} Learning Objectives

- Define work and kinetic energy

- Review the work-energy theorem

- Introduce conservative forces and gravity

- Introduce potential energy

::::

In this chapter, we will switch to using energy to solve physical problems instead of Newton’s laws and momentum. We will review the concepts of work, kinetic energy, and potential energy, and we will introduce conservative forces.

(sec-8-1)=
## 8.1 Introduction to Work and Energy

When a force is applied to an object such that it moves a displacement of $\Delta \vec{r}$, work is done by that force. Work is defined as:

$$
W = \int \vec{F} \cdot \mathrm{d}\vec{r}
$$ (eq-8-1)

where $\vec{F}$ is the force and $\mathrm{d}\vec{r}$ represents a small displacement.

::::{admonition} Units of Work

Work has units of energy. The SI units for energy is the Joule, abbreviated as [J].

$$
[1 \mathrm{J}] = [1 \mathrm{N} \mathrm{m}] = [1 \mathrm{kg} \mathrm{m}^{2}\mathrm{s}^{-2}].
$$

::::

If the force is *constant*, then you can simplify the above equations to:

$$
W = \vec{F} \cdot \int \mathrm{d}\vec{r} = \vec{F} \cdot \Delta \vec{r} = F_{x}\Delta x + F_{y}\Delta y + F_{z}\Delta z
$$

where $\Delta \vec{r}$ represents the displacement between two points, $r_{1}$ and $r_{2}$. Alternatively, the vector dot product can be solved following $\vec{F} \cdot \Delta \vec{r} = F\Delta r\cos \theta$, where $\theta$ is the angle between the two vectors.

If $\vec{F}$ and $\mathrm{d}\vec{r}$ are parallel $(\theta$ = 0), then the force is acting in the same direction as the displacement and the force does maximum positive work. If the force is perpendicular to the displacement $(\theta = \frac{\pi}{2})$, then the force does zero work. That is, the force is not responsible for the displacement and contributed no work to that displacement. If the force

<!-- Source PDF page 174; printed label 165. -->

is antiparallel to the displacement $(\theta = \pi)$, then the force does maximum negative work (the force acts to counter the motion as much as it can).

::::{tip} Quick Question

1. Describe a situation where a force is at an angle of $0^{\circ},90^{\circ}$, and $180^{\circ}$ from a displacement. Consider how that force affects the motion.

::::

Work is a *scalar* quantity. It has magnitude but no direction. Since work is calculated by a vector dot product between force and displacement, only the component of the force that is along the displacement vector matters for the work calculation. Thus, solving problems with energy can make the math much easier if you select the right coordinate system (e.g., Cartesian versus polar coordinates) when defining your force and displacement.

::::{admonition} Describing Work

Since work is measured from one position $(r_{1})$ to a second position $(r_{2})$, we will use $W(r_{1}\rightarrow r_{2})$ to illustrate that the work is being done from $r_{1}$ to $r_{2}$. This form is convenient to specify the direction, because you can also measure the work from $r_{2}$ to $r_{1}$. For conservative forces ([Chapter 8.5](#sec-8-5)),

$$
W(r_{1}\rightarrow r_{2}) = -W(r_{2}\rightarrow r_{1})
$$ (eq-8-2)

The difference between these two cases is the direction of the displacement vector for $\mathrm{d}\vec{r}$. In one case, the force will be against the displacement (negative work), and in the other case, the force will be in the same direction as the displacement (positive work).

::::

(sec-8-2)=
## 8.2 Work-Energy Theorem

Consider a net 1-D force $F$ that acts on a single particle in the $x$ direction. From Newton’s second law (in one dimension), we have:

$$
F = m \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = m \frac{\mathrm{d}x}{\mathrm{d}t} \frac{\mathrm{d}v}{\mathrm{d}x} = mv \frac{\mathrm{d}v}{\mathrm{d}x}
$$

using the chain rule (see [Sample Problem 2-3](#example-2-3) for more information). We can re-write the above as:

$$
\begin{aligned}
F\mathrm{d}x &= mv\mathrm{d}v \\
F\mathrm{d}x &= \frac{1}{2} m\mathrm{d}(v^{2}) =\Rightarrow \mathrm{note} \mathrm{that} \mathrm{d}(v^{2}) = 2v\mathrm{d}v \\
F\mathrm{d}x &= \mathrm{d}\bigg(\frac{1}{2} mv^{2}\bigg) =\Rightarrow m \mathrm{is} \mathrm{constant} \\
F\mathrm{d}x &= \mathrm{d}K
\end{aligned}
$$

where $K$ corresponds to the kinetic energy of the system.

The work done by the force $F$ going from position $x_{1}$ to $x_{2}$ can be found by integrating both sides of the above equation:

<!-- Source PDF page 175; printed label 166. -->

$$
\begin{aligned}
\int_{x_{1}}^{x_{2}} F(x)\mathrm{d}x &= \int_{x_{1}}^{x_{2}} \mathrm{d}K \\
W_{2}- W_{1}&= K_{2}- K_{1}
\end{aligned}
$$

$$
W(x_{1}\rightarrow x_{2}) = \Delta K
$$ (eq-8-3)

Equation 8.3 is the *work-kinetic energy theorem*.

::::{admonition} Work-Kinetic Energy Theorem

The work done by all forces acting on a system corresponds to the change in kinetic energy of the system. That is, if positive work is done by the force (movement is with the force), then there is an increase in kinetic energy, and if there is negative work (movement is against the force), there is a decrease in kinetic energy.

::::

Similarly, one can also define the work-kinetic energy theorem for rotation and torques. Recall from [Chapter 7](#ch-7) that the net torque is:

$$
\tau = I\alpha = I \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} = I \frac{\mathrm{d}\theta}{\mathrm{d}t} \frac{\mathrm{d}\omega}{\mathrm{d}\theta} = I\omega \frac{\mathrm{d}\omega}{\mathrm{d}\theta}
$$

Now, torque is a vector quantity given by $\vec{\tau} = \vec{r} \times \vec{F}$ . But work is a scalar quantity and the work done on a particle to move it from one position to another applies only to the component of the force in the direction of motion. If a force is perpendicular to the direction of motion, that force does no work. And if a force is parallel to the direction of motion, it does maximum work.

So if the path length in the direction of the force is d$s = r$d$\theta$, then we can say that the work done by the force is:

d$W = F_{s}$d$s =\Rightarrow F_{s}$ is the component parallel to the path $s$

$$
= F_{s}r\mathrm{d}\theta =\Rightarrow \mathrm{sub} \mathrm{in} \mathrm{d}s = r\mathrm{d}\theta
$$

$$
= \tau \mathrm{d}\theta =\Rightarrow \tau = rF_{s}\mathrm{because} \vec{F}_{s}\perp \vec{r} \mathrm{if} \vec{F}_{s}// \mathrm{d}\vec{s} (\mathrm{e.g}., \vec{r} \perp \mathrm{d}\vec{s})
$$

Combining this with our definition of torque from before, we get:

$$
\begin{aligned}
\mathrm{d}W &= \tau \mathrm{d}\theta \\
&= \Bigg(I\omega \frac{\mathrm{d}\omega}{\mathrm{d}\theta} \Bigg)\mathrm{d}\theta =\Rightarrow \mathrm{equation} \mathrm{for} \tau \mathrm{from} \mathrm{the} \mathrm{second} \mathrm{law}
\end{aligned}
$$

$$
\begin{aligned}
&= I\omega \mathrm{d}\omega \\
&= \frac{1}{2} I\mathrm{d}(\omega ^{2}) =\Rightarrow \mathrm{note} \mathrm{that} \mathrm{d}(\omega ^{2}) = 2\omega \mathrm{d}\omega \\
&= \mathrm{d}\bigg(\frac{1}{2} I\omega ^{2}\bigg) =\Rightarrow I \mathrm{is} \mathrm{constant} \\
&= \mathrm{d}K
\end{aligned}
$$

<!-- Source PDF page 176; printed label 167. -->

Integrating both sides will give you the same answer as the linear case: $W(\theta _{1}\rightarrow \theta _{2}) = \Delta K$. So the work-kinetic energy theorem applies for both translation and rotation movement. The kinetic energy equations are slightly different, however.

$$
K = \frac{1}{2} mv^{2}=\Rightarrow \mathrm{for} \mathrm{translation}
$$ (eq-8-4)

$$
K = \frac{1}{2} I\omega ^{2}=\Rightarrow \mathrm{for} \mathrm{rotation}
$$ (eq-8-5)

(sec-8-3)=
## 8.3 Work in Different Frames

The work-kinetic energy theorem applies to all inertial frames (constant velocity) whether they are moving or stationary. So the change in work is the same within a stationary $(S)$ frame or in a moving frame $S^{\prime }$ (e.g., the centre-of-mass frame such as in [Chapter 6](#ch-6)).

[Figure 8.1](#fig-8-1) show a particle starting from rest and moving under a constant force $F$ in a laboratory. This particle will have a constant acceleration $a$ due to this force. The work done to move this particle from point $x_{1}$ to $x_{2}$ in the laboratory frame $(S)$ is simply $W_{S}= F\Delta x = \Delta K$ because all the motion is in 1-D.

:::{figure} ../images/figures/figure-8-1.png
:label: fig-8-1
:enumerator: 8.1
:alt: Figure compares the standard 2D Cartesian axes for a rest frame and a moving frame.
:width: 234px

The motion of a particle in two different inertial frames. The lab frame $S$ is stationary (red) and the second frame $S^{\prime }$ is moving at a constant velocity $u$ relative to the lab frame. A particle moves under a constant force $F$ with an acceleration $a$ in the lab frame. The work done to move that particle from points $x_{1}$ to $x_{2}$ in the lab frame is equal to the work done to move the particle in the moving inertial frame.
:::

Now, consider what an observer in a moving frame, $S^{\prime }$ would measure for the work done by that force. Here, $S^{\prime }$ is moving at a constant velocity and is also an inertial frame. Because $S^{\prime }$ is moving at a constant velocity, the observer in $S^{\prime }$ would find the same acceleration as the observer in $S$ (e.g., $\frac{\mathrm{d}}{\mathrm{d}t} (v + v_{0}) = \frac{\mathrm{d}v}{\mathrm{d}t}$ ). As a result, both the acceleration and force are unchanged in the moving frame. So

$$
F_{S}= F_{S^{\prime }}= ma
$$ (eq-8-6)

with the same value of $a$ for both frames.

If the force is constant (given in the question), then the work in the moving frame is $W_{S^{\prime }}= \vec{F}\Delta \vec{x}_{S^{\prime }}$, where $\Delta \vec{x}_{S^{\prime }}$ is the displacement in the moving frame. Note that since the motion still takes place in 1-D we can drop vectors (if there are more dimensions, you just need to break up the movement by each coordinate).

<!-- Source PDF page 177; printed label 168. -->

For the displacement, $\Delta \vec{x}_{S^{\prime }}$, we need to know how far the particle travels in time $\Delta t$. For a system with constant acceleration (see [Chapters 1](#ch-1) and 2), the displacement $\Delta x = \frac{1}{2} at^{2}+v_{i}t$, where $v_{i}$ is the initial velocity of the system. While the particle is initially at rest in the stationary frame, from the perspective of the moving frame, the particle does not start stationary. The moving frame has a velocity of $-u\hat{\imath}$ relative to the lab frame. That means that the moving frame would see the particle as having an initial speed of $u\hat{\imath}$. So we can say that $v_{i}= u$ and the displacement is:

$$
\Delta x = \frac{1}{2} at^{2}+ v_{i}t = \frac{1}{2} at^{2}+ ut
$$

Taking our equations for $F$ and $\Delta x$ in the moving frame, the work done by the force is

$$
\begin{aligned}
\Delta W &= F\Delta x \\
&=(ma)\left(\frac12at^2+ut\right)\\
&=\frac12m\left[(at)^2+2uat\right]\\
&=\frac12m\left[(at)^2+2uat+u^2-u^2\right]=\Rightarrow\mathrm{add}\ \mathrm{and}\ \mathrm{subtract}\ u^{2}\ (\mathrm{same}\ \mathrm{as}\ \mathrm{adding}\ \mathrm{zero})\\
&=\frac12m\left[(at+u)^2-u^2\right]=\Rightarrow\mathrm{recall}\ \mathrm{that}\ (a+b)^{2}=a^{2}+2ab+b^{2}\\
&=\frac12m\left[v_f^2-u^2\right]=\Rightarrow\mathrm{for}\ \mathrm{constant}\ \mathrm{acceleration},\ v_{f}=at+u\\
&=\frac12m\left[v_f^2-v_i^2\right]=\Rightarrow u\ \mathrm{is}\ \mathrm{just}\ \mathrm{the}\ \mathrm{initial}\ \mathrm{velocity},\ v_{i}\\
&=K_f-K_i\\
&=\Delta K
\end{aligned}
$$

where $K_{f}$ is the final kinetic energy and $K_{i}$ in the initial kinetic energy.

So while the values of $W$ and $K$ as measured in the two frames (stationary and moving) may be different, the requirement that $\Delta W = \Delta K$ holds in both frames. Again, this is only the case for *inertial* frames. In non-inertial frames (e.g., rotating or accelerating frames), the net force will include fictitious forces due to the non-inertial frame and the measured accelerations would be different (see [Chapters 4](#ch-4) and 5).

(sec-8-4)=
## 8.4 Gravity

(sec-8-4-1)=
### 8.4.1 Simple Approximation

Near the Earth’s surface, we often describe the gravitational force as $\vec{F}_{g}= m\vec{g}$, where $\vec{g}$ is a constant vector that points down vertically and has a constant magnitude.

Consider the case where the position of a heavy box of mass $m$ changes $y_{1}$ to $y_{2}$ in vertical height and that both positions $y_{2}$ and $y_{1}$ are near the Earth’s surface. Work is done by gravity as the box moves by this displacement. The vector describing the displacement of

<!-- Source PDF page 178; printed label 169. -->

the box is $\Delta \vec{y} = (y_{2}-y_{1})\hat{\jmath}$ , whereas the gravitational force is $\vec{F}_{g}= -mg\hat{\jmath}$ , which is constant. Taking the equation for work with a constant force, the work is:

$$
\Delta W = \vec{F}_{g}\cdot \Delta \vec{y}
$$

$$
= (-mg\hat{\jmath}) \cdot (y_{2}- y_{1})\hat{\jmath}
$$

$$
= -mg(y_{2}- y_{1}) =\Rightarrow \hat{\jmath} \cdot \hat{\jmath} = 1
$$

Remember, this is the work done by gravity. So if a box is lifted upward $(y_{2}> y_{1})$, gravity acts against the displacement and $W < 0$. If the box is lowered $(y_{2}< y_{1})$, gravity acts with (helps) the displacement and $W > 0$. And if $y_{2}= y_{1}$ then $W$ = 0 (no work is done by gravity).

(sec-8-4-2)=
### 8.4.2 General Equation

In general, the true form of the gravitational force is:

$$
\vec{F}_{g}= - \frac{GMm}{r^{2}} \hat{r}
$$ (eq-8-7)

where $G$ is the gravitational constant of $6.67 \times 10^{-11}$ N $\mathrm{m}^{2}\mathrm{kg}^{-2}, M$ is the mass of the object producing the gravitational field, $m$ is the mass of an object being accelerated in the gravitational field, and $r$ is the distance between the centers of the two objects. Thus, the true form for the acceleration due to gravity is given by:

$$
\vec{g} = - \frac{GM}{r^{2}} \hat{r}
$$ (eq-8-8)

Note that the acceleration due to gravity always points toward the centre of the source of the gravitational field (points radially inward).

::::{tip} Quick Question

1. Show that the acceleration due to gravity near the surface of the Earth is roughly 9.8 m $\mathrm{s}^{-2}$. The radius of the Earth is $\approx 6370$ km and the mass of the Earth is

$$
M \approx 5.97 \times 10^{24}\mathrm{kg}.
$$

::::

The force of gravity is a radial force with no azimuthal (angle) dependence. That means that any point that has the same radial distance $(|\vec{r}|)$ will have the same magnitude of gravity $|\vec{g}|$. We often describe gravity as a gravitational field, a sphere of influence where any object with a mass $m$ will be subjected to a gravitational force. The magnitude of the gravitational field changes as a function of radial distance. For example, [Figure 8.2](#fig-8-2) shows a cartoon of the Earth with two different vectors, $\vec{r}_{1}$ and $\vec{r}_{2}$. Their magnitudes of gravitational acceleration are:

$$
|\vec{g}_{1}| = \frac{GM}{r_{1}^{2}} \mathrm{and} |\vec{g}_{2}| = \frac{GM}{r_{2}^{2}}
$$

<!-- Source PDF page 179; printed label 170. -->

:::{figure} ../images/figures/figure-8-2.png
:label: fig-8-2
:enumerator: 8.2
:alt: Figure shows two different radial orbits around the Earth.
:width: 234px

A cartoon of the Earth with two different vectors, $\vec{r}_{1}$ and $\vec{r}_{2}$. Each vector also has a circle with corresponding radii of $r_{1}$ and $r_{2}$. Every point on the $r_{1}$ circle will have the same gravitational field magnitude and similarly, every point on the $r_{2}$ circle will have the same gravitational field magnitude.
:::

Since $r_{2}> r_{1}, |\vec{g}_{1}| > |\vec{g}_{2}|$. But any point on a sphere with radius $r_{1}$ around the Earth will have the same magnitude of acceleration due to gravity (e.g., the circles in [Figure 8.2](#fig-8-2)), and likewise for all the points on a sphere with radius $r_{2}$. You can think of gravity as a sphere of influence, where any point that has the same distance from the centre of the Earth has the same magnitude of $|\vec{g}|$.

Note that the direction of gravity will be different depending on where you are, because the force always points inward toward the centre of the Earth (in its true form, gravity is not vertical, but radial). For very small distances and positions near the Earth’s surface, you can still assume a vertical direction and constant magnitude for a frame at that surface.

*What is the work done by gravity using this general equation?*

Well, consider going from $r_{1}$ to $r_{2}$ as shown in [Figure 8.2](#fig-8-2).

$$
\begin{aligned}
W(r_{1}\rightarrow r_{2}) &= \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} =\Rightarrow \mathrm{force} \mathrm{is} \mathrm{not} \mathrm{constant} \\
&= \int_{r_{1}}^{r_{2}} \bigg(- \frac{GMm}{r^{2}} \bigg)\hat{r} \cdot \mathrm{d}\vec{r} =\Rightarrow \mathrm{use} \mathrm{the} \mathrm{equation} \mathrm{for} \mathrm{the} \mathrm{force} \mathrm{of} \mathrm{gravity} \\
&= -GMm\int_{r_{1}}^{r_{2}} \bigg(\frac{1}{r^{2}} \hat{r}\bigg) \cdot (\mathrm{d}r\hat{r}) =\Rightarrow \mathrm{d}\vec{r} = \mathrm{d}r\hat{r} \\
&= -GMm\int_{r_{1}}^{r_{2}} \bigg(\frac{1}{r^{2}} \mathrm{d}r\bigg)\hat{r} \cdot \hat{r} =\Rightarrow \hat{a} \cdot \hat{a} = 1 \mathrm{for} \mathrm{any} \mathrm{unit} \mathrm{vector} \\
&= -GMm\int_{r_{1}}^{r_{2}} \frac{1}{r^{2}} \mathrm{d}r \\
&= -GMm\bigg(- \frac{1}{r} \bigg|_{r_{1}}^{r_{2}} \bigg) \\
&= \frac{GMm}{r_{2}} - \frac{GMm}{r_{1}}
\end{aligned}
$$

Note that if $r_{2}> r_{1}, W < 0$ as we would expect (e.g., you are doing work against gravity to move an object further away). You may recognize $- \frac{GMm}{r}$ as the gravitational potential energy. We will discuss potential energies in more detail in [Section 8.6](#sec-8-6).

<!-- Source PDF page 180; printed label 171. -->

(sec-8-4-3)=
### 8.4.3 Escape velocity

The gravitational force follows an inverse square ( $\frac{1}{r^{2}})$ law. So at very large distances from the source of the gravitational field, the gravitational force goes to zero and the work necessary to move a particle also goes to zero (if there is no force, there is no work).

Consider an object that is on the surface of Earth and is launched so that it reaches a very large distance away (assume infinity). Due to Earth’s gravitational field, the object will feel a force that opposes its motion to leave. Gravity will be doing negative work and the kinetic energy of the object will decrease. **What speed is needed for this object to** **just reach infinity?** Assume Earth’s atmosphere does not affect its motion.

To solve this problem, we will use the work-kinetic energy theorem (Equation (8.3)).

$$
W(r_{1}\rightarrow r_{2}) = \Delta K = \frac{1}{2} mv_{2}^{2}- \frac{1}{2} mv_{1}^{2}
$$

We just solved for the work to move an object between two radii in a gravitational field. We start with Earth’s surface $(r_{1}= R_{E})$ and we end very far away $(r_{2}= \infty)$. That means that:

$$
W(r_{1}\rightarrow r_{2}) = \frac{GMm}{r_{2}} - \frac{GMm}{r_{1}} = 0 - \frac{GmM_{E}}{R_{E}}
$$

where $R_{E}$ is the radius of the Earth, $M_{E}$ is the mass of the Earth, and $m$ is the mass of our object being moved. For kinetic energy, $v_{2}$ = 0 because the object just reaches infinity. As such:

$$
\begin{aligned}
W(r_{1}\rightarrow r_{2}) &= \frac{1}{2} mv_{2}^{2}- \frac{1}{2} mv_{1}^{2} \\
- \frac{GmM_{E}}{R_{E}} &= 0 - \frac{1}{2} mv_{1}^{2} \\
v_{1}^{2}&= \frac{2GM_{E}}{R_{E}}
\end{aligned}
$$

(eq-8-9)=
$$
v_{esc}=\sqrt{\frac{2GM_E}{R_E}}.
$$

[Equation 8.9](#eq-8-9) describes the *escape velocity* and for Earth, which is roughly 11 km $\mathrm{s}^{-1}$. The escape velocity is the minimum speed for rockets and satellites to leave Earth’s surface and travel great distances away.

::::{tip} Quick Question

1. Verify that $v_{esc}$ = 11 km $\mathrm{s}^{-1}$ is the escape velocity for the Earth. Assume that $R_{E}\approx 6370$ km and $M_{E}\approx 5.97 \times 10^{24}$ kg.

::::

Note that an object starting from rest at a great distance from the Earth will hit the Earth at a speed equivalent to the escape velocity. This converse situation is true because gravity is a *conservative force*, which we will discuss in the next section.

<!-- Source PDF page 181; printed label 172. -->

(sec-8-5)=
## 8.5 Conservative Forces

Conservative forces are a class of forces that depend only on position. These forces are also ones where *energy is conserved*. Common examples of conservative forces are gravity, the spring force, and the electric force. Conservative forces must meet the following criteria:

1. A conservative force does no total work on an object during a round trip.

2. The work done by a conservative force is independent of the path taken between two points.

The first requirement states:

$$
W(r_{1}\rightarrow r_{1}) = \oint \vec{F} \cdot \mathrm{d}\vec{r} = 0
$$ (eq-8-10)

where $\oint$ indicates an integral over a closed loop. For example, if you measure the work between $r_{1}\rightarrow r_{2}$ and then $r_{2}\rightarrow r_{1}$, the work function would be:

$$
W(r_{1}\rightarrow r_{2}\rightarrow r_{1}) = \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} + \int_{r_{2}}^{r_{1}} \vec{F} \cdot \mathrm{d}\vec{r}
$$

For a conservative force, that equation would equal zero.

::::{admonition} Cora’s Thoughts

Let’s show how it equals zero by connecting to what we saw in [Chapter 8.1](#sec-8-1). We can say that:

$$
W(r_{1}\rightarrow r_{2}\rightarrow r_{1}) = W(r_{1}\rightarrow r_{2}) + W(r_{2}\rightarrow r_{1}) = \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} + \int_{r_{2}}^{r_{1}} \vec{F} \cdot \mathrm{d}\vec{r}
$$

So if we substitute in Equation (8.2), which is true for conservative forces, we get:

$$
W(r_{1}\rightarrow r_{2}) + W(r_{2}\rightarrow r_{1}) = \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} - \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r}
$$

$$
W(r_{1}\rightarrow r_{2}\rightarrow r_{1}) = 0
$$

$$
W = 0
$$

Showing that the force does no total work on a round trip.

::::

Now consider the case of gravity,

$$
\begin{aligned}
\int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} &= \frac{GMm}{r_{2}} - \frac{GMm}{r_{1}} \\
\int_{r_{2}}^{r_{1}}\vec{F} \cdot \mathrm{d}\vec{r} &= \frac{GMm}{r_{1}} - \frac{GMm}{r_{2}}
\end{aligned}
$$

If you add those two segments, you indeed get $W$ = 0. This is true for any number of stops in the closed loop. As long as your starting and final positions are the same, you will get $W$ = 0 for a conservative force.

<!-- Source PDF page 182; printed label 173. -->

::::{tip} Quick Question

1. Verify that the electric force and the spring force also satisfy criterion 1 and give you the condition that $W$ = 0 for a closed loop.

::::

The second requirement states that the total work done to move an object between two points only depends on the initial and final positions. How you get from point one to point two doesn’t matter. [Figure 8.3](#fig-8-3) shows two paths that connect points $r_{1}$ and $r_{2}$. The work done by a conservative force will be the same no matter the path chosen.

:::{figure} ../images/figures/figure-8-3.png
:label: fig-8-3
:enumerator: 8.3
:alt: Figure shows two paths between the same two points, one linear and one wandering.
:width: 232px

Comparison of two paths between points $r_{1}$ and $r_{2}$. For a conservative force, the work done to go from $r_{1}$ to $r_{2}$ is the same for both paths, even though the paths are very different.
:::

And of course, if you go from $r_{1}$ to $r_{2}$ and then from $r_{2}$ back to $r_{1}$, the total work is zero (first criterion) no matter which path you take in either case (e.g., Path I from $r_{1}$ to $r_{2}$ and then Path II from $r_{2}$ back to $r_{1})$.

Note that forces like friction are *not* conservative forces. First, friction doesn’t depend on position. Second, friction removes energy from a system. Third, the work done by friction in a closed loop is not zero. For example, consider a hockey puck moving in a circle of radius $R$ on a rough horizontal surface that has friction. The friction force on the hockey puck is $\vec{f} = \mu _{K}mg\hat{\theta}$ , and the puck moves so that it is always antiparallel $(180^{\circ})$ to the displacement. So $W_{f}= -f\Delta d = -\mu _{K}mg(2\pi R)$ for a closed loop. Thus, $W_{f}\not =$ 0.

(sec-8-5-1)=
### 8.5.1 Identifying Conservative Forces

A conservative force can be identified mathematically using the following condition:

$$
\vec{\nabla} \times \vec{F} = 0
$$ (eq-8-11)

Note that $\vec{\nabla} \times \vec{F}$ is a vector cross product called the curl of the vector $\vec{F}$ . The $\vec{\nabla}$ symbol is a vector differential operator sometimes called the del or nabla operator. In Cartesian coordinates, it has the form of:

$$
\vec{\nabla} = \frac{\partial}{\partial x} \hat{\imath} + \frac{\partial}{\partial y} \hat{\jmath} + \frac{\partial}{\partial z} \hat{k}
$$

where $\partial$ indicates the partial derivative. For partial derivatives, you ignore any other variable. For example, $\frac{\partial}{\partial x} f(y)$ = 0 because $x$ is not present in the function (you treat $y$ as a constant for a partial derivative with respect to $x)$. For $\vec{\nabla}$ in other coordinate systems, see [Appendix A.5](#sec-A-5).

<!-- Source PDF page 183; printed label 174. -->

The curl of $\vec{A}$ (in Cartesian coordinates) is then given by the following matrix.

$$
\begin{aligned}
\vec{\nabla} \times \vec{A} &= \begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
A_{x} & A_{y} & A_{z}
\end{vmatrix} \\
&= \Bigg(\frac{\partial}{\partial y} A_{z}- \frac{\partial}{\partial z} A_{y}\Bigg)\hat{\imath} + \Bigg(\frac{\partial}{\partial z} A_{x}- \frac{\partial}{\partial x} A_{z}\Bigg)\hat{\jmath} + \Bigg(\frac{\partial}{\partial x} A_{y}- \frac{\partial}{\partial y} A_{x}\Bigg)\hat{k}
\end{aligned}
$$

A conservative force has $\vec{\nabla} \times \vec{F}$ = 0 by definition. We will discuss why in [Chapter 8.6](#sec-8-6).

(sec-8-5-2)=
### 8.5.2 Example Conservative Forces

(example-8-1)=

::::{admonition} Sample Problem 8-1

**Show that the gravitational force is a conservative force.**

**Solution**

The gravitational force is:

$$
\vec{F}_{g}= - \frac{GMm}{r^{2}} \hat{r}
$$

Since this is a radial force, use the spherical coordinates for the curl. You can use Cartesian, but there is a lot more math involved. See [Appendix A.5](#sec-A-5) for the definition of curl in spherical coordinates.

$$
\begin{aligned}
\vec{\nabla} \times \vec{F}_{g}&= \frac{1}{r^{2}\sin \theta}
\begin{vmatrix}
\hat{r} & r\hat{\theta} & r\sin \theta \hat{\varphi} \\
\frac{\partial}{\partial r} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial \varphi} \\
-\frac{GMm}{r^{2}} & 0 & 0
\end{vmatrix}
\end{aligned}
$$

$$
= \frac{1}{r^{2}\sin \theta} \Bigg[\frac{\partial}{\partial r} (0)\hat{r} + \frac{\partial}{\partial \varphi} \bigg(- \frac{GMm}{r^{2}} \bigg)r\hat{\theta} + \frac{\partial}{\partial \theta} \bigg(- \frac{GMm}{r^{2}} \bigg)r\sin \theta \hat{\varphi}\Bigg]
$$

$$
= 0
$$

because there is no $\theta$ or $\varphi$ dependence on the force. That is, $\frac{\partial}{\partial \theta} f(r) = \frac{\partial}{\partial \varphi} f(r)$ = 0 because you would treat $r$ as a constant for a partial derivative with respect to $\theta$ or $\varphi$. Since we have $\vec{\nabla} \times \vec{F}$ = 0, the gravitational force is conservative.

::::

<!-- Source PDF page 184; printed label 175. -->

::::{tip} Quick Question

1. Verify that $\vec{\nabla} \times \vec{F}$ = 0 also for the 1-D spring force, $F = -kx$.

::::

(example-8-2)=

::::{admonition} Sample Problem 8-2

**Is the force** $\vec{F} = x^{2}yz\hat{\imath} - xyz^{2}\hat{k}$ **conservative?**

**Solution**

Here we have some unnamed force that depends on position. To find out if this force is conservative, we have to solve $\vec{\nabla} \times \vec{F}$ . Note that the force is in Cartesian coordinates, so we will want to use the curl in Cartesian coordinates.

$$
\begin{aligned}
\vec{\nabla} \times \vec{F} &= | \frac{\partial \hat{\imath}}{\partial x} \frac{\partial \hat{\jmath}}{\partial y} \frac{\partial \hat{k}}{\partial z} | \\
x^{2}yz 0 -xyz^{2} \\
&= \Bigg(\frac{\partial}{\partial y} [-xyz^{2}] - 0\Bigg)\hat{\imath} + \Bigg(\frac{\partial}{\partial z} [x^{2}yz] - \frac{\partial}{\partial x} [-xyz^{2}]\Bigg)\hat{\jmath} + \Bigg(0 - \frac{\partial}{\partial y} [x^{2}yz]\Bigg)\hat{k}
\end{aligned}
$$

$$
= (-xz^{2})\hat{\imath} + (x^{2}y + yz^{2})\hat{\jmath} + (-x^{2}z)\hat{k}
$$

Since $\vec{\nabla} \times \vec{F} \not =$ 0, this force is not a conservative force.

::::

(sec-8-6)=
## 8.6 Potential Energy

The potential energy represents the energy of a system based on its position or configuration. It represents the capacity of the system to do work,

$$
\Delta U = -\Delta W_{con}
$$

where $\Delta W_{con}$ is the work done by a conservative force. More formally,

$$
U(r_{1}\rightarrow r_{2}) = -\int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} = -W_{con}(r_{1}\rightarrow r_{2})
$$ (eq-8-12)

Potential energy is associated with conservative forces only. Consider a heavy box. If you lift that box upward, the work done by gravity is negative (gravity opposes the motion), but you increase the potential energy of the box because work is being done against gravity $(W < 0)$. If you lower that box or let go, then gravity is doing positive work on the box $(W > 0)$ and it will have a decrease in potential energy.

Let’s look at the gravitational potential energy between positions $r_{1}$ and $r_{2}$.

<!-- Source PDF page 185; printed label 176. -->

$$
\begin{aligned}
U(r_1\to r_2)
&=-W_{con}(r_1\to r_2)\\
&=-\int_{r_1}^{r_2}\vec{F}\cdot\mathrm{d}\vec{r}\\
&=-\int_{r_1}^{r_2}\left(-\frac{GMm}{r^2}\hat{r}\right)\cdot(\mathrm{d}r\,\hat{r})\\
&=\int_{r_1}^{r_2}\frac{GMm}{r^2}\,\mathrm{d}r\\
&=\left.-\frac{GMm}{r}\right|_{r_1}^{r_2}
=-\frac{GMm}{r_2}+\frac{GMm}{r_1}.
\end{aligned}
$$

In general, the gravitational potential energy is measured between two points. It is a *relative* energy. You will want to set a convenient reference point. For example, we can set $r_{1}= \infty$, where there would be no contribution from the force, such that:

$$
U = - \frac{GMm}{r} (\mathrm{compared} \mathrm{to} \mathrm{infinity})
$$

For gravity problems near Earth’s surface, setting $U$ = 0 at the surface is often convenient.

The potential energy for the spring force going from $x_{1}$ to $x_{2}$ is:

$$
U(x_{1}\rightarrow x_{2}) = -\int_{x_{1}}^{x_{2}} (-kx\hat{x}) \cdot (\mathrm{d}x\hat{x}) = \int_{x_{1}}^{x_{2}} kx\mathrm{d}x = \frac{1}{2} kx^{2}\Big|_{x_{1}}^{x_{2}} = \frac{1}{2} kx_{2}^{2}- \frac{1}{2} kx_{1}^{2}
$$

Once again, we want to set a convenient initial value like $x_{1}$ = 0 (the equilibrium position), so that the potential energy of a spring is simply $U = \frac{1}{2} kx^{2}$ relative to that point.

::::{tip} Quick Questions

1. Show that that the potential energy of a pendulum can be written as $U = \frac{1}{2} mgh\theta ^{2}$ for small angles of $\theta$ and setting $\theta _{1}$ = 0.

2. Show that the potential energy of the electric force $F_{e}= \frac{kQq}{r^{2}} \hat{r}$ is given by $U = \frac{kQq}{r}$, where $k$ is the electric constant, $Q$ is the electric charge of the central object forming the electric field, and $q$ is the charge of the test particle in the field.

::::

(sec-8-7)=
## 8.7 Conservation of Energy

The work-kinetic energy theorem states that $\Delta W = \Delta K$. That is, the total work on a system by a force is equal to the change in the kinetic energy. The total work is the sum of work by conservative forces $(\Delta W_{con})$ and the work by non-conservative forces $(\Delta W_{nc})$:

$$
\Delta W = \Delta K
$$

$$
\Delta W_{con}+ \Delta W_{nc}= \Delta K =\Rightarrow \Delta W = \Delta W_{con}+ \Delta W_{nc}
$$

$$
\Delta W_{nc}= \Delta K - \Delta W_{con}
$$

$$
\Delta W_{nc}= \Delta K + \Delta U =\Rightarrow \Delta W_{con}= -\Delta U
$$

<!-- Source PDF page 186; printed label 177. -->

Setting $\Delta W_{nc}= \Delta E$, or the change in mechanical energy (non-conservative work), we get:

$$
\Delta E = \Delta (K + U)
$$ (eq-8-13)

For small times d$t$, you can say that d$E = \mathrm{d}(K+U)$. Integrating these functions then gives

$$
E = K + U.
$$

In the absence of non-conservative forces (e.g., if all forces acting on a system are conservative), then $\Delta W_{nc}$ = 0 and $\Delta E$ = 0 such that we get $\Delta (K + U)$ = 0 or $K + U$ = constant. This is the *conservation of energy*. When energy is conserved, $\Delta K = -\Delta U$ or the change in kinetic energy directly corresponds to a change in potential energy. If kinetic energy increases, then potential energy decreases and vice versa.

::::{admonition} Real World Applications

Hydroelectric power generation works by converting gravitational potential energy to kinetic energy and ultimately electrical energy. The basic principle behind hydroelectric power is a large volume of water experiencing a drop in elevation. Water flows from the intake downward to a turbine, gaining kinetic energy which can be captured by the turbine. The larger the elevation change, the more power that can potentially be generated. Hydroelectric installations often involve huge dams and are some of the largest construction projects on Earth.

:::{figure} ../images/figures/figure-8-4.png
:label: fig-8-4
:enumerator: 8.4
:alt: Figure shows how water flowing downward under gravity through a turbine generates electricity in a hydroelectric dam.
:width: 310px

Cartoon of a hydroelectric dam. Image credit: Tennessee Valley Authority.
:::

::::

(sec-8-8)=
## 8.8 Application of Potential Energy

A conservative force can also be written in terms of the potential energy,

$$
\vec{F} = -\vec{\nabla}U = -\Bigg(\frac{\partial U}{\partial x} \hat{\imath} + \frac{\partial U}{\partial y} \hat{\jmath} + \frac{\partial U}{\partial z} \hat{k}\Bigg)
$$ (eq-8-14)

for Cartesian coordinates (see [Appendix A.5](#sec-A-5) for other coordinate systems). The $\vec{\nabla}$ operator in this context means the gradient of $U$.

<!-- Source PDF page 187; printed label 178. -->

We can use this definition of a conservative force to show that $U(r_{1}\rightarrow r_{2}) = -W(r_{1}\rightarrow r_{2})$.

$$
\begin{aligned}
W(r_{1}\rightarrow r_{2}) &= \int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} \\
&= \int_{r_{1}}^{r_{2}}(-\vec{\nabla}U) \cdot \mathrm{d}\vec{r} =\Rightarrow \mathrm{substitute} \mathrm{in} \mathrm{our} \mathrm{scalar} \mathrm{field} \\
&= -\int_{r_{1}}^{r_{2}} \mathrm{d}U_{r}=\Rightarrow \mathrm{only} \mathrm{the} \mathrm{component} \mathrm{along} \mathrm{the} \mathrm{path} \mathrm{is} \mathrm{non-zero} \\
&= -\Big(U_{r}\Big|_{r_{1}}^{r_{2}}\Big) =\Rightarrow \mathrm{only} \mathrm{the} \mathrm{end} \mathrm{points} \mathrm{matter} \mathrm{for} \mathrm{conservative} \mathrm{forces} \\
&= -U(r_{1}\rightarrow r_{2})
\end{aligned}
$$

Exactly as we expect. Thus, the potential energy of a conservative force satisfies $\vec{F} = -\vec{\nabla}U$.

Moreover, $\vec{\nabla} \times \vec{F}$ = 0 for a conservative force. We can substitute in $\vec{F} = -\vec{\nabla}U$,

$$
\vec{\nabla} \times (-\vec{\nabla}U) = \begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
\frac{\partial U}{\partial x} & \frac{\partial U}{\partial y} & \frac{\partial U}{\partial z}
\end{vmatrix}
$$

$$
= -\Bigg(\frac{\partial}{\partial y} \frac{\partial U}{\partial z} - \frac{\partial}{\partial z} \frac{\partial U}{\partial y} \Bigg)\hat{\imath} - \Bigg(\frac{\partial}{\partial z} \frac{\partial U}{\partial x} - \frac{\partial}{\partial x} \frac{\partial U}{\partial z} \Bigg)\hat{\jmath} - \Bigg(\frac{\partial}{\partial x} \frac{\partial U}{\partial y} - \frac{\partial}{\partial y} \frac{\partial U}{\partial x} \Bigg)\hat{k}
$$

$$
= -\Bigg(\frac{\partial ^{2}U}{\partial y\partial z} - \frac{\partial ^{2}U}{\partial z\partial y} \Bigg)\hat{\imath} - \Bigg(\frac{\partial ^{2}U}{\partial z\partial x} - \frac{\partial ^{2}U}{\partial x\partial z} \Bigg)\hat{\jmath} - \Bigg(\frac{\partial ^{2}U}{\partial x\partial y} - \frac{\partial ^{2}U}{\partial y\partial x} \Bigg)\hat{k}
$$

$$
= 0\hat{\imath} + 0\hat{\jmath} + 0\hat{k} = 0
$$

Note for the above we are assuming that $U$ is twice continuously differentiable. If $U$ can be differentiated twice, then its partial derivatives are independent of the order and all terms cancel (e.g, $\frac{\partial ^{2}U}{\partial y\partial z} = \frac{\partial ^{2}U}{\partial z\partial y})$.

(example-8-3)=

::::{admonition} Sample Problem 8-3

A potential energy has the function of $U(r) = U_{0}- \frac{1}{2} A\sigma ^{2}e^{-r^{2}/\sigma ^{2}}$, where $U_{0}, A$, and $\sigma$ are all constants. **What is the force for this potential?**

**Solution**

Since the potential energy has a radial component only, we only need the radial com-

::::

<!-- Source PDF page 188; printed label 179. -->

::::{admonition} Continued

ponent of the gradient $(\vec{F} = -\vec{\nabla}U)$ to find the force.

$$
\vec{F} = -\vec{\nabla}U = - \frac{\partial U(r)}{\partial r} \hat{r} = -\bigg(\frac{1}{2} A\sigma ^{2}\bigg)(- \frac{2r}{\sigma ^{2}} e^{-r^{2}/\sigma ^{2}})\hat{r} = -rAe^{-r^{2}/\sigma ^{2}}\hat{r}
$$

::::

For a potential, $U$, there can be points where $-\vec{\nabla}U = \vec{F}$ = 0. Mathematically, these points are located where the derivative of the potential is zero and correspond to points of local maxima or local minima. [Figure 8.5](#fig-8-5)) shows a sketch of a potential with a local maximum and local minimum. These locations are also known as *equilibrium points* or saddle points.

:::{figure} ../images/figures/figure-8-5.png
:label: fig-8-5
:enumerator: 8.5
:alt: Figure shows a simple graph of a cubic-shaped function with local maximum and minimum points labeled to demonstrate equilibrium points.
:width: 260px

Example potential with a local maximum and local minimum.
:::

A local minimum is a *stable* equilibrium point. At the minimum, if a particle is slightly perturbed, it wouldn’t really go anywhere. The particle will feel a force that just brings it back to the minimum saddle point. Recall that the force is the negative derivative of the potential, so if you perturb the particle to a lower $x$ value, the potential has a negative slope and the force will be positive back toward the saddle point. And if you perturb the particle to a higher $x$ value, the potential has a positive slope and the force will be negative back toward the saddle point. So for a small shift in position, your particle more or less stays at the saddle point.

At the local maximum saddle point, however, a slight perturbation will have a huge effect on the particle’s motion. If you slightly perturb the particle to a lower $x$ value, the potential has a positive slope so the force will be negative toward even more negative $x$ values. (Similar case if you perturb the particle to a higher $x$ value). So a slight perturbation at the maximum of a potential will cause the system to be unstable and move away from that position.

::::{tip} Quick Questions

1. Do the math for this problem and show yourself that the minimum is an equilibrium saddle point where the force will always point back to the minimum and the maximum is an unstable saddle point where the force will always point away from the maximum.

::::

::::{admonition} Cora’s Thoughts

When looking at potential graphs it can

:::{figure} ../images/figures/figure-8-6.png
:label: fig-8-6
:enumerator: 8.6
:alt: Figure shows a ball at a local maximum (peak) and a ball at a local minimum (valley).
:width: 304px

A ball rolling on the same potential graph from [Figure 8.5](#fig-8-5).
:::

be useful to consider the functions as hills for a ball to roll on. At the exact max of the function, the ball will not roll, however, with a small perturbation, it will roll making it an unstable position. At the minimum, the ball will also be stationary, but with a small perturbation, it will not roll much. The valley that the ball is in keeps it in a stable position.

::::

<!-- Source PDF page 189; printed label 180. -->

(example-8-4)=

::::{admonition} Sample Problem 8-4

A particle is moving in one dimension under the influence of the potential $U(x)$ = $2x^{3}-3x^{2}-12x+30$, where all values are in SI units. **Find the equilibrium point(s)** **of this potential. Which point(s) are stable?**

**Solution**

[Figure 8.5](#fig-8-5) shows a sketch of this potential (a cubic function). So we should expect two equilibrium points, one maximum and one minimum. Since equilibrium points are where $\vec{F}$ = 0, we can set the derivative of the potential to zero to find their location.

$$
0 = \frac{\partial U(x)}{\partial x} = 6x^{2}- 6x - 12 = x^{2}- x - 2
$$

which is a quadratic equation with the solutions $x = -1$ m and $x$ = 2 m.

Although there are two equilibrium points, only one of these is a *stable* equilibrium solution.

Visually, we can see from the figure of the potential, that our minimum saddle point is at $x$ = 2 m. But if we wanted to calculate the saddle point without plotting, the true equilibrium position is when the second derivative of the potential is positive. The second derivative of our potential is:

$$
\frac{\partial ^{2}U(x)}{\partial x^{2}} = \frac{\partial}{\partial x} (6x^{2}- 6x - 12) = 12x - 6
$$

At $x = -1$ m, $U^{\prime \prime }< 0$ and at $x$ = 2 m, $U^{\prime \prime }> 0$. So the stable point is at $x$ = 2 m.

::::

<!-- Source PDF page 190; printed label 181. -->

::::{admonition} Real World Applications

Lagrange points are saddle points that correspond to maxima or minima in gravitational potential between the planets and the Sun. These are special points where gravity from the Sun and planet and the centrifugal force balance. For example, Jupiter has a collection of “moons” called Trojan asteroids that located in two clusters within Jupiter’s orbit at the Lagrange Points L4 and L5, which are potential minima. These asteroids are effectively trapped by a local potential minimum saddle point and they orbit [the](http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/trojan.html) Sun (not Jupiter) in lock-step with Jupiter. For more information, see the [hyperphysics webpage](http://hyperphysics.phy-astr.gsu.edu/hbase/Solar/trojan.html) for Trojan satellites and [NASA’s webpage](https://solarsystem.nasa.gov/resources/754/what-is-a-lagrange-point/) on Lagrange points.

::::

(example-8-5)=

::::{admonition} Sample Problem 8-5

A particle of mass $m$ moves in a potential given by the following equation: $U$ = $k(\frac{1}{3} x^{2}+4y^{2})$. **What is the equation for acceleration for the particle in both** $x$ **and** $y$ **coordinates?**

**Solution**

To solve for the acceleration, we need to start by finding the force, since Newton’s second law states that $\sum F = ma$, assuming the particle mass is constant.

The force is given by the gradient of the potential, Equation (8.14). Since our potential has Cartesian coordinates, we’ll use Cartesian coordinates for the gradient.

$$
F_{x}= - \frac{\partial U}{\partial x} = - \frac{2}{3} kx
$$

$$
F_{y}= - \frac{\partial U}{\partial y} = -8ky
$$

Using Newton’s Second Law:

$$
F_{x}= m\ddot{x} = - \frac{2}{3} kx
$$

$$
F_{y}= m\ddot{y} = -8ky
$$

So we have:

$$
\ddot{x} = - \frac{2}{3m} kx
$$

$$
\ddot{y} = - \frac{8}{m} ky
$$

::::

<!-- Source PDF page 191; printed label 182. -->

::::{admonition} Continued

Note that both of these accelerations have the form of simple harmonic motion (see [Chapter 3](#ch-3)). Thus, this potential represents a 2-D harmonic oscillator.

1. Solve the differential equation of motion for each axis for this 2-D harmonic oscillator.

::::

(example-8-6)=

::::{admonition} Sample Problem 8-6

A particle of mass m is moving under the influence of a potential of $U = Ay^{2}e^{-x}$, where $A$ is a constant. No other forces act on the particle. **Find the work required to** **move the particle under a straight path from points** $(2,$ 1) **to** $(2,$ 3)**.**

**Solution**

To solve for the work, you can do one of two things. You can use $U = -\Delta W$ (true if there are no non-conservative forces) or you can solve for $F$ and specify that $\Delta W = \int F$d$r$.

**Case 1:** $\Delta W = -\Delta U$ **(this is the simplest of the methods).**

$$
W(1 \rightarrow 2) = -[U(2,3)-U(2,1)] = U(2,1)-U(2,3) = A(e^{-2})-A(9e^{-2}) = -8Ae^{-2}
$$

**Case 2: Solve for** $F$ **using the gradient of** $U$

$$
F_{x}= - \frac{\mathrm{d}U}{\mathrm{d}x} = Ay^{2}e^{-x}, F_{y}= - \frac{\mathrm{d}U}{\mathrm{d}y} = -2Aye^{-x}
$$

With the force, you can get work from:

$$
\begin{aligned}
W(2,1\to2,3)
&=\int F_x\,\mathrm{d}x+\int F_y\,\mathrm{d}y\\
&=\int_2^2 Ay^2e^{-x}\,\mathrm{d}x+\int_1^3(-2Aye^{-x})\,\mathrm{d}y\\
&=-2Ae^{-2}\int_1^3 y\,\mathrm{d}y\\
&=-2Ae^{-2}\left.\left(\frac12y^2\right)\right|_1^3\\
&=-8Ae^{-2}.
\end{aligned}
$$

As you can see we can get the same answer with both cases.

::::

<!-- Source PDF page 192; printed label 183. -->

(sec-8-9)=
## 8.9 Summary

::::{admonition} Key Takeaways

This chapter introduces kinetic energy, potential energy, and work. These are fundamental concepts in physics. Energy is a scalar quantity, which can make physics problems easier to solve.

We defined the concept of work as

$$
W = \int \vec{F} \cdot \mathrm{d}\vec{r}
$$

Work is always measured as a relative quantity and it can be positive or negative. Broadly, work is defined based on how a force affects the motion of a system. If the force helps the motion, then it does positive work. If the force opposes the motion, then it does negative work.

The change in work equals the change in kinetic energy through the work-kinetic energy theorem.

$$
W(r_{1}\rightarrow r_{2}) = \Delta K
$$

where the kinetic energy can be either translation (linear motion) or rotation.

$$
\begin{aligned}
K &= \frac{1}{2} mv^{2}=\Rightarrow \mathrm{for} \mathrm{translation} \\
K &= \frac{1}{2} I\omega ^{2}=\Rightarrow \mathrm{for} \mathrm{rotation}
\end{aligned}
$$

This chapter also introduced conservative forces, such as gravity, which are a class of forces where the work done is independent of the path taken, and energy is conserved.

$$
W(r_{1}\rightarrow r_{1}) = \oint \vec{F} \cdot \mathrm{d}\vec{r} = 0
$$

$$
\vec{\nabla} \times \vec{F} = 0
$$

Conservative forces are also associated with a potential energy, defined by:

$$
\vec{F} = -\vec{\nabla}U
$$

The potential energy is important to setting how a system, when released, will move because it directly connects to a force. The chapter briefly introduces saddle points, which are regions of local stability or instability within a potential field. Examples of conservative forces and potential energy are given for gravity.

::::

<!-- Source PDF page 193; printed label 184. -->

::::{admonition} Continued

For systems with only conservative forces,

$$
\Delta E = \Delta (K + U)
$$

which is the equation of energy conservation.

::::

::::{admonition} Important Equations

**Work:**

$$
W = \int \vec{F} \cdot \mathrm{d}\vec{r}
$$

$$
W(r_{1}\rightarrow r_{2}) = -W(r_{2}\rightarrow r_{1}) =\Rightarrow \mathrm{for} \mathrm{conservative} \mathrm{forces}
$$

**Work Kinetic Energy Theorem:**

$$
W(r_{1}\rightarrow r_{2}) = \Delta K
$$

**Kinetic Energy:**

$$
\begin{aligned}
K &= \frac{1}{2} mv^{2}=\Rightarrow \mathrm{for} \mathrm{translation} \\
K &= \frac{1}{2} I\omega ^{2}=\Rightarrow \mathrm{for} \mathrm{rotation}
\end{aligned}
$$

**Gravitational Force:**

$$
\begin{aligned}
\vec{F}_{g}&= - \frac{GMm}{r^{2}} \hat{r} \\
\vec{g} &= - \frac{GM}{r^{2}} \hat{r}
\end{aligned}
$$

**Escape Velocity:**

$$
v=\sqrt{\frac{2GM_E}{R_E}}.
$$

**Conservative Forces:**

$$
W(r_{1}\rightarrow r_{1}) = \oint \vec{F} \cdot \mathrm{d}\vec{r} = 0
$$

$$
\vec{\nabla} \times \vec{F} = 0
$$

$$
\vec{F} = -\vec{\nabla}U
$$

::::

<!-- Source PDF page 194; printed label 185. -->

::::{admonition} Continued

**Potential Energy:**

$$
U(r_{1}\rightarrow r_{2}) = -\int_{r_{1}}^{r_{2}} \vec{F} \cdot \mathrm{d}\vec{r} = -W_{con}(r_{1}\rightarrow r_{2})
$$

**Conservation of Energy:**

$$
\Delta E = \Delta (K + U)
$$

::::

<!-- Source PDF page 195; printed label 186. -->

(sec-8-10)=
## 8.10 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-8-1)=

::::{admonition} Practice Problem 8-1

Find the work done in each of the following cases:

a) Lifting a crate of mass $m$ from the floor to a table of height $h$.

b) Pushing a 1000 kg car 100 m up a $10^{\circ}$ incline at constant speed. Neglect friction.

c) A particle moving under a force $\vec{F} = (x^{2}+ 3x + 4)\hat{\imath}$ from $x$ = 1 to $x$ = 3.

::::

(problem-8-2)=

::::{admonition} Practice Problem 8-2

Calculate the escape velocity for the Sun at:

a) The surface of the Sun.

b) At the average orbital radius of the Earth (1 au). Compare this to the escape velocity of the Earth.

c) The average orbital radius of Neptune (30.1 au).

d) Plot the escape velocity as a function of distance from the Sun.

::::

(problem-8-3)=

::::{admonition} Practice Problem 8-3

For each of the following forces, determine if the force is conservative.

$$
\mathrm{a}) \vec{F} = (xy)\hat{\imath} + (yz)\hat{\jmath} + (xz)\hat{k}
$$

$$
\mathrm{b}) \vec{F} = (xz)\hat{\imath} + (y^{3}z^{2})\hat{\jmath} + (x^{2}z)\hat{k}
$$

$$
\mathrm{c}) \vec{F} = (yz)\hat{\imath} + (xz)\hat{\jmath} + (xy)\hat{k}
$$

d) $\vec{F} = r\sin (2\varphi)\hat{r} + r\cos (2\varphi)\hat{\varphi} + 3\hat{z}$ (Hint: use cylindrical coordinates)

::::

(problem-8-4)=

::::{admonition} Practice Problem 8-4

A force has the form $\vec{F} = (ax + by^{2})\hat{\imath} + (cxy)\hat{\jmath}$ , where $a, b$, and $c$ are all constants. Under what condition(s) is this force conservative?

::::

<!-- Source PDF page 196; printed label 187. -->

(problem-8-5)=

::::{admonition} Practice Problem 8-5

What value of $c$ will make

$$
\vec{F}=\left(\frac{z}{y}\right)\hat{\imath}
+c\left(\frac{xz}{y^2}\right)\hat{\jmath}
+\left(\frac{x}{y}\right)\hat{k}
$$

a conservative force?

::::

(problem-8-6)=

::::{admonition} Practice Problem 8-6

Find the equation for the conservative force that produces the following potentials:

$$
\mathrm{a}) U = 2x + 3y^{2}+ 4z^{2}
$$

$$
\mathrm{b}) U = x^{2}y^{2}+ z^{3}
$$

::::

(problem-8-7)=

::::{admonition} Practice Problem 8-7

A particle can move only along the $x-$axis. It is in a potential defined as $U = Bx + A/x$, where $B$ and $A$ are constants. What is the equilibrium position of this particle?

::::

(problem-8-8)=

::::{admonition} Practice Problem 8-8

A particle of mass m moves under a potential of $U(x,y,z) = ax + by^{2}+ cz^{3}$ with no other forces acting on it. The parameters $a, b$, and $c$ are all constants. If the particle is momentarily at rest at position $(1,1,$ 1), what is its speed at the origin? (Hint: you do not need to solve any differential equations of motion for this problem.)

::::

<!-- Source PDF page 197; printed label 188. -->

(problem-8-9)=

::::{admonition} Practice Problem 8-9

Famous tennis player Serena Williams is playing a match when her opponent sends the $0.0577$ kg tennis ball is $1.5$ m above the ground and has a speed of $20.0$ m/s. Williams hits the ball, doing 50 J of work on it. However, due to air resistance the energy of the ball halves by the time it hits the ground.

a) Determine the potential energy of the ball before Williams hits it.

b) Determine the kinetic energy of the ball before Williams spikes it.

c) Determine the total mechanical energy of the ball before Williams hits it.

d) Determine the total mechanical energy of the ball upon hitting the ground on the opponent’s side of the net.

e) Determine the speed of the ball upon hitting the ground on the opponent’s side of the net.

::::

(problem-8-10)=

::::{admonition} Practice Problem 8-10

Consider the forces $F_{1}= x\hat{\imath} + y\hat{\jmath}$ , and $F_{2}= y\hat{\imath} - x\hat{\jmath}$ .

a) Find the work done by both forces to move a particle from position $(0,$ 0) to $(0,$ 1) and then the work done to move the particle from position $(0,$ 1) to $(1,$ 1)

b) Find the work done by both forces to move a particle from position $(0,$ 0) to $(1,$ 1) using a direct path (e.g., using the line $y = x)$.

c) Note that the initial and final points in a) and b) are the same. How does the total work done from both forces compare between a) and b)? What does that mean for the forces?

d) Verify your answer for c) by taking the curl of both forces.

::::
