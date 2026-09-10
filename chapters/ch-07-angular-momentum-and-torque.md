(ch-7)=
# 7. Angular Momentum and Torque

<!-- Source PDF page 147; printed label 138. -->

::::{admonition} Learning Objectives

- Introduce angular momentum and rotational dynamics

- Introduce torques and identify Newton’s second law for torques

- Solve equations of motion with simple torques

- Solve equations of motion with both rotational and translational motion

::::

In this chapter, we will discuss rotational motion in the context of angular momentum and torques, and we will apply Newton’s Laws to force problems that involve rotation.

(sec-7-1)=
## 7.1 Angular Momentum

In [Chapter 6](#ch-6), we introduced linear momentum, $\vec{p} = m\vec{v}$. But objects can also move by rotation (spinning), and the momentum of a body as it undergoes rotation is called *angular* *momentum*. We define the angular momentum of a particle as:

$$
\vec{l}_{i}= \vec{r}_{i}\times \vec{p}_{i}
$$ (eq-7-1)

where $\vec{r}_{i}$ is the position of the particle relative to the origin, and $\vec{p}_{i}$ is the momentum of that particle. The total angular momentum of a system of particles is the sum of all the particles angular momentum’s:

$$
\vec{L} = \sum \vec{l}_{i}= \sum (\vec{r}_{i}\times \vec{p}_{i})
$$ (eq-7-2)

Note: The angular momentum is a vector quantity. The direction of the vector is given by the vector cross product of $\vec{r}$ and $\vec{p}$ (see [Chapter 1.5.2](#sec-1-5-2) for a review of cross products).

Angular momentum is tied to circular motion. It describes any motion where there is rotation about an axis or arc-like movement. For example, an object moving in a straight line will have no angular momentum because $\vec{r}_{i}$ is parallel to $\vec{p}_{i}$ (cross product is zero). An object also has no angular momentum if it is stationary $(\vec{p}_{i}$ = 0) or it is at the origin

$$
(\vec{r}_{i}= 0).
$$

Like linear momentum $(\vec{p}$ ), the angular momentum in an isolated system is conserved.

<!-- Source PDF page 148; printed label 139. -->

(sec-7-2)=
## 7.2 Rotational Dynamics

(sec-7-2-1)=
### 7.2.1 Rotational Dynamics from Newton’s Laws

Another form of Newton’s laws comes from the conservation of angular momentum rather than the conservation of linear momentum. With Newton’s second law, the change in linear momentum with time is equal to the net force acting on the system.

$$
\sum \vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}
$$

Now, consider the time derivative of angular momentum. For simplicity, let’s look at a single particle of mass $m_{i}$ located at a distance $r_{i}$ from the origin:

$$
\begin{aligned}
\frac{\mathrm{d}\vec{l}_{i}}{\mathrm{d}t} &= \frac{\mathrm{d}}{\mathrm{d}t} (\vec{r}_{i}\times \vec{p}_{i}) \\
&= \frac{\mathrm{d}}{\mathrm{d}t}[\vec{r}_{i}\times (m_{i}\dot{\vec{r}}_{i})] =\Rightarrow \mathrm{assume} \mathrm{mass} \mathrm{is} \mathrm{constant} \\
&= m_{i}(\dot{\vec{r}}_{i}\times \dot{\vec{r}}_{i}+ \vec{r}_{i}\times \ddot{\vec{r}}_{i}) =\Rightarrow \mathrm{apply} \mathrm{the} \mathrm{time} \mathrm{derivative} \mathrm{to} \mathrm{each} \mathrm{term} \\
&= m_{i}(0 + \vec{r}_{i}\times \ddot{\vec{r}}_{i}) =\Rightarrow \mathrm{the} \mathrm{cross} \mathrm{product} \mathrm{of} \mathrm{two} \mathrm{identical} \mathrm{vectors} \mathrm{is} \mathrm{zero} \\
&= \vec{r}_{i}\times (m_{i}\ddot{\vec{r}}_{i}) =\Rightarrow \mathrm{mass} \mathrm{is} \mathrm{a} \mathrm{constant}, \mathrm{so} \mathrm{you} \mathrm{can} \mathrm{put} \mathrm{it} \mathrm{anywhere} \\
&= \vec{r}_{i}\times \vec{F}_{i}=\Rightarrow \mathrm{recall} \mathrm{that} F = ma = m\ddot{r} \mathrm{for} \mathrm{constant} \mathrm{mass}
\end{aligned}
$$

We get that the time derivative of the angular momentum equals to the cross product of $\vec{r}$ and $\vec{F}$ . This cross product is also known as the torque, $\vec{\tau}$.

$$
\vec{\tau}_{i}= \vec{r}_{i}\times \vec{F}_{i}
$$ (eq-7-3)

Now, if we have a collection of particles, then we need to sum up all their individual contributions. This yields:

$$
\sum\vec{\tau}_{i}= \sum \frac{\mathrm{d}\vec{l}_{i}}{\mathrm{d}t} = \frac{\mathrm{d}\vec{L}}{\mathrm{d}t}
$$ (eq-7-4)

where $\vec{L}$ is the total angular momentum of a system. Thus, we find that the net torque acting on a system is equal to the time derivative of the total angular momentum of that system. Equation 7.4 is Newton’s second law for rotation.

If you have a rigid body instead of a system of independent particles, then all the mass elements in the body will rotate together with the same angular velocity, $\omega$, and angular acceleration, $\alpha$ (e.g., the body does not deform). The magnitude of the total angular momentum, $L$, of a body is:

$$
L = I\omega
$$ (eq-7-5)

where $I$ is the moment of inertia of the system of particles (see [Section 7.2.2](#sec-7-2-2) for details).

<!-- Source PDF page 149; printed label 140. -->

Combining our equation for the total angular momentum (Equation 7.5) with the equation for the net torque (Equation 7.4), we get:

$$
\sum\vec{\tau}=\frac{\mathrm{d}\vec{L}}{\mathrm{d}t}
=\frac{\mathrm{d}(I\vec{\omega})}{\mathrm{d}t}
=I\frac{\mathrm{d}\vec{\omega}}{\mathrm{d}t}
=I\vec{\alpha},
$$

where $I$ is constant in time because the system does not deform.

So similarly to $F = ma$ for the net force, we have $\tau = I\alpha$ for the net torque.

::::{tip} Quick Question

1. Consider a planet in a circular orbit around a star with only the gravitational force acting on the planet. What is the equation for the net torque? Use $\sum \tau = I\alpha$ and

$$
\vec{\tau} = \vec{r} \times \vec{F}.
$$

::::

::::{admonition} Torques in the Earth-Moon System

You’ve probably heard that the Moon causes tides on

:::{image} ../images/figures/figure-p149-1.png
:alt: Figure shows a representation of the Earth-Moon system, exaggerating the tidal bulge to show torque.
:width: 204px
:align: center
:::

Earth. The tides don’t occur right when the Moon is overhead, instead the tides are ahead of the Moon. As a consequence, the Earth’s tides bulge at an angle to the Moon. This bulge pulls on the Moon and the Moon in return pulls on the bulge (equal and opposite reactions), see figure (not to scale). Because these tiny forces are at an angle relative to the Earth-Moon radial line, they will each cause a torque. The torque on the Moon pulls the Moon ahead in its orbit slightly (the Moon gains momentum), whereas the torque on Earth drags the Earth slightly back in its spin (the Earth loses momentum). This is a case of angular momentum conservation! The net effect is very small, but the Moon is slowly moving away from us (at a rate of $\sim 40$ mm per year) and the Earth’s day is slowly increasing (by $\sim 2$ ms per century). For more information, see the [Wikipedia webpage](https://en.wikipedia.org/wiki/Tidal_acceleration) and [Explaining Science’s](https://explainingscience.org/2014/05/27/the-days-are-getting-longer/) [webpage](https://explainingscience.org/2014/05/27/the-days-are-getting-longer/) on tidal acceleration and the day on Earth.

::::

(sec-7-2-2)=
### 7.2.2 Moment of Inertia

The moment of inertia, $I$, is an important quantity in rotation. It represents how the mass of the system is distributed as a function of position and describes how efficiently the system can be rotated. It is defined as:

$$
I = \sum_{i}m_{i}r_{i}^{2}
$$ (eq-7-6)

<!-- Source PDF page 150; printed label 141. -->

where $m_{i}$ is the mass of a tiny piece of the system and $r_{i}$ is the distance between that mass and the rotation axis (pivot point) of that system.

For example, [Figure 7.1](#fig-7-1) shows an irregular shaped mass that is free to rotate back and forth about a pivot point toward its top. The position vector $\vec{r}_{i}$ is defined for each mass element in the object as measured from the pivot point. You must sum up all mass elements to measure the full moment of inertia for any object. Note that any mass elements at the position of the rotation axis have zero contribution to the moment of inertia because $\vec{r}_{i}$ = 0.

:::{figure} ../images/figures/figure-7-1.png
:label: fig-7-1
:enumerator: 7.1
:alt: Figure 7.1 from the source textbook
:width: 163px

Definition of the moment of inertia. This object will rotate about the fixed pivot point. A tiny section of mass $m_{i}$ is located a distance $r_{i}$ from that pivot point. The total moment of inertia of this system is $I = \sum(m_{i}r_{i}^{2})$ for the whole system.
:::

::::{tip} Quick Questions

1. Try calculating the moment of inertia for a simple geometric shape like a uniform ring or disk for an axis through the centre (see [Appendix A.4](#sec-A-4) for the solutions to many shapes).

2. Show that $L = I\omega$ from $\vec{L} = \vec{r} \times \vec{p}$ for circular motion. Hint: Recall that $\vec{r} \perp \vec{p}$ for circular motion.

::::

::::{admonition} Changing your moment of inertia

You can change the moment of inertia by changing the distribution of mass. For example, you could re-arrange your mass. A figure skater is an example of this. When they spin with their arms out, their moment of inertia is at its highest because they have arranged their mass (their arms) at larger radii, $I = \sum m_{i} r_{i}^{2}$. Conversely, when they bring their arms in, their moment of inertia is smaller. Since their total angular momentum $L$ must be conserved, when the skater’s arms are out, their speed will be slower and when their arms are tucked in, their speed will be faster $(L$ = constant = $I\omega$, so if $I$ increases, $\omega$ decreases and vice versa). See also: [Video connecting rotation with the moment of inertia](https://www.youtube.com/watch?v=M6PuutIm5h4) [Video on figure skating](https://www.youtube.com/watch?v=0RVyhd3E9hY)

::::

See [Appendix A.4](#sec-A-4) for a chart of basic shapes and their moments of inertia. Most of these equations are relative to a rotation axis through the centre of mass, whereas in practice, the rotation axis could be at a different location. If you change the location of the rotation axis, you can also change the mass distribution and the moment of inertia. We can calculate the new moment of inertia using the *parallel axis theorem*.

<!-- Source PDF page 151; printed label 142. -->

Equation 7.7 gives the parallel axis theorem. Consider an object that has a moment of inertia about its centre of mass of $I_{cm}$. If you were to pivot that object at a point $P$ that is a distance $d$ from the centre of mass, the moment of inertia about point $P$ would be.

$$
I_{p}= I_{cm}+ Md^{2}
$$ (eq-7-7)

where $I_{p}$ is the moment of inertia about $P$ and $M$ is the total mass of the object.

::::{admonition} Lance’s Thoughts

The power of the parallel axis theorem shines through when you have a strange or unusual object that you can break into parts with individually easy moments. Once you’ve got those, you essentially stack them using the parallel axis theorem and add them all up. Don’t forget to calculate the centre of mass, too.

::::

(sec-7-2-3)=
### 7.2.3 Direction of Torque and Angular Momentum

Torque and angular momentum are vectors, where their directions are defined by a vector cross product, which makes finding their directions more challenging. There are several ways to get the directions. First, you can use the RHR or matrix determinant to get the direction from the definition of each vector, e.g., $\vec{\tau} = \vec{r} \times \vec{F}$ . See [Chapter 1.5.2](#sec-1-5-2) for a review of the vector cross product.

Second, you can use the RHR for rotation to connect the rotation of a system to the direction of its torque or angular momentum vectors. To apply the RHR for rotation, curl your fingers in the direction of rotation and your thumb will point in the direction of the torque vector (see also [Figure 7.2](#fig-7-2)). Note you can also use the RHR for rotation to get the direction of rotation if you know the direction of torque.

:::{figure} ../images/figures/figure-7-2.png
:label: fig-7-2
:enumerator: 7.2
:alt: Cartoon demonstrating the rotational right-hand rule to determine the direction of the torque vector.
:width: 195px

Right hand rule for connecting the direction of rotation with the direction of the torque vector.
:::

If the torque vector points out of the page (e.g., toward you), then the system is rotating counter-clockwise. If the torque vector points into the page (away from you), then the system is rotating clockwise. When solving problems, you will want to define which of these two rotation directions (counter-clockwise versus clockwise) is positive.

<!-- Source PDF page 152; printed label 143. -->

::::{admonition} Cora’s Thoughts

Another way to think of torques is in the context of screws. When twisting a screw clockwise, it gets tighter and moves into the page which is the direction of that torque. When twisting a screw counterclockwise it loosens and moves out of the page, which is the direction of its torque. The direction of the movement of a screw is the same as the direction of its torque.

:::{figure} ../images/figures/figure-7-3.png
:label: fig-7-3
:enumerator: 7.3
:alt: Cartoon showing how the two possible rotation directions for a screw connect to the direction of the torque vector as an example of the right-hand rule.
:width: 372px

The motion of the screws can be remembered by the old axiom “righty-tighty and lefty-loosey.”
:::

::::

(sec-7-3)=
## 7.3 The Pendulum Revisited

Let’s return to the pendulum program from [Chapter 3.4](#sec-3-4), but this time, we’re going to solve it using torques and angular motion instead of forces and linear motion. Here is our sketch of the pendulum and the free-body diagram from before.

:::{figure} ../images/figures/figure-7-4.png
:label: fig-7-4
:enumerator: 7.4
:alt: Figure 7.4 from the source textbook
:width: 455px

Example of a simple pendulum. Left: The mass is in equilibrium when it is vertically downward and displaced from equilibrium when shifted an angle $\theta$ from the vertical axis. A restoring force $(F)$ moves the pendulum back to equilibrium. Right: The free-body diagram shows the labeled forces tension $(T)$ in red, gravity $(mg)$ in blue, and the restoring force $(mg\sin \theta)$ in magenta. Shown in dotted-red is the component of gravity that balances tension $(mg\cos \theta)$.
:::

The restoring force acting on the pendulum is given by $F = -mg\sin \theta$. The torque acting on the pendulum is then $\vec{\tau} = \vec{r}\times \vec{F}$ . So we need to find $\vec{r}, \vec{F}$ , and the angle between them.

<!-- Source PDF page 153; printed label 144. -->

::::{tip} Quick Question

1. What is the direction of the torque vector for the pendulum shown in the above figure? Use the RHR to find it.

2. Describe the torque vector through one full period of the pendulum’s motion. What is the torque at the maxima versus the equilibrium point?

::::

For our simple pendulum, $r = L$ is the distance from the pivot point to where the force is applied, which is fixed. $F$ is the restoring force, $F = -mg\sin \theta$. By definition, the restoring force is perpendicular to the radius vector (the restoring force is given by the component of gravity that is perpendicular to the radius vector along the string, see [Figure 7.4](#fig-7-4)). If $\vec{r} \perp \vec{F}$ , then $\tau = rF$. Putting this information in, we have:

$$
\tau = |\vec{r} \times \vec{F}|
$$

$$
\tau = rF
$$

$$
\tau = -mgL\sin \theta
$$

From Newton’s second law for rotation, the net torque is equal to:

$$
\sum \tau = I\alpha
$$ (eq-7-8)

Since there is only one torque acting on the system (from the restoring force),

$$
I\alpha = -mgL\sin \theta
$$

$$
\begin{aligned}
\alpha &= - \frac{mgL}{I} \sin \theta \\
\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} &= - \frac{mgL}{I} \sin \theta
\end{aligned}
$$

This form of the differential equation of motion is difficult to solve. But, we can make it solvable by assuming that the angle formed by the pendulum and the vertical axis is small $(\theta \ll$ 1 in radian units). If $\theta$ is small, then $\sin \theta \approx \theta$ (See [Appendix B](#app-b)) and

$$
\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + \frac{mgL}{I} \theta = 0
$$

Now our equation is in the form of a simple differential equation of motion (see [Chapter 3](#ch-3)), and we know how to solve an equation in this format. The solution for $x(t)$ is a cos function with an angular frequency given by the coefficient in front of the $\theta$ term.

But wait, that isn’t the exact same solution as what we had before in [Chapter 3.4](#sec-3-4). Well, there is one more step we need to do. We need to define the moment of inertia, $I$.

For a point mass located a distance $L$ from the pivot point, the moment of inertia is just $I = mL^{2}$. If you plug in $I = mL^{2}$ into the differential equation of motion, we get:

$$
\frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + \frac{g}{L} \theta = 0
$$

<!-- Source PDF page 154; printed label 145. -->

which is exactly the same as what we had before in [Chapter 3](#ch-3), and it once again gives us an angular frequency of $\omega_0=\sqrt{g/L}$.

::::{admonition} Force vs Torque

The torque method gives $\ddot{\theta}+ \frac{mgL}{I} \theta$ = 0, which is a more general solution to describe the motion of a pendulum. This solution holds for a single pendulum of any shape. If you can write down the moment of inertia for that pendulum, you can solve its equation of motion. See [Appendix A.4](#sec-A-4) for basic geometric shapes. Or you can find a [table of](https://courses.lumenlearning.com/physics/chapter/10-5-angular-momentum-and-its-conservation/) [solutions online](https://courses.lumenlearning.com/physics/chapter/10-5-angular-momentum-and-its-conservation/).

Complex pendulum shapes are hard to solve with the linear force method. Think about the problem you are trying to solve, and consider using torques rather than forces!

::::

::::{tip} Quick Questions

1. Find the angular frequency, $\omega _{0}$, of a pendulum that consists of a rod hanging from the pivot point at one end. Assume the rod has mass $M$ and length $L$.

2. You construct a pendulum by attaching a ring to a massless rod and setting it into periodic motion. Find the angular frequency, $\omega _{0}$, of this pendulum if the rod has a length $L$, and the ring has a mass $M$ and radius $R$.

3. You have a massless rod of length $L$ to which you can attach either a solid sphere or a spherical shell. The solid sphere and spherical shells have masses and radii of (1) $M, R, (2) 2M, \frac{1}{2} R$, or (3) $\frac{1}{2} M 2R$. Which object will give your pendulum the shortest period and which will give you the longest period of oscillation?

::::

(sec-7-4)=
## 7.4 The Physical Pendulum

By definition, a physical pendulum is any rigid body that is free to swing about a pivot point. [Figure 7.5](#fig-7-5) is an example of a physical pendulum.

:::{figure} ../images/figures/figure-7-5.png
:label: fig-7-5
:enumerator: 7.5
:alt: Figure shows a physical pendulum of irregular shape with a pivot point near the top and the restoring force at the centre of mass toward the bottom.
:width: 130px

A physical pendulum. The body is suspended from the point $O$ and allowed to rotate freely by an angle $\theta$. The centre of mass of the system $C$ is located a distance $h$ from the pivot point. The total mass of the objects is $m$. The purple arrow shows the restoring force acting on this pendulum.
:::

Although the object has an irregular shape, the problem can be simplified by expressing the motion for the centre of mass rather than for each individual mass element of the object.

<!-- Source PDF page 155; printed label 146. -->

You can think of this as compressing the mass of the entire object to a single point located at the centre of mass (point C) and then determining how the restoring force acts on that compressed object. The force acting on this physical pendulum is $F = -mg\sin \theta$ at the position C. This simplification is another strength of the centre of mass.

The torque acting at the centre of mass is given by $\vec{\tau} = \vec{r}_{cm}\times F$. The $\vec{r}_{cm}$ vector is the vector from the pivot point to the centre of mass. We know that $\vec{r}_{cm}\perp F$, which means that our torque has a magnitude of $\tau = r_{cm}F = -mgh\sin \theta \approx -mgh\theta$ for small angles.

If this is the only torque acting on our system, Equation (7.8) becomes:

$$
\sum \tau = I\alpha
$$

$$
I\alpha = -mgh\theta
$$

$$
0 = I\alpha + mgh\theta
$$

$$
0 = \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + \frac{mgh}{I} \theta
$$

This is the exact same equation of motion as the simple pendulum, only that the simple pendulum had the length of the rope to the mass, $L$, and the physical pendulum has the distance between the pivot and the centre of mass $h$.

So for a physical pendulum of any shape swinging from a pivot point that is a distance $h$ from its centre of mass, we find that the motion can be described with an angular frequency of $\omega_0=\sqrt{mgh/I}$, where $h$ is the distance to the centre of mass and $I$ is the moment of inertia for the body. Note that for an object to be a physical pendulum, the pivot point must be located away from the centre of mass (at the centre of mass, $h=0$).

(sec-7-5)=
## 7.5 Example of a Physical Pendulum

In this example, we will determine the equation of motion for a physical pendulum corresponding to a single simple harmonic oscillator.

(example-7-1)=

::::{admonition} Sample Problem 7-1

A disk of mass $m_{d}$ and radius $R$ is attached to a rod of mass $m_{r}$ and length $L$. **What** **is the period of oscillations if this object is set in motion about the other** **end of the rod?** See [Figure 7.6](#fig-7-6).

::::

<!-- Source PDF page 156; printed label 147. -->

:::{figure} ../images/figures/figure-7-6.png
:label: fig-7-6
:enumerator: 7.6
:alt: Figure shows a physical pendulum consisting of a rod and disk with the pivot point at the top of the rod and the disk at the bottom of the rod.
:width: 155px

Diagram of the physical pendulum. This physical pendulum is constructed from a disk and rod. The disk is attached to the rod at one end and allowed to rotate freely at the other end of the rod. The disk has mass $m_{d}$ and radius $R$. The rod has mass $m_{r}$ and length $L$.
:::

**Solution**

This system is not a simple pendulum (e.g., a point source at the end of a rope), because the rod has mass and disk has mass and dimension. So you need to consider this as a physical pendulum.

The solution for a physical pendulum is:

$$
0 = \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} + \frac{Mgh\theta}{I}
$$

where $h$ is the distance to the centre of mass, $M=m_r+m_d$ is the total mass of the system, and $I$ is the moment of inertia for the system (see [Chapter 7.4](#sec-7-4)). The solution is a cosine function with an angular frequency of $\omega_0=\sqrt{Mgh/I}$. So the solution for the period of rotation is:

$$
T = \frac{2\pi}{\omega _{0}}
$$

$$
T=2\pi\sqrt{\frac{I}{Mgh}}.
$$

Getting the equation for the period isn’t the hard part. The trick for this problem is defining $h$ and $I$.

Let’s start with $h$, which is the distance from the pivot to the centre of mass of the pendulum. Since both the rod and the disk have mass, the centre of mass of the two combined is located at a mass-averaged position between the two. We will need to calculate the position of the centre of mass (see [Chapter 6.4](#sec-6-4) for a definition of the centre of mass).

<!-- Source PDF page 157; printed label 148. -->

Fortunately, the centre of mass for each component of the pendulum is easy to calculate. The centre of mass for a uniform rod would be its midpoint and the centre of mass for a uniform disk would be its midpoint. For the rod, $r_{cm,r}= \frac{L}{2}$ (location of the midpoint of the rod from the pivot) whereas for the disk, $r_{cm,d}= L$ (location of the midpoint of the disk from the pivot). So we can treat both systems as effective point masses with all their mass at the respective centre-of-mass positions.

Thus, the centre of mass for this physical pendulum is:

$$
h = \frac{m_{r}r_{cm,r}+ m_{d}r_{cm,d}}{m_{r}+ m_{d}}
$$

$$
h = \frac{m_{r}(\frac{1}{2} L) + m_{d}L}{M}
$$

where $M = m_{r}+ m_{d}$ is the total mass of the pendulum.

Thus, we have a position for our centre of mass. Note that if our rod mass is very small (e.g., $m_{r}\rightarrow$ 0), then $M \rightarrow m_{d}$ and $r_{cm}\rightarrow L$, or the centre of the disk. This recovers the solution for a simple pendulum.

Now let’s look at $I$. We have two objects, a rod and a disk. To get the moment of inertia for the combined rod+disk pendulum, we can simply add the $I$ components from each object separately.

:::{figure} ../images/figures/figure-7-7.png
:label: fig-7-7
:enumerator: 7.7
:alt: Figure shows the rod only relative to the pivot point.
:width: 93px

Sketch of the rod with the pivot at one end.
:::

The moment of inertia for a rod with the axis of rotation at one end is ([Appendix A.4](#sec-A-4)):

$$
I_{rod}= \frac{1}{3} m_{r}L^{2}
$$

:::{figure} ../images/figures/figure-7-8.png
:label: fig-7-8
:enumerator: 7.8
:alt: Figure 7.8 from the source textbook
:width: 93px

Sketch of the disk with the pivot a distance $L$ from the centre of mass.
:::

<!-- Source PDF page 158; printed label 149. -->

::::{admonition} Continued

The moment of inertia for a disk with the axis of rotation through its centre of mass is ([Appendix A.4](#sec-A-4)):

$$
I_{disk}= \frac{1}{2} m_{d}R^{2}
$$

But the pivot is not located at the centre of mass. The pivot is located a distance $L$ from the centre of mass. Therefore, we need to find $I$ for the disk about the pivot point, $O$. Using the parallel axis theorem ([Chapter 7.2.2](#sec-7-2-2)), we have,

$$
I_{disk,0}= \frac{1}{2} m_{d}R^{2}+ m_{d}L^{2}
$$

Thus, the moment of inertia for the entire physical pendulum is

$$
I = I_{rod}+ I_{disk,0}= \frac{1}{3} m_{r}L^{2}+ \frac{1}{2} m_{d}R^{2}+ m_{d}L^{2}
$$

Taking our equations for $h$ and $I$, we can now solve for the period:

$$
\begin{aligned}
T
&=2\pi\sqrt{\frac{I}{Mgh}}\\
&=2\pi\sqrt{\frac{\left(\frac13m_r+m_d\right)L^2+\frac12m_dR^2}
{gL\left(\frac12m_r+m_d\right)}}.
\end{aligned}
$$

Here the total mass $M$ cancels from the denominator.

1. Find the period if the disk was attached at the midpoint of the rod instead.

::::

(sec-7-6)=
## 7.6 Example with Rolling Motion

In this case, we will consider a system rolling on a surface. In ideal cases, rolling motion occurs without slipping, which means that friction at the point of contact between the rolling object and the surface is sufficient to keep the system moving continuously by rolling motion. If the system is slipping, then you can get forward motion without rolling.

<!-- Source PDF page 159; printed label 150. -->

(example-7-2)=

::::{admonition} Sample Problem 7-2

A light cord is wrapped around the inner drum of a wheel of mass $m$ and pulled with a constant force $F$ to make the wheel roll. The wheel has a radius $R$ and the inner drum has a radius of $r$. If the wheel rolls without slipping, **what is the force of friction** **at the point of contact between the wheel and horizontal surface?**

:::{figure} ../images/figures/figure-7-9.png
:label: fig-7-9
:enumerator: 7.9
:alt: Figure shows a wheel with inner and outer radius, and a force applied at the bottom of the inner radius.
:width: 217px

The applied force $(F)$ is represented by the magenta arrow, $(r)$ is the radius of the inner drum, and $(R)$ is the radius of the wheel.
:::

**Solution**

First, make sure you know how this system will move. Pulling the cord in the direction shown will cause the wheel to rotate. Will it rotate clockwise or counter-clockwise? Well, let’s draw a free-body diagram to describe the forces at play in this motion and figure out how this system is going to move.

:::{figure} ../images/figures/figure-7-10.png
:label: fig-7-10
:enumerator: 7.10
:alt: Figure shows the free-body diagram and defined coordinate systems for the wheel.
:width: 217px

Free-body diagram of the system. The force $F$ is applied to the wheel (magenta). Also acting on the wheel are gravity (black), the normal force (blue), and friction (red). The positive $x$ and $y$ axes are shown. We have also defined the clockwise rotation direction as positive.
:::

Overall, the wheel is moving forward in the same direction as $F$ but it is also rotating. So there are two types of motion we need to consider, translation for the forward movement and rotation for the spin of the wheel. This means we will need to consider both forms of Newton’s second law.

$$
\sum F = ma_{cm}=\Rightarrow \mathrm{for} \mathrm{translation}
$$

$$
\sum \tau = I\alpha =\Rightarrow \mathrm{for} \mathrm{rotation}
$$

::::

<!-- Source PDF page 160; printed label 151. -->

Note that for the translation motion, we’re interested only in how the centre of mass is moving. That’s because the centre of mass has no rotation motion, only linear motion.

Let’s set up our coordinate system. We define $+x$ toward the right, $+y$ up, and $+\omega$ in the clockwise direction. These choices are intentional. If the linear motion is in the $+\hat{\imath}$, then the rotation should be in the clockwise direction. While we set up the coordinate system to be most intuitive, as long as you are consistent with your defined coordinate system you will still get the correct answer.

Let’s look at $\sum F = ma_{cm}$ to start. What forces do we need to worry about for the forward motion? Both gravity and the normal force act along the $y-$axis. These will be equal and opposite forces. The wheel does not rise above the ground nor does it sink below the ground. So we only care about $F$ and $f$. These are opposite in direction ([Figure 7.10](#fig-7-10)). Based on our definition of the $+x$ axis, we have $\sum F = F - f$.

*What about* $a_{cm}$*?* Keep in mind that the acceleration corresponds to the bulk forward motion of the system. If the wheel was a square box that didn’t rotate, then $a_{cm}$ would be how fast you were able to drag the box. But the magnitude of $a_{cm}$ depends on the rate of rotation because all the motion happens due to rotation (condition of rolling without slipping).

[Figure 7.11](#fig-7-11) shows a schematic of our rolling wheel. The wheel is rolling forward a distance $s$ represented by the red arc. As a result of moving forward, the centre of mass has changed position from $x_{1}$ to $x_{2}$, where $\Delta x = s$ (the translation motion is relative to the ground). That is, the system goes forward an equal distance given by the arc of the circle traveled.

:::{figure} ../images/figures/figure-7-11.png
:label: fig-7-11
:enumerator: 7.11
:alt: Figure shows how the wheel rotates an arc length S as its center of mass moves between two points.
:width: 217px

The rolling wheel of radius $R$. The centre of mass is given by the origin $(O)$ and the system moves forward a distance $s$ given by the red arc.
:::

If the system has moved a distance $s$ in time $\Delta t$. If you have *rolling without slipping*, then the centre of mass motion is given by $v_{cm} = \frac{\Delta x}{\Delta t} = \frac{s}{\Delta t}$. For very small times,

<!-- Source PDF page 161; printed label 152. -->

$\Delta t \rightarrow$ d$t, v_{cm}$ and $a_{cm}$ can be instead written as:

$$
\begin{aligned}
v_{cm}&= \frac{\mathrm{d}s}{\mathrm{d}t} \\
a_{cm}&= \frac{\mathrm{d}^{2}s}{\mathrm{d}t^{2}}
\end{aligned}
$$

But the arc length, $s$ can be written in terms of the angle $\theta$ and the radius $R$. That is, $s = R\theta$. Substituting $s = R\theta$ into our acceleration equation gives:

$$
a_{cm}= \frac{\mathrm{d}^{2}s}{\mathrm{d}t^{2}} = \frac{\mathrm{d}^{2}R\theta}{\mathrm{d}t^{2}} = R \frac{\mathrm{d}^{2}\theta}{\mathrm{d}t^{2}} = R\alpha
$$

The above equation gives the magnitude of $a_{cm}$ in terms of the rotation.

Assuming positive clockwise rotation, we need to check whether our $\alpha$ is also clockwise. To get the rotation direction, note that rolling happens at the point of contact where the base of the wheel meets the ground. There is only one force acting at the contact point (friction) and friction will point against the direction of motion. Using the RHR for rotation, the torque produced by the friction force is into the page and the rotation of the wheel will be clockwise. So $\alpha$ is in the clockwise direction and positive based on our definition.

Thus, combining the values of $\sum F$ and $a_{cm}$, we get:

$$
\sum F = ma_{cm}
$$

$$
F - f = mR\alpha
$$

::::{admonition} Definitions

Just like with $x$ and $y$, you need to define a positive and negative direction for rotation. And it is important that you stay consistent with that choice. For this example, we defined the positive axis as clockwise. By this definition, we get $a_{cm}= R\alpha$. But had we defined the positive rotation axis as counter-clockwise, then we would need to set $a_{cm}= -R\alpha$, because in this case, the rotation of the system would be counter to the defined axis. Either way is fine, just be consistent.

Here is a [video demonstration that shows positive and negative rotation](https://www.youtube.com/watch?v=Hb91ewjeiF).

::::

A key feature of this problem is the condition of rolling without slipping. This condition specifies that the rotation is entirely responsible for any forward motion such that the rotation rate can be equated to the centre of mass motion. Under this condition,

<!-- Source PDF page 162; printed label 153. -->

$$
v_{cm}= \omega R
$$

$$
a_{cm}= \alpha R
$$

where $\omega$ is the angular velocity and $\alpha$ is the angular acceleration. Note that the vector directions are not the same for these quantities. Only the magnitudes apply.

For a rigid object, $v_{cm}$ applies equally in magnitude and direction to the whole object (it is moving forward and doesn’t deform), whereas the motion from rotation depends on the radius and can be either forward or backwards. Consider the motion from translation and rotation at the contact point (where the wheel meets the ground). There are two velocities acting at that point, the translation velocity from $v_{cm}$ and the rotation velocity, $R\omega$. These two velocity are equal in magnitude, but opposite in direction (at the contact point, the wheel is moving forward with $v_{cm}$ but backwards with $\omega R$ from rotation). Therefore, the contact point is *instantaneously* at rest. If you had rolling with slipping, then the contact point would have excess motion from translation and not be at rest.

Now let’s switch to $\sum \tau = I\alpha$. This equation describes how the wheel is going to rotate. Again, rotation and translation are two separate actions, although their magnitudes are connected due to the condition of rolling without slipping. To describe the rotation, we will want to look at how the wheel is being torqued. There are two torques acting on the wheel from $F$ and $f$, so we want to find $\tau _{F}$ and $\tau _{f}$.

::::{tip} Quick Questions

1. Why do we not consider torques produced by the gravitational force or normal force?

::::

The external force is applied at the inner radius, $r$, whereas friction is acting at the outer radius $R$ of the wheel (where it hits the ground). Both forces are perpendicular to their radius vectors, which makes the math much easier. [Figure 7.12](#fig-7-12) shows a sketch of these vectors.

:::{figure} ../images/figures/figure-7-12.png
:label: fig-7-12
:enumerator: 7.12
:alt: Figure shows the direction of the radial vector and force vectors needed to calculate the torques produced by the applied force and the friction force.
:width: 310px

Sketch of how the two forces produce torques. The radius vectors are defined by the origin (centre of mass location) and the forces are shown with their directions.
:::

<!-- Source PDF page 163; printed label 154. -->

Since the forces are perpendicular to the radii vectors, we can simplify the torques to:

$$
\tau _{F}= rF
$$

$$
\tau _{f}= Rf
$$

But direction also matters. If you use the RHR, you will get that the external force produces a torque that is directed out of the page and the friction force produces a torque that is into the page. As a consequence, $\tau _{F}$ will produce rotation that is counterclockwise and $\tau _{f}$ will produce rotation that is clockwise. Based on our definition of positive clockwise rotation, the total torque of our system is:

$$
\sum \tau = Rf - rF
$$

It may seem counter intuitive to have the external force as the negative term, but this is due to our choice to define the clockwise direction as positive. Had we defined the counter-clockwise direction as positive, then we would have the external force as the positive term (but we would need a negative factor relating $a_{cm}$ and $\alpha$; see prior comment).

Now we have both forms of Newton’s law’s:

$$
\sum F = ma_{cm}=\Rightarrow F - f = mR\alpha
$$

$$
\sum \tau = I\alpha =\Rightarrow Rf - rF = I\alpha
$$

With two equations and two unknowns, $f$ (which we want) and $\alpha$, we can re-arrange these equations to solve for $f$.

$$
\begin{aligned}
\alpha &= \frac{Rf - rF}{I} (1) \\
\alpha &= \frac{F - f}{mR} (2)
\end{aligned}
$$

$$
\frac{Rf - rF}{I} = \frac{F - f}{mR} =\Rightarrow (1) = (2)
$$

$$
\begin{aligned}
f \bigg(\frac{R}{I} + \frac{1}{mR} \bigg) &= F \bigg(\frac{r}{I} + \frac{1}{mR} \bigg) \\
f \Bigg(\frac{mR^{2}+ I}{mRI} \Bigg) &= F \bigg(\frac{mRr + I}{mRI} \bigg)
\end{aligned}
$$

$$
f = F \bigg(\frac{mRr + I}{mR^{2}+ I} \bigg)
$$

To fully solve this problem, however, we need to know the moment of inertia $I$. What is $I$ for a wheel? We will assume that the wheel consists of a thick ring with an inner

<!-- Source PDF page 164; printed label 155. -->

::::{admonition} Continued

radius of $r$ and an outer radius of $R$. In this case, the rotation axis is through the centre of the wheel, so we don’t need to apply the parallel axis theorem ([Chapter 7.2.2](#sec-7-2-2)). The moment of inertia for a thick ring with an axis through its centre is $I_{CM}= \frac{1}{2} M(r_{1}^{2}+r_{2}^{2})$ (see [Appendix A.4](#sec-A-4)). For our values, this gives $I = \frac{1}{2} m(r^{2}+ R^{2})$. Adding our equation for $I$ to the problem, we get:

$$
\begin{aligned}
f &= F \Bigg(\frac{mRr + \frac{1}{2} m(r^{2}+ R^{2})}{mR^{2}+ \frac{1}{2} m(r^{2}+ R^{2})} \Bigg) \\
f &= F \frac{2Rr + r^{2}+ R^{2}}{3R^{2}+ r^{2}}
\end{aligned}
$$

1. Find the *maximum* amount of friction for the wheel if the mass is 45 kg and the coefficient of kinetic friction is $\mu _{k}= 0.15$.

2. How does the maximum amount of friction compare to the friction necessary to keep the wheel rolling without slipping? Assume $r = 7.5$ cm, $R = 12.5$ cm, and $F$ = 180 N.

3. What force should you exert on the wheel (from b) to have it move without slipping?

::::

(sec-7-7)=
## 7.7 Real-World Application

The conservation of angular momentum is a fundamental physics concept. It is sometimes referred to as Gyroscopic Motion, the tendency of a rotating object to maintain its orientation of motion. A common application you may be familiar with are fidget spinners. Fidget spinners are essentially miniature gyroscopes with a low-friction bearing to allow it to rotate longer. If you set the spinner in motion and then tilt it slowly to one side, you’ll feel it resisting the tilt, pulling back toward its original position to conserve angular momentum.

:::{figure} ../images/figures/figure-7-13.png
:label: fig-7-13
:enumerator: 7.13
:alt: Figure shows three fidget spinners with one in motion.
:width: 325px

Examples of fidget spinners. Image credit: Matthias Wewering from Pixabay
:::

While the fidget spinner is an example of a simple low-weight mechanical gyroscope, there

<!-- Source PDF page 165; printed label 156. -->

are other types, including fluid, laser, fibre-optic, and vibrational, all working on same basic principles of rotational motion. For example, with vibrational or MEMS (Micro Electro- Mechanical System) gyroscopes, the angular velocity in the sensor produces torques on vibration elements, providing measurable displacements that can then be amplified to produce an angular velocity signal. Three sensors arranged orthogonally in a single chip provide three dimensional components and track changes in orientation. This is the type of gyroscope is used in smart phones to provide image stabilization in a camera or auto-rotation, track step counts in fitness programs, and help give accurate location and positioning with accelerometers in GPS satellites.

**For more information:**

For lots of detail on the physics of fidget spinners, check out [this article](https://www.researchgate.net/publication/325741350_Fidget_Spinner_Physics) from the International Journal for Research in Applied Science and Engineering Technology by Vandana Kaushik.

For some detail on the different types of gyroscopes, see [this article](https://www.smlease.com/entries/mechanical-design-basics/what-is-gyroscope-how-gyroscopes-work-and-their-applications/) from SM Lease Design.

<!-- Source PDF page 166; printed label 157. -->

(sec-7-8)=
## 7.8 Summary

::::{admonition} Key Takeaways

This chapter introduces angular momentum and torques. Angular momentum is defined as:

$$
\vec{L} = \vec{r} \times \vec{p}
$$

And torque is defined as:

$$
\vec{\tau} = \vec{r} \times \vec{F}
$$

where both properties are vector cross products. Angular momentum and torque describe systems that are rotating. In many respects, angular momentum and torque are analogous to linear momentum and force. Newton’s second law can be written for rotation, where the net torque on a system is equal to the time derivative of the total angular momentum.

$$
\begin{aligned}
\sum \vec{\tau} &= \frac{\mathrm{d}\vec{L}}{\mathrm{d}t} \\
\sum \tau &= I\alpha
\end{aligned}
$$

A key feature of angular momentum and torques is the moment of inertia, which represents how easily a system is able to rotate.

$$
I = \sum_{i}m_{i}r_{i}^{2}
$$

In this chapter, we applied Newton’s second law for rotation to simple harmonic motion and rolling problems. In particular, we discussed the condition of rolling without slipping, which is a special physical case.

$$
v_{cm}= \omega R
$$

This condition allows you to simplify rolling problems. Rolling without slipping means that any translation (centre of mass) motion occurs due to rolling, such that forward motion can be directly connected to the rotation. If slipping occurs, then you can get forward motion independent of rotation.

::::

<!-- Source PDF page 167; printed label 158. -->

::::{admonition} Important Equations

**Angular Momentum of a Particle:**

$$
\vec{l}_{i}= \vec{r}_{i}\times \vec{p}_{i}
$$

**Total Angular Momentum:**

$$
\vec{L} = \sum \vec{l}_{i}= \sum (\vec{r}_{i}\times \vec{p}_{i})
$$

**Torque:**

$$
\vec{\tau}_{i}= \vec{r}_{i}\times \vec{F}_{i}
$$

**Newton’s second law for rotation:**

$$
\begin{aligned}
\sum \vec{\tau} &= \frac{\mathrm{d}\vec{L}}{\mathrm{d}t} \\
\sum \tau &= I\alpha
\end{aligned}
$$

**Magnitude of Total Angular Momentum:**

$$
L = I\omega
$$

**Moment of Inertia:**

$$
I = \sum_{i}m_{i}r_{i}^{2}
$$

**Parallel Axis Theorem:**

$$
I_{P}= I_{cm}+ Md^{2}
$$

**Rolling Without Slipping Condition:**

$$
v_{cm}= \omega R
$$

::::

<!-- Source PDF page 168; printed label 159. -->

(sec-7-9)=
## 7.9 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-7-1)=

::::{admonition} Practice Problem 7-1

Use the Parallel Axis Theorem to find expressions for the moments of inertia for each of the figures below. Note the location of the axis of rotation in each case.

:::{figure} ../images/figures/figure-7-14.png
:label: fig-7-14
:enumerator: 7.14
:alt: Cartoons for each of the mass configurations, described below, in the problem.
:width: 434px

Figure for [Problem 7-1](#problem-7-1).
:::

a) A thin disk of radius $R$ and mass $M$ rotating around an axis at its edge.

b) A rod of length $L$ and mass $M_{R}$ with a sphere of radius $R$ and mass $M_{S}$ attached to one end and the axis of rotation at the opposite end.

c) A rod of length $L$ and mass $M_{R}$ with a thin rectangular plate of mass $M_{P}$, length $\ell$, and width $w$ attached to one end and the axis of rotation at the opposite end.

d) A rod of length $L$ and mass $M_{R}$ with a hollow cylinder of mass $M_{C}$, inner radius $R_{1}$ and outer radius $R_{2}$ attached to one end. The axis of rotation is through the centre of the rod.

::::

<!-- Source PDF page 169; printed label 160. -->

(problem-7-2)=

::::{admonition} Practice Problem 7-2

A red giant star has a mass fifteen times that of our Sun (15 $\mathrm{M}_{\odot})$ and a radius of one astronomical unit $(1.5 \times 10^{8}$ km). It undergoes a sudden supernova, producing a neutron star with a radius of 20 km. Assuming only 1/10th of the star’s mass ends up in the neutron star, what happens to its rotation rate (angular speed)? Assume both the red giant star and the neutron star can be approximated as perfect spheres.

::::

(problem-7-3)=

::::{admonition} Practice Problem 7-3

Find expressions for the torque (magnitude and direction) in each of the following figures.

:::{figure} ../images/figures/figure-7-15.png
:label: fig-7-15
:enumerator: 7.15
:alt: Figure shows the set up for each of the cases to this problem with the force vectors or a cartoon of a pulley system.
:width: 496px

Figure for [Problem 7-3](#problem-7-3).
:::

a) A force $F$ is applied orthogonally to the end of a fulcrum of length $r$.

b) A force $F$ is applied at an angle $\theta$ to the end of a fulcrum of length $r$.

c) A mass $M$ hangs from a pulley of radius $R$. Find the torque on the pulley.

d) Two masses, $M_{1}$ and $M_{2}$, hang from opposite ends of a rope over a pulley of radius $R$. Find the equation for the torque on the pulley.

::::

<!-- Source PDF page 170; printed label 161. -->

(problem-7-4)=

::::{admonition} Practice Problem 7-4

See figure below. A piece of sticky putty of mass $m$ moves with speed $v_{0}$ and collides with a rod of length $\ell$ and mass $M$. The rod is pivoted at its centre and the putty hits the rod (and sticks to it) at the far end at an angle perpendicular to the axis of the rod.

a) Write an equation for the angular momentum before and after the collision. Assume that $M \gg m$ such that the centre of mass of the system remains at the centre of the rod.

b) What is the angular velocity $\omega$ of the resulting rotation.

:::{figure} ../images/figures/figure-7-16.png
:label: fig-7-16
:enumerator: 7.16
:alt: Figure shows a rod at rest vertically as the mass of putty approaches the upper end moving to the right.
:width: 93px

Figure for [Problem 7-4](#problem-7-4).
:::

::::

(problem-7-5)=

::::{admonition} Practice Problem 7-5

Two identical rods of mass $M$ and length $L$ are welded together forming a right angle. They are then allowed to rotate about a pivot point at their corner, producing a physical pendulum. What is the distance between the centre of mass of the physical pendulum and the pivot point?

::::

(problem-7-6)=

::::{admonition} Practice Problem 7-6

See figure below. You have a circular disk of mass $M$ and radius $R$. The disk is hanging from a pivot point located a distance $s$ from the centre of mass as shown.

a) What is the moment of inertia for the disk about the pivot point $s$?

b) What is the period of oscillations, assuming the disk is displaced a small angle from the vertical?

c) What value of $s$ gives you the smallest possible period of oscillations?

::::

<!-- Source PDF page 171; printed label 162. -->

::::{admonition} Continued

:::{figure} ../images/figures/figure-7-17.png
:label: fig-7-17
:enumerator: 7.17
:alt: Figure shows the physical pendulum which is a disk pivoted toward the upper half.
:width: 93px

Figure for [Problem 7-6](#problem-7-6).
:::

::::

(problem-7-7)=

::::{admonition} Practice Problem 7-7

A metre stick is pivoted at the 20cm mark and allowed to freely oscillate. What is the angular frequency of those oscillations assuming that the metre stick is displaced from equilibrium by a small amount?

:::{figure} ../images/figures/figure-7-18.png
:label: fig-7-18
:enumerator: 7.18
:alt: Figure shows a metre stick with the pivot point labeled as described in the problem.
:width: 62px

Figure for [Problem 7-7](#problem-7-7).
:::

::::

(problem-7-8)=

::::{admonition} Practice Problem 7-8

A Physical pendulum made of a rod of length $L$ and a sphere of radius $R$, as shown in [Figure 7-14](#fig-7-14) (top right). The rod and the sphere have the same mass, $M$. Consider the pivot point to be through the opposite end of the rod from the sphere.

a) Where is the center of mass?

b) What is the moment of inertia?

c) Find the period of oscillations for small angles.

::::

(problem-7-9)=

::::{admonition} Practice Problem 7-9

A circular disk of mass $M$ and radius $R$ rolls down an incline (angle for the incline is $\theta)$ without slipping. The moment of inertia for a disk is $\frac{1}{2} MR^{2}$.

a) Draw a free body diagram for the system.

::::

<!-- Source PDF page 172; printed label 163. -->

::::{admonition} Continued

b) Find the equations for $\sum F$ and $\sum \tau$.

c) What is the acceleration of the disk centre of mass?

d) If the coefficient of static friction is $\mu$, what is the steepest angle $\theta$ before the disk starts to slip?

:::{figure} ../images/figures/figure-7-19.png
:label: fig-7-19
:enumerator: 7.19
:alt: Figure shows a disk of radius rolling down an inclined plane.
:width: 217px

Figure for [Problem 7-9](#problem-7-9).
:::

::::
