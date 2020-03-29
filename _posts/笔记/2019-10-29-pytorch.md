---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---


## PyTorch problems collect

> cited from [60 min blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)

### 1. NumPy Bridge

Converting a Torch Tensor to a NumPy array and vice versa:

```python
a = torch.ones(5)
b = a.numpy()

a = np.ones(5)
b = torch.from_numpy(a)
```

The Torch Tensor and NumPy array will **share their underlying memory locations** (if the Torch Tensor is on CPU), and changing one will change the other.



### 2. CUDA Tensors

Tensors can be moved onto any device using the `.to` method.

```python
# let us run this cell only if CUDA is available
# We will use ``torch.device`` objects to move tensors in and out of GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    # could simply use x.cuda()
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
```

Out:

```
tensor([0.6313], device='cuda:0')
tensor([0.6313], dtype=torch.float64)
```



### 3. `autograd` package

`torch.Tensor` is the central class of the package. If you set its attribute `.requires_grad` as `True`, it starts to track all operations on it. The tensors created as a result of an operation wiil have a `grad_fn`.When you finish your computation you can call `.backward()` and have all the gradients computed automatically. The gradient for this tensor will be accumulated into `.grad` attribute.

```python
x = torch.ones(2, 2, requires_grad=True)

a = torch.randn(2, 2)
a.requires_grad_(True)
```

#### Gradients

Call `.backward()` to backprop.

```python
y = x + 2
z = y * y * 3
out = z.mean()
out.backward()
```

Because `out` contains a single scalar, `out.backward()` is equivalent to `out.backward(torch.tensor(1.))`.

Print gradients d(out)/dx:

```python
print(x.grad)
```

Mathematically, if you have a vector valued function $\vec{y}=f(\vec{x})$, then the gradient of $\vec{y}$ with respect to $\vec{x}$ is a Jacobian matrix:
$$
J=\left(\begin{array}{ccc}{\frac{\partial y_{1}}{\partial x_{1}}} & {\cdots} & {\frac{\partial y_{1}}{\partial x_{n}}} \\ {\vdots} & {\ddots} & {\vdots} \\ {\frac{\partial y_{m}}{\partial x_{1}}} & {\cdots} & {\frac{\partial y_{m}}{\partial x_{n}}}\end{array}\right)
$$
Generally speaking, `torch.autograd` is an engine for computing vector-Jacobian product. Given a vector $v=\left(\begin{array}{llll}{v_{1}} & {v_{2}} & {\cdots} & {v_{m}}\end{array}\right)^{T}$, it computes $v^{T} \cdot J$. If $\vec{v}$ happens to be the gradient of a scalar function $l=g(\vec{y})$, that is, $v=\left(\begin{array}{ccc}{\frac{\partial l}{\partial y_{1}}} & {\dots} & {\frac{\partial l}{\partial y_{m}}}\end{array}\right)^{T}$, then by the chain rule, the vector-Jacobian product would be the gradient of $l$ with respect to $\vec{x}$:
$$
J^{T} \cdot v=\left(\begin{array}{ccc}{\frac{\partial y_{1}}{\partial x_{1}}} & {\cdots} & {\frac{\partial y_{m}}{\partial x_{1}}} \\ {\vdots} & {\ddots} & {\vdots} \\ {\frac{\partial y_{1}}{\partial x_{n}}} & {\cdots} & {\frac{\partial y_{m}}{\partial x_{n}}}\end{array}\right)\left(\begin{array}{c}{\frac{\partial l}{\partial y_{1}}} \\ {\vdots} \\ {\frac{\partial l}{\partial y_{m}}}\end{array}\right)=\left(\begin{array}{c}{\frac{\partial l}{\partial x_{1}}} \\ {\vdots} \\ {\frac{\partial l}{\partial x_{n}}}\end{array}\right)
$$
For example,

```python
x = torch.randn(3, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y = y * 2
```

Now in this case `y` is no longer a scalar. `torch.autograd` could not compute the full Jacobian directly, but if we just want the vector-Jacobian product, simply pass the vector to `backward` as argument:

```python
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
```



### 4. Neural networks

Neural networks can be constructed using the `torch.nn` package.

`nn` depends on `autograd` to define models and differentiate them. An `nn.Module` contains layers, and a method `forward(input)`that returns the `output`.

A typical training procedure for a neural network is as follows:

- Define the neural network that has some learnable parameters (or weights)
- Iterate over a dataset of inputs
- Process input through the network
- Compute the loss (how far is the output from being correct)
- Propagate gradients back into the network’s parameters
- Update the weights of the network, typically using a simple update rule: `weight = weight - learning_rate * gradient`

#### `torch.nn.Conv2d`

```python
class torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
```



> Collected problems

### 5. `nn.Variable`

#### `nn.Parameter`

Parameter, in its raw form, is a tensor i.e. a multi dimensional matrix. It sub-classes the Variable class.



### 6. `nn.forward`

In an outer forward function,

```python
def forward(self, nodes):
	embeds = self.enc(nodes)  # call self.enc.forward(nodes)
	scores = self.weight.mm(embeds)
	return scores.t()
```

When you call the model directly, the internal `__call__` function is used. This function manages all registered hooks and calls forward afterwards. That’s also the reason you should call the model directly, because otherwise your hooks might not work etc.



### 7. Multi-label loss function







